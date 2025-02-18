"""Main Text-to-SQL conversion engine with learning capabilities."""
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime
import json

from .schema_learner import SchemaLearner
from .query_history import QueryHistory
from .context_manager import ContextManager

class TextToSQLEngine:
    def __init__(self, connection_params: Dict[str, str]):
        """Initialize the Text-to-SQL engine."""
        self.schema_learner = SchemaLearner(connection_params)
        self.query_history = QueryHistory()
        self.context_manager = ContextManager()
        self.logger = logging.getLogger(__name__)
        
        # Load initial schema
        self.schema_learner.learn_schema()

    def convert_to_sql(self, text_input: str) -> Tuple[str, Dict[str, str]]:
        """Convert natural language to SQL with learning capabilities."""
        try:
            # 1. Analyze input and extract intent
            intent = self._analyze_intent(text_input)
            
            # 2. Consider conversation context
            enhanced_query = self.context_manager.enhance_query(text_input)
            
            # 3. Generate SQL
            sql = self._generate_sql(enhanced_query, intent)
            
            # 4. Validate and optimize
            final_sql = self._optimize_sql(sql)
            
            # 5. Update context
            self.context_manager.update_context(
                text_input, final_sql, 
                {"generated_at": datetime.now().isoformat()}
            )
            
            # 6. Learn from success
            self.schema_learner.learn_from_query(text_input, final_sql, True)
            
            return final_sql, {"success": True}
            
        except Exception as e:
            self.logger.error(f"Error converting to SQL: {str(e)}")
            
            # Learn from failure
            self.schema_learner.learn_from_query(text_input, "", False)
            
            # Try to suggest corrections
            suggestion = self._suggest_correction(text_input, str(e))
            
            return "", {
                "success": False,
                "error": str(e),
                "suggestion": suggestion
            }

    def _analyze_intent(self, text_input: str) -> Dict[str, str]:
        """Analyze the input text to determine query intent."""
        intent = {
            "action": self._extract_action(text_input),
            "entities": self._extract_entities(text_input),
            "conditions": self._extract_conditions(text_input),
            "aggregations": self._extract_aggregations(text_input),
            "order": self._extract_order(text_input),
            "limit": self._extract_limit(text_input)
        }
        
        self.logger.debug(f"Extracted intent: {intent}")
        return intent

    def _extract_action(self, text: str) -> str:
        """Extract the main action from the text."""
        text_lower = text.lower()
        
        # Define action keywords
        select_keywords = ["show", "find", "get", "list", "display", "what"]
        count_keywords = ["count", "how many", "total"]
        update_keywords = ["update", "change", "modify", "set"]
        delete_keywords = ["delete", "remove", "eliminate"]
        insert_keywords = ["add", "insert", "create", "new"]
        
        # Check for each type of action
        for word in text_lower.split():
            if word in select_keywords:
                return "SELECT"
            elif word in count_keywords:
                return "COUNT"
            elif word in update_keywords:
                return "UPDATE"
            elif word in delete_keywords:
                return "DELETE"
            elif word in insert_keywords:
                return "INSERT"
        
        # Default to SELECT if no action found
        return "SELECT"

    def _extract_entities(self, text: str) -> List[str]:
        """Extract entity names from the text."""
        entities = []
        
        # Get all known table names
        table_names = [
            table.name.lower() 
            for table in self.schema_learner.tables.values()
        ]
        
        # Look for table names in text
        words = text.lower().split()
        for word in words:
            if word in table_names:
                entities.append(word)
            # Could add fuzzy matching here
        
        return entities

    def _extract_conditions(self, text: str) -> List[Dict[str, str]]:
        """Extract conditions from the text."""
        conditions = []
        text_lower = text.lower()
        
        # Define condition keywords
        operators = {
            "equals": "=",
            "equal to": "=",
            "greater than": ">",
            "less than": "<",
            "at least": ">=",
            "at most": "<=",
            "not": "!=",
            "like": "LIKE"
        }
        
        # Look for condition patterns
        for op_text, op_symbol in operators.items():
            if op_text in text_lower:
                # Find the column and value
                parts = text_lower.split(op_text)
                if len(parts) >= 2:
                    conditions.append({
                        "column": parts[0].strip().split()[-1],
                        "operator": op_symbol,
                        "value": parts[1].strip().split()[0]
                    })
        
        return conditions

    def _extract_aggregations(self, text: str) -> List[Dict[str, str]]:
        """Extract aggregation operations from the text."""
        aggregations = []
        text_lower = text.lower()
        
        # Define aggregation keywords
        aggs = {
            "average": "AVG",
            "mean": "AVG",
            "sum": "SUM",
            "total": "SUM",
            "maximum": "MAX",
            "highest": "MAX",
            "minimum": "MIN",
            "lowest": "MIN",
            "count": "COUNT"
        }
        
        # Look for aggregation patterns
        for agg_text, agg_func in aggs.items():
            if agg_text in text_lower:
                # Find what we're aggregating
                words = text_lower.split()
                idx = words.index(agg_text)
                if idx + 1 < len(words):
                    aggregations.append({
                        "function": agg_func,
                        "column": words[idx + 1]
                    })
        
        return aggregations

    def _extract_order(self, text: str) -> Optional[Dict[str, str]]:
        """Extract ordering information from the text."""
        text_lower = text.lower()
        
        # Define ordering keywords
        order_keywords = {
            "ascending": "ASC",
            "descending": "DESC",
            "increasing": "ASC",
            "decreasing": "DESC"
        }
        
        # Look for ordering patterns
        for keyword, direction in order_keywords.items():
            if keyword in text_lower:
                # Find what we're ordering by
                words = text_lower.split()
                idx = words.index(keyword)
                if idx - 1 >= 0:
                    return {
                        "column": words[idx - 1],
                        "direction": direction
                    }
        
        return None

    def _extract_limit(self, text: str) -> Optional[int]:
        """Extract limit information from the text."""
        text_lower = text.lower()
        words = text_lower.split()
        
        # Look for limit patterns
        limit_keywords = ["first", "top", "limit"]
        
        for keyword in limit_keywords:
            if keyword in words:
                idx = words.index(keyword)
                if idx + 1 < len(words):
                    try:
                        return int(words[idx + 1])
                    except ValueError:
                        pass
        
        return None

    def _generate_sql(self, text: str, intent: Dict[str, str]) -> str:
        """Generate SQL from analyzed intent."""
        # Start building the query
        query_parts = []
        
        # Handle different actions
        action = intent["action"]
        if action == "SELECT":
            query_parts.append("SELECT")
            
            # Handle aggregations
            if intent["aggregations"]:
                aggs = [
                    f"{agg['function']}({agg['column']})"
                    for agg in intent["aggregations"]
                ]
                query_parts.append(", ".join(aggs))
            else:
                query_parts.append("*")
            
            # Add FROM clause
            if intent["entities"]:
                query_parts.append(f"FROM {intent['entities'][0]}")
            else:
                # Use context to determine table
                context_table = self.context_manager.state.current_context.focus_table
                if context_table:
                    query_parts.append(f"FROM {context_table}")
                else:
                    raise ValueError("No table specified and no context available")
            
            # Add WHERE clause
            if intent["conditions"]:
                conditions = [
                    f"{cond['column']} {cond['operator']} {cond['value']}"
                    for cond in intent["conditions"]
                ]
                query_parts.append("WHERE " + " AND ".join(conditions))
            
            # Add ORDER BY
            if intent["order"]:
                order = intent["order"]
                query_parts.append(
                    f"ORDER BY {order['column']} {order['direction']}"
                )
            
            # Add LIMIT
            if intent["limit"]:
                query_parts.append(f"LIMIT {intent['limit']}")
                
        elif action == "COUNT":
            query_parts.append("SELECT COUNT(*)")
            # Similar logic for FROM, WHERE, etc.
            
        # Join all parts
        sql = " ".join(query_parts)
        
        self.logger.debug(f"Generated SQL: {sql}")
        return sql

    def _optimize_sql(self, sql: str) -> str:
        """Optimize the generated SQL query."""
        # TODO: Implement query optimization
        return sql

    def _suggest_correction(self, text_input: str, 
                          error_message: str) -> Optional[str]:
        """Suggest corrections for failed queries."""
        # Look for similar successful queries
        similar_queries = self.query_history.get_similar_queries(text_input)
        
        if similar_queries:
            return (
                f"Try rephrasing like: '{similar_queries[0].text_input}'"
            )
        
        # Analyze error message for common patterns
        if "column not found" in error_message.lower():
            return "Try specifying the column name more clearly"
        elif "table not found" in error_message.lower():
            return "Try specifying the table name more clearly"
        
        return None

    def feedback(self, text_input: str, sql_query: str, 
                was_correct: bool, correction: Optional[str] = None) -> None:
        """Process feedback about query correctness."""
        if was_correct:
            self.query_history.add_query(
                text_input=text_input,
                sql_query=sql_query,
                execution_time=0.0,  # Would need actual execution time
                rows_affected=None  # Would need actual rows affected
            )
        else:
            self.query_history.add_query(
                text_input=text_input,
                sql_query=sql_query,
                execution_time=0.0,
                error_message="Incorrect query"
            )
            
            if correction:
                self.query_history.add_correction(
                    original_text=text_input,
                    original_sql=sql_query,
                    corrected_sql=correction,
                    correction_type="user_correction"
                )

    def save_state(self, directory: str) -> None:
        """Save complete engine state."""
        self.schema_learner.save_learned_data(f"{directory}/schema.json")
        self.query_history.save_history(f"{directory}/history.json")
        self.context_manager.save_state(f"{directory}/context.json")

    def load_state(self, directory: str) -> None:
        """Load complete engine state."""
        self.schema_learner.load_learned_data(f"{directory}/schema.json")
        self.query_history.load_history(f"{directory}/history.json")
        self.context_manager.load_state(f"{directory}/context.json")
