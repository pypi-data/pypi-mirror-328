"""Context management for SQL generation."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

from adpa.text2sql.models import Schema, Table


@dataclass
class QueryContext:
    """Context for SQL query generation."""
    schema: Schema
    tables: Set[str] = field(default_factory=set)
    columns: Dict[str, List[str]] = field(default_factory=dict)
    conditions: List[str] = field(default_factory=list)
    joins: List[str] = field(default_factory=list)
    parameters: Dict[str, str] = field(default_factory=dict)
    aliases: Dict[str, str] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

    def add_table(self, table: str) -> None:
        """Add a table to the context.
        
        Args:
            table: Name of the table to add
        """
        self.tables.add(table)

    def add_column(self, table: str, column: str) -> None:
        """Add a column to the context.
        
        Args:
            table: Table the column belongs to
            column: Name of the column
        """
        if table not in self.columns:
            self.columns[table] = []
        self.columns[table].append(column)

    def add_condition(self, condition: str) -> None:
        """Add a WHERE condition.
        
        Args:
            condition: SQL condition string
        """
        self.conditions.append(condition)

    def add_join(self, join: str) -> None:
        """Add a JOIN clause.
        
        Args:
            join: SQL join string
        """
        self.joins.append(join)

    def add_parameter(self, name: str, value: str) -> None:
        """Add a query parameter.
        
        Args:
            name: Parameter name
            value: Parameter value
        """
        self.parameters[name] = value

    def add_alias(self, table: str, alias: str) -> None:
        """Add a table alias.
        
        Args:
            table: Original table name
            alias: Table alias
        """
        self.aliases[table] = alias

    def get_table(self, name: str) -> Optional[Table]:
        """Get table schema by name.
        
        Args:
            name: Table name
            
        Returns:
            Table schema if found, None otherwise
        """
        return self.schema.tables.get(name)

    def get_alias(self, table: str) -> str:
        """Get table alias or original name.
        
        Args:
            table: Table name
            
        Returns:
            Table alias if exists, original name otherwise
        """
        return self.aliases.get(table, table)

    def clear(self) -> None:
        """Clear all context data except schema."""
        self.tables.clear()
        self.columns.clear()
        self.conditions.clear()
        self.joins.clear()
        self.parameters.clear()
        self.aliases.clear()
        self.metadata.clear()
