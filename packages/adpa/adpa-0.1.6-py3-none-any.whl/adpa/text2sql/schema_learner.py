"""
Schema learning utilities for Text2SQL module.
"""
from typing import Dict, List, Optional, Set, Tuple
import sqlalchemy as sa
from collections import defaultdict
import logging
from datetime import datetime

from adpa.text2sql.models import (
    Column, Table, Index, Schema,
    DatabaseConfig
)
from adpa.text2sql.types import SchemaConfig

logger = logging.getLogger(__name__)

class SchemaLearner:
    """Learn database schema from queries and usage patterns."""
    
    def __init__(
        self,
        config: SchemaConfig,
        min_confidence: float = 0.8,
        max_samples: int = 1000
    ):
        """Initialize schema learner.
        
        Args:
            config: Schema configuration
            min_confidence: Minimum confidence for schema suggestions
            max_samples: Maximum number of samples to store
        """
        self.config = config
        self.min_confidence = min_confidence
        self.max_samples = max_samples
        self.samples = []
        self.patterns = defaultdict(int)
        self.last_update = None
    
    def analyze_query(
        self,
        query: str,
        execution_time: float,
        row_count: int
    ) -> None:
        """Analyze a query for schema patterns.
        
        Args:
            query: SQL query to analyze
            execution_time: Query execution time in seconds
            row_count: Number of rows returned
        """
        # Extract patterns
        tables = self._extract_tables(query)
        joins = self._extract_joins(query)
        conditions = self._extract_conditions(query)
        
        # Store sample
        self.samples.append({
            "query": query,
            "tables": tables,
            "joins": joins,
            "conditions": conditions,
            "execution_time": execution_time,
            "row_count": row_count,
            "timestamp": datetime.now()
        })
        
        # Limit samples
        if len(self.samples) > self.max_samples:
            self.samples.pop(0)
        
        # Update patterns
        for table in tables:
            self.patterns[f"table:{table}"] += 1
        for join in joins:
            self.patterns[f"join:{join}"] += 1
        for condition in conditions:
            self.patterns[f"condition:{condition}"] += 1
        
        self.last_update = datetime.now()
    
    def suggest_indexes(self) -> List[Index]:
        """Suggest indexes based on query patterns.
        
        Returns:
            List of suggested indexes
        """
        suggestions = []
        
        # Analyze conditions
        condition_counts = defaultdict(int)
        for sample in self.samples:
            for condition in sample["conditions"]:
                if "=" in condition or ">" in condition or "<" in condition:
                    table, column = condition.split(".", 1)
                    condition_counts[f"{table}.{column}"] += 1
        
        # Get high-frequency columns
        total_samples = len(self.samples)
        if total_samples == 0:
            return suggestions
        
        for key, count in condition_counts.items():
            frequency = count / total_samples
            if frequency >= self.min_confidence:
                table, column = key.split(".")
                suggestions.append(
                    Index(
                        name=f"idx_{table}_{column}",
                        table=table,
                        columns=[column]
                    )
                )
        
        return suggestions
    
    def suggest_foreign_keys(self) -> List[Tuple[str, str]]:
        """Suggest foreign key relationships based on join patterns.
        
        Returns:
            List of (referencing_column, referenced_column) tuples
        """
        suggestions = []
        
        # Analyze joins
        join_counts = defaultdict(int)
        for sample in self.samples:
            for join in sample["joins"]:
                join_counts[join] += 1
        
        # Get high-frequency joins
        total_samples = len(self.samples)
        if total_samples == 0:
            return suggestions
        
        for join, count in join_counts.items():
            frequency = count / total_samples
            if frequency >= self.min_confidence:
                col1, col2 = join.split("=")
                suggestions.append((col1.strip(), col2.strip()))
        
        return suggestions
    
    def _extract_tables(self, query: str) -> Set[str]:
        """Extract table names from query.
        
        Args:
            query: SQL query
            
        Returns:
            Set of table names
        """
        tables = set()
        try:
            # Parse with SQLAlchemy
            stmt = sa.text(query)
            for token in stmt._compiler().statement.tokens:
                if token.ttype is sa.sql.tokens.Name and not token.is_keyword:
                    tables.add(token.value)
        except Exception as e:
            logger.warning(f"Error extracting tables: {e}")
        return tables
    
    def _extract_joins(self, query: str) -> Set[str]:
        """Extract join conditions from query.
        
        Args:
            query: SQL query
            
        Returns:
            Set of join conditions
        """
        joins = set()
        try:
            # Simple pattern matching for now
            query = query.lower()
            parts = query.split("join")
            for i in range(1, len(parts)):
                on_part = parts[i].split("on")
                if len(on_part) > 1:
                    condition = on_part[1].split("where")[0].split("group")[0].strip()
                    joins.add(condition)
        except Exception as e:
            logger.warning(f"Error extracting joins: {e}")
        return joins
    
    def _extract_conditions(self, query: str) -> Set[str]:
        """Extract WHERE conditions from query.
        
        Args:
            query: SQL query
            
        Returns:
            Set of conditions
        """
        conditions = set()
        try:
            # Simple pattern matching for now
            query = query.lower()
            where_parts = query.split("where")
            if len(where_parts) > 1:
                cond_part = where_parts[1].split("group")[0].split("order")[0]
                for cond in cond_part.split("and"):
                    conditions.add(cond.strip())
        except Exception as e:
            logger.warning(f"Error extracting conditions: {e}")
        return conditions
    
    def get_stats(self) -> Dict:
        """Get learner statistics.
        
        Returns:
            Dictionary with statistics
        """
        return {
            "num_samples": len(self.samples),
            "num_patterns": len(self.patterns),
            "last_update": self.last_update.isoformat() if self.last_update else None,
            "top_patterns": dict(
                sorted(
                    self.patterns.items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]
            )
        }
