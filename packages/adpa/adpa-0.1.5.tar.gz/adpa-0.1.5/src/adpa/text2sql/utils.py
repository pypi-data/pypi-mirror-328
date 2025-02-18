"""Utility functions for SQL generation."""

import re
from typing import Dict, List, Optional, Set, Tuple

from adpa.text2sql.models import Column, Index, Schema, Table


def extract_table_references(text: str) -> Set[str]:
    """Extract table references from natural language text.
    
    Args:
        text: Natural language query text
        
    Returns:
        Set of table names found in text
    """
    # Common patterns for table references
    patterns = [
        r"from\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"join\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"in\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"update\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"into\s+([a-zA-Z_][a-zA-Z0-9_]*)",
    ]
    
    tables = set()
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.I)
        for match in matches:
            tables.add(match.group(1))
    
    return tables


def extract_column_references(text: str) -> Set[str]:
    """Extract column references from natural language text.
    
    Args:
        text: Natural language query text
        
    Returns:
        Set of column names found in text
    """
    # Common patterns for column references
    patterns = [
        r"select\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"where\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"group\s+by\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        r"order\s+by\s+([a-zA-Z_][a-zA-Z0-9_]*)",
    ]
    
    columns = set()
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.I)
        for match in matches:
            columns.add(match.group(1))
    
    return columns


def suggest_joins(
    tables: Set[str], schema: Schema
) -> List[Tuple[str, str, str]]:
    """Suggest possible joins between tables.
    
    Args:
        tables: Set of table names
        schema: Database schema
        
    Returns:
        List of (table1, table2, join_condition) tuples
    """
    joins = []
    processed = set()
    
    for table in tables:
        processed.add(table)
        table_schema = schema.tables.get(table)
        if not table_schema:
            continue
        
        # Check foreign key relationships
        for col in table_schema.columns:
            if col.foreign_key and col.foreign_key.split(".")[0] in tables:
                target_table, target_col = col.foreign_key.split(".")
                if target_table not in processed:
                    joins.append((
                        table,
                        target_table,
                        f"{table}.{col.name} = {target_table}.{target_col}"
                    ))
    
    return joins


def suggest_indexes(
    query: str, schema: Schema
) -> List[Index]:
    """Suggest indexes that could improve query performance.
    
    Args:
        query: SQL query string
        schema: Database schema
        
    Returns:
        List of suggested indexes
    """
    suggestions = []
    
    # Extract conditions from WHERE clause
    where_pattern = r"WHERE\s+(.+?)(?:ORDER\s+BY|GROUP\s+BY|HAVING|LIMIT|$)"
    where_match = re.search(where_pattern, query, re.I | re.S)
    
    if where_match:
        conditions = where_match.group(1)
        
        # Extract column references from conditions
        col_pattern = r"([a-zA-Z_][a-zA-Z0-9_]*\.)?([a-zA-Z_][a-zA-Z0-9_]*)"
        for match in re.finditer(col_pattern, conditions):
            table = match.group(1)[:-1] if match.group(1) else None
            column = match.group(2)
            
            if table and table in schema.tables:
                # Suggest index for frequently filtered columns
                suggestions.append(Index(
                    name=f"idx_{table}_{column}",
                    table=table,
                    columns=[column],
                    description=f"Suggested index for filtering on {column}"
                ))
    
    return suggestions


def analyze_query_complexity(query: str) -> str:
    """Analyze the computational complexity of a query.
    
    Args:
        query: SQL query string
        
    Returns:
        String describing the query complexity
    """
    # Count joins
    join_count = len(re.findall(r"\bJOIN\b", query, re.I))
    
    # Check for expensive operations
    has_distinct = bool(re.search(r"\bDISTINCT\b", query, re.I))
    has_group_by = bool(re.search(r"\bGROUP\s+BY\b", query, re.I))
    has_order_by = bool(re.search(r"\bORDER\s+BY\b", query, re.I))
    
    if join_count > 0:
        if has_distinct or has_group_by:
            return "O(n * m * log(n))"  # Joins with sorting
        return "O(n * m)"  # Simple joins
    elif has_distinct or has_group_by or has_order_by:
        return "O(n * log(n))"  # Sorting operations
    else:
        return "O(n)"  # Simple scan


def generate_query_explanation(query: str) -> str:
    """Generate a natural language explanation of a query.
    
    Args:
        query: SQL query string
        
    Returns:
        Human-readable explanation of the query
    """
    parts = []
    
    # Determine operation type
    if re.match(r"\s*SELECT", query, re.I):
        parts.append("This query retrieves data")
    elif re.match(r"\s*INSERT", query, re.I):
        parts.append("This query inserts new data")
    elif re.match(r"\s*UPDATE", query, re.I):
        parts.append("This query updates existing data")
    elif re.match(r"\s*DELETE", query, re.I):
        parts.append("This query removes data")
    
    # Add details about tables
    from_match = re.search(r"FROM\s+([a-zA-Z_][a-zA-Z0-9_]*)", query, re.I)
    if from_match:
        parts.append(f"from the {from_match.group(1)} table")
    
    # Add join information
    join_count = len(re.findall(r"\bJOIN\b", query, re.I))
    if join_count > 0:
        parts.append(f"joining with {join_count} other table(s)")
    
    # Add filter information
    where_match = re.search(r"WHERE\s+(.+?)(?:ORDER|GROUP|HAVING|LIMIT|$)", query, re.I)
    if where_match:
        parts.append("with specific conditions")
    
    # Add sorting information
    if re.search(r"\bORDER\s+BY\b", query, re.I):
        parts.append("sorted by specified columns")
    
    return " ".join(parts)
