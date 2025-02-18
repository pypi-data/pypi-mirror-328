"""Query history tracking component that learns from past queries."""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
import logging

@dataclass
class QueryResult:
    text_input: str
    sql_query: str
    execution_time: float
    timestamp: datetime = field(default_factory=datetime.now)
    error_message: Optional[str] = None
    rows_affected: Optional[int] = None
    was_successful: bool = True

@dataclass
class QueryCorrection:
    original_text: str
    original_sql: str
    corrected_sql: str
    correction_type: str
    timestamp: datetime = field(default_factory=datetime.now)
    notes: Optional[str] = None

class QueryHistory:
    def __init__(self):
        """Initialize query history tracker."""
        self.successful_queries: List[QueryResult] = []
        self.failed_queries: List[QueryResult] = []
        self.corrections: Dict[str, List[QueryCorrection]] = {}
        self.pattern_success_rates: Dict[str, Tuple[int, int]] = {}  # (successes, total)
        self.logger = logging.getLogger(__name__)

    def add_query(self, text_input: str, sql_query: str, 
                 execution_time: float, rows_affected: Optional[int] = None,
                 error_message: Optional[str] = None) -> None:
        """Add a query execution result to history."""
        result = QueryResult(
            text_input=text_input,
            sql_query=sql_query,
            execution_time=execution_time,
            rows_affected=rows_affected,
            error_message=error_message,
            was_successful=error_message is None
        )

        if result.was_successful:
            self.successful_queries.append(result)
            self._update_pattern_stats(text_input, True)
        else:
            self.failed_queries.append(result)
            self._update_pattern_stats(text_input, False)

        self._prune_history()

    def add_correction(self, original_text: str, original_sql: str, 
                      corrected_sql: str, correction_type: str,
                      notes: Optional[str] = None) -> None:
        """Add a correction for a failed query."""
        correction = QueryCorrection(
            original_text=original_text,
            original_sql=original_sql,
            corrected_sql=corrected_sql,
            correction_type=correction_type,
            notes=notes
        )

        if original_text not in self.corrections:
            self.corrections[original_text] = []
        self.corrections[original_text].append(correction)

        # Learn from the correction
        self._learn_from_correction(correction)

    def _learn_from_correction(self, correction: QueryCorrection) -> None:
        """Learn patterns from corrections."""
        # Extract the type of correction made
        if correction.correction_type == "syntax":
            self._learn_syntax_correction(correction)
        elif correction.correction_type == "semantic":
            self._learn_semantic_correction(correction)
        elif correction.correction_type == "structure":
            self._learn_structure_correction(correction)

    def _learn_syntax_correction(self, correction: QueryCorrection) -> None:
        """Learn from syntax corrections."""
        # Compare original and corrected SQL to identify syntax patterns
        original_tokens = correction.original_sql.split()
        corrected_tokens = correction.corrected_sql.split()
        
        # Find differences and store the correction pattern
        differences = self._find_token_differences(original_tokens, corrected_tokens)
        self.logger.info(f"Learned syntax correction pattern: {differences}")

    def _learn_semantic_correction(self, correction: QueryCorrection) -> None:
        """Learn from semantic corrections."""
        # Analyze semantic changes (e.g., wrong table joins, conditions)
        original_parts = self._parse_sql_parts(correction.original_sql)
        corrected_parts = self._parse_sql_parts(correction.corrected_sql)
        
        # Store semantic correction patterns
        self.logger.info(f"Learned semantic correction pattern: {original_parts} -> {corrected_parts}")

    def _learn_structure_correction(self, correction: QueryCorrection) -> None:
        """Learn from structural corrections."""
        # Analyze query structure changes
        original_structure = self._analyze_query_structure(correction.original_sql)
        corrected_structure = self._analyze_query_structure(correction.corrected_sql)
        
        # Store structure correction patterns
        self.logger.info(f"Learned structure correction: {original_structure} -> {corrected_structure}")

    def _find_token_differences(self, original: List[str], 
                              corrected: List[str]) -> Dict[str, str]:
        """Find differences between original and corrected tokens."""
        differences = {}
        for i, (orig, corr) in enumerate(zip(original, corrected)):
            if orig != corr:
                differences[f"pos_{i}"] = f"{orig} -> {corr}"
        return differences

    def _parse_sql_parts(self, sql: str) -> Dict[str, str]:
        """Parse SQL into its constituent parts."""
        parts = {
            "select": "",
            "from": "",
            "where": "",
            "group_by": "",
            "having": "",
            "order_by": ""
        }
        
        # Simple parsing - can be made more sophisticated
        sql_lower = sql.lower()
        
        if "select" in sql_lower:
            parts["select"] = self._extract_clause(sql_lower, "select", "from")
        if "from" in sql_lower:
            parts["from"] = self._extract_clause(sql_lower, "from", "where")
        if "where" in sql_lower:
            parts["where"] = self._extract_clause(sql_lower, "where", "group by")
        
        return parts

    def _extract_clause(self, sql: str, start_keyword: str, 
                       end_keyword: str) -> str:
        """Extract a SQL clause between keywords."""
        start_idx = sql.find(start_keyword) + len(start_keyword)
        end_idx = sql.find(end_keyword) if end_keyword in sql else len(sql)
        return sql[start_idx:end_idx].strip()

    def _analyze_query_structure(self, sql: str) -> Dict[str, bool]:
        """Analyze the structure of a SQL query."""
        sql_lower = sql.lower()
        return {
            "has_join": "join" in sql_lower,
            "has_subquery": "(" in sql and "select" in sql_lower,
            "has_aggregation": any(agg in sql_lower 
                                 for agg in ["count(", "sum(", "avg(", "max(", "min("]),
            "has_group_by": "group by" in sql_lower,
            "has_having": "having" in sql_lower,
            "has_order_by": "order by" in sql_lower
        }

    def _update_pattern_stats(self, text_input: str, success: bool) -> None:
        """Update success statistics for query patterns."""
        pattern = self._extract_pattern(text_input)
        if pattern not in self.pattern_success_rates:
            self.pattern_success_rates[pattern] = (0, 0)
        
        successes, total = self.pattern_success_rates[pattern]
        self.pattern_success_rates[pattern] = (
            successes + (1 if success else 0),
            total + 1
        )

    def _extract_pattern(self, text_input: str) -> str:
        """Extract a pattern from text input."""
        # TODO: Implement more sophisticated pattern extraction
        words = text_input.lower().split()
        return " ".join(word for word in words if len(word) > 3)

    def _prune_history(self, max_history: int = 1000) -> None:
        """Prune history to prevent excessive memory usage."""
        if len(self.successful_queries) > max_history:
            self.successful_queries = self.successful_queries[-max_history:]
        if len(self.failed_queries) > max_history:
            self.failed_queries = self.failed_queries[-max_history:]

    def get_similar_queries(self, text_input: str, 
                          limit: int = 5) -> List[QueryResult]:
        """Find similar successful queries."""
        pattern = self._extract_pattern(text_input)
        similar_queries = []
        
        for query in reversed(self.successful_queries):
            if self._pattern_similarity(pattern, 
                                     self._extract_pattern(query.text_input)) > 0.5:
                similar_queries.append(query)
                if len(similar_queries) >= limit:
                    break
        
        return similar_queries

    def _pattern_similarity(self, pattern1: str, pattern2: str) -> float:
        """Calculate similarity between two patterns."""
        # TODO: Implement more sophisticated similarity calculation
        words1 = set(pattern1.split())
        words2 = set(pattern2.split())
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        return len(intersection) / len(union) if union else 0.0

    def get_success_rate(self, pattern: str) -> float:
        """Get success rate for a pattern."""
        if pattern in self.pattern_success_rates:
            successes, total = self.pattern_success_rates[pattern]
            return successes / total if total > 0 else 0.0
        return 0.0

    def save_history(self, filepath: str) -> None:
        """Save query history to a file."""
        data = {
            "successful_queries": [vars(q) for q in self.successful_queries],
            "failed_queries": [vars(q) for q in self.failed_queries],
            "corrections": {
                k: [vars(c) for c in v] 
                for k, v in self.corrections.items()
            },
            "pattern_success_rates": self.pattern_success_rates
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def load_history(self, filepath: str) -> None:
        """Load query history from a file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Reconstruct objects from dict
        self.successful_queries = [
            QueryResult(**q) for q in data["successful_queries"]
        ]
        self.failed_queries = [
            QueryResult(**q) for q in data["failed_queries"]
        ]
        self.corrections = {
            k: [QueryCorrection(**c) for c in v]
            for k, v in data["corrections"].items()
        }
        self.pattern_success_rates = data["pattern_success_rates"]
