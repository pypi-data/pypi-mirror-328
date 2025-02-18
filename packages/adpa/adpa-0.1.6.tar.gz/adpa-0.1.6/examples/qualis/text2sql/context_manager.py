"""Context manager for maintaining conversation state and query context."""
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import json
import logging

@dataclass
class QueryContext:
    focus_table: Optional[str] = None
    focus_columns: Set[str] = field(default_factory=set)
    active_filters: Dict[str, str] = field(default_factory=dict)
    temporal_context: Optional[str] = None
    last_query_time: datetime = field(default_factory=datetime.now)

@dataclass
class ContextState:
    previous_queries: List[str] = field(default_factory=list)
    current_context: QueryContext = field(default_factory=QueryContext)
    context_stack: List[QueryContext] = field(default_factory=list)
    max_stack_size: int = 10
    context_timeout: timedelta = field(default_factory=lambda: timedelta(minutes=30))

class ContextManager:
    def __init__(self):
        """Initialize the context manager."""
        self.state = ContextState()
        self.logger = logging.getLogger(__name__)

    def update_context(self, query_text: str, sql_query: str, 
                      result_info: Dict) -> None:
        """Update context based on new query and its results."""
        # Update query history
        self.state.previous_queries.append(query_text)
        if len(self.state.previous_queries) > self.state.max_stack_size:
            self.state.previous_queries.pop(0)

        # Extract and update focus
        new_focus = self._extract_focus(sql_query)
        if new_focus:
            self._push_context()
            self.state.current_context.focus_table = new_focus

        # Update columns and filters
        columns = self._extract_columns(sql_query)
        filters = self._extract_filters(sql_query)
        
        self.state.current_context.focus_columns.update(columns)
        self.state.current_context.active_filters.update(filters)
        
        # Update temporal context
        temporal = self._extract_temporal_context(sql_query)
        if temporal:
            self.state.current_context.temporal_context = temporal

        # Update timestamp
        self.state.current_context.last_query_time = datetime.now()

        self._cleanup_old_contexts()

    def _push_context(self) -> None:
        """Push current context to stack and create new one."""
        if len(self.state.context_stack) >= self.state.max_stack_size:
            self.state.context_stack.pop(0)
        self.state.context_stack.append(self.state.current_context)
        self.state.current_context = QueryContext()

    def pop_context(self) -> Optional[QueryContext]:
        """Pop and return the previous context."""
        if self.state.context_stack:
            self.state.current_context = self.state.context_stack.pop()
            return self.state.current_context
        return None

    def _cleanup_old_contexts(self) -> None:
        """Remove expired contexts."""
        current_time = datetime.now()
        timeout = self.state.context_timeout

        # Clean context stack
        self.state.context_stack = [
            ctx for ctx in self.state.context_stack
            if (current_time - ctx.last_query_time) <= timeout
        ]

        # Reset current context if expired
        if ((current_time - self.state.current_context.last_query_time) 
                > timeout):
            self.state.current_context = QueryContext()

    def _extract_focus(self, sql_query: str) -> Optional[str]:
        """Extract the main table focus from SQL query."""
        sql_lower = sql_query.lower()
        
        # Extract table from FROM clause
        from_idx = sql_lower.find("from")
        if from_idx == -1:
            return None

        # Find the end of the FROM clause
        where_idx = sql_lower.find("where", from_idx)
        join_idx = sql_lower.find("join", from_idx)
        group_idx = sql_lower.find("group by", from_idx)
        
        # Find the earliest clause after FROM
        end_indices = [i for i in [where_idx, join_idx, group_idx] if i != -1]
        end_idx = min(end_indices) if end_indices else len(sql_lower)
        
        # Extract and clean table name
        table_part = sql_query[from_idx + 4:end_idx].strip()
        return table_part.split()[0]  # Take first word after FROM

    def _extract_columns(self, sql_query: str) -> Set[str]:
        """Extract columns from SQL query."""
        sql_lower = sql_query.lower()
        
        # Extract columns from SELECT clause
        select_idx = sql_lower.find("select")
        from_idx = sql_lower.find("from")
        
        if select_idx == -1 or from_idx == -1:
            return set()

        columns_part = sql_query[select_idx + 6:from_idx].strip()
        
        # Handle * case
        if columns_part == "*":
            return set()

        # Split and clean column names
        columns = set()
        for col in columns_part.split(","):
            col = col.strip()
            # Handle aliased columns
            if " as " in col.lower():
                col = col.split(" as ")[0].strip()
            # Handle table qualified columns
            if "." in col:
                col = col.split(".")[1].strip()
            columns.add(col)

        return columns

    def _extract_filters(self, sql_query: str) -> Dict[str, str]:
        """Extract filters from SQL query."""
        sql_lower = sql_query.lower()
        
        # Extract WHERE clause
        where_idx = sql_lower.find("where")
        if where_idx == -1:
            return {}

        # Find the end of the WHERE clause
        group_idx = sql_lower.find("group by", where_idx)
        having_idx = sql_lower.find("having", where_idx)
        order_idx = sql_lower.find("order by", where_idx)
        
        # Find the earliest clause after WHERE
        end_indices = [i for i in [group_idx, having_idx, order_idx] if i != -1]
        end_idx = min(end_indices) if end_indices else len(sql_lower)
        
        where_clause = sql_query[where_idx + 5:end_idx].strip()
        
        # Parse conditions
        filters = {}
        conditions = where_clause.split("and")
        for condition in conditions:
            condition = condition.strip()
            # Handle basic equality conditions
            if "=" in condition:
                col, val = condition.split("=")
                filters[col.strip()] = val.strip()
            # Could add more condition types here

        return filters

    def _extract_temporal_context(self, sql_query: str) -> Optional[str]:
        """Extract temporal context from SQL query."""
        sql_lower = sql_query.lower()
        
        temporal_keywords = [
            "current_date",
            "current_timestamp",
            "interval",
            "date",
            "timestamp"
        ]
        
        for keyword in temporal_keywords:
            if keyword in sql_lower:
                return keyword

        return None

    def enhance_query(self, query_text: str) -> str:
        """Enhance query text with context information."""
        enhanced = query_text

        # Add table context if missing
        if (self.state.current_context.focus_table and 
            self.state.current_context.focus_table.lower() not in query_text.lower()):
            enhanced += f" from {self.state.current_context.focus_table}"

        # Add active filters if relevant
        if self.state.current_context.active_filters:
            filter_text = " and ".join(
                f"{col} = {val}" 
                for col, val in self.state.current_context.active_filters.items()
            )
            if "where" not in enhanced.lower():
                enhanced += f" where {filter_text}"

        # Add temporal context if relevant
        if self.state.current_context.temporal_context:
            if "date" in enhanced.lower():
                enhanced = enhanced.replace(
                    "date", 
                    self.state.current_context.temporal_context
                )

        return enhanced

    def save_state(self, filepath: str) -> None:
        """Save context state to a file."""
        data = {
            "previous_queries": self.state.previous_queries,
            "current_context": vars(self.state.current_context),
            "context_stack": [vars(ctx) for ctx in self.state.context_stack],
            "max_stack_size": self.state.max_stack_size,
            "context_timeout": str(self.state.context_timeout)
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def load_state(self, filepath: str) -> None:
        """Load context state from a file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.state.previous_queries = data["previous_queries"]
        self.state.current_context = QueryContext(**data["current_context"])
        self.state.context_stack = [
            QueryContext(**ctx) for ctx in data["context_stack"]
        ]
        self.state.max_stack_size = data["max_stack_size"]
        self.state.context_timeout = timedelta(
            seconds=int(data["context_timeout"].split()[0])
        )
