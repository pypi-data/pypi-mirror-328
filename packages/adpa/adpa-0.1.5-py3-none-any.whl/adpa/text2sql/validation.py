"""SQL validation and security checks."""

import re
from typing import List, Optional, Set, Tuple

from adpa.text2sql.models import Schema, Table
from adpa.text2sql.types import ValidationError


class SQLValidator:
    """SQL query validator and sanitizer."""

    def __init__(self) -> None:
        """Initialize validator with default rules."""
        self._dangerous_patterns = [
            r";\s*DROP\s+",
            r";\s*DELETE\s+",
            r";\s*UPDATE\s+",
            r";\s*INSERT\s+",
            r";\s*ALTER\s+",
            r";\s*CREATE\s+",
            r";\s*TRUNCATE\s+",
            r"--",
            r"/\*.*?\*/",
        ]
        self._compiled_patterns = [
            re.compile(pattern, re.I) for pattern in self._dangerous_patterns
        ]

    def validate_query(self, query: str) -> List[ValidationError]:
        """Validate a SQL query for security issues.
        
        Args:
            query: SQL query string
            
        Returns:
            List of validation errors
        """
        errors = []
        
        # Check for SQL injection patterns
        for pattern in self._compiled_patterns:
            if pattern.search(query):
                errors.append(ValidationError(
                    path="query",
                    message="Potentially dangerous SQL pattern detected",
                    severity="error",
                    suggestion="Remove semicolons and dangerous keywords"
                ))

        # Check for proper quoting
        if not self._check_quotes(query):
            errors.append(ValidationError(
                path="query",
                message="Mismatched quotes in query",
                severity="error",
                suggestion="Ensure all quotes are properly matched"
            ))

        # Check for common syntax errors
        syntax_errors = self._check_syntax(query)
        errors.extend(syntax_errors)

        return errors

    def validate_schema_compatibility(
        self, query: str, schema: Schema
    ) -> List[ValidationError]:
        """Validate query compatibility with schema.
        
        Args:
            query: SQL query string
            schema: Database schema
            
        Returns:
            List of validation errors
        """
        errors = []
        
        # Extract table and column references
        tables, columns = self._extract_references(query)
        
        # Validate table references
        for table in tables:
            if table not in schema.tables:
                errors.append(ValidationError(
                    path=f"query.tables.{table}",
                    message=f"Referenced table '{table}' not found in schema",
                    severity="error",
                    suggestion=f"Available tables: {list(schema.tables.keys())}"
                ))
                continue
            
            # Validate column references for this table
            table_schema = schema.tables[table]
            table_columns = {col.name for col in table_schema.columns}
            
            for col in columns.get(table, []):
                if col != "*" and col not in table_columns:
                    errors.append(ValidationError(
                        path=f"query.columns.{table}.{col}",
                        message=f"Column '{col}' not found in table '{table}'",
                        severity="error",
                        suggestion=f"Available columns: {list(table_columns)}"
                    ))

        return errors

    def sanitize_query(self, query: str) -> str:
        """Sanitize a SQL query by removing dangerous patterns.
        
        Args:
            query: SQL query string
            
        Returns:
            Sanitized query string
        """
        sanitized = query
        
        # Remove comments
        sanitized = re.sub(r"--.*$", "", sanitized, flags=re.M)
        sanitized = re.sub(r"/\*.*?\*/", "", sanitized, flags=re.S)
        
        # Remove multiple semicolons
        sanitized = re.sub(r";+", ";", sanitized)
        
        # Remove trailing semicolon
        sanitized = sanitized.rstrip(";")
        
        # Normalize whitespace
        sanitized = " ".join(sanitized.split())
        
        return sanitized

    def _check_quotes(self, query: str) -> bool:
        """Check for properly matched quotes.
        
        Args:
            query: SQL query string
            
        Returns:
            True if quotes are properly matched, False otherwise
        """
        stack = []
        in_string = False
        string_char = None
        
        for char in query:
            if char in ["'", "\""]:
                if not in_string:
                    in_string = True
                    string_char = char
                    stack.append(char)
                elif char == string_char:
                    if stack:
                        stack.pop()
                        in_string = False
                        string_char = None
        
        return len(stack) == 0

    def _check_syntax(self, query: str) -> List[ValidationError]:
        """Check for common SQL syntax errors.
        
        Args:
            query: SQL query string
            
        Returns:
            List of validation errors
        """
        errors = []
        
        # Check for missing FROM clause in SELECT
        if re.match(r"\s*SELECT", query, re.I) and "FROM" not in query.upper():
            errors.append(ValidationError(
                path="query.syntax",
                message="SELECT query missing FROM clause",
                severity="error",
                suggestion="Add FROM clause after SELECT"
            ))

        # Check for invalid JOIN syntax
        if "JOIN" in query.upper() and "ON" not in query.upper():
            errors.append(ValidationError(
                path="query.syntax",
                message="JOIN missing ON clause",
                severity="error",
                suggestion="Add ON clause to specify join condition"
            ))

        return errors

    def _extract_references(
        self, query: str
    ) -> Tuple[Set[str], Dict[str, Set[str]]]:
        """Extract table and column references from query.
        
        Args:
            query: SQL query string
            
        Returns:
            Tuple of (tables, columns) where tables is a set of table names
            and columns is a dict mapping table names to sets of column names
        """
        tables = set()
        columns = {}
        
        # Extract FROM and JOIN tables
        from_pattern = r"FROM\s+([a-zA-Z_][a-zA-Z0-9_]*)"
        join_pattern = r"JOIN\s+([a-zA-Z_][a-zA-Z0-9_]*)"
        
        for match in re.finditer(from_pattern, query, re.I):
            tables.add(match.group(1))
        
        for match in re.finditer(join_pattern, query, re.I):
            tables.add(match.group(1))
        
        # Extract columns
        for table in tables:
            columns[table] = set()
            col_pattern = rf"{table}\.([a-zA-Z_][a-zA-Z0-9_]*)"
            
            for match in re.finditer(col_pattern, query, re.I):
                columns[table].add(match.group(1))
        
        return tables, columns
