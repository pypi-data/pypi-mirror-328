"""SQL generation functionality."""

import re
from typing import Dict, List, Optional, Set, Tuple

from adpa.text2sql.types import (ColumnSchema, GeneratorConfig, IndexSchema,
                                QueryResult, SchemaConfig, SQLDialect,
                                ValidationError)


class SQLGenerator:
    """Generates SQL queries from natural language text."""

    def __init__(self, config: Optional[GeneratorConfig] = None) -> None:
        """Initialize the SQL generator.

        Args:
            config: Generator configuration. If None, uses default settings.
        """
        self.config = config or GeneratorConfig()
        self._query_templates: Dict[str, str] = self._load_templates()
        self._common_patterns: Dict[str, re.Pattern] = self._compile_patterns()

    def _load_templates(self) -> Dict[str, str]:
        """Load query templates for common operations."""
        return {
            "select": "SELECT {columns} FROM {tables}{joins}{where}{group}{having}{order}{limit}",
            "insert": "INSERT INTO {table} ({columns}) VALUES {values}",
            "update": "UPDATE {table} SET {sets}{where}",
            "delete": "DELETE FROM {table}{where}",
            "create_table": """
                CREATE TABLE {table} (
                    {columns},
                    {constraints}
                )""",
            "create_index": "CREATE {unique} INDEX {name} ON {table} ({columns}){where}",
            "join": "{type} JOIN {table} ON {condition}"
        }

    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        """Compile regex patterns for query analysis."""
        return {
            "select": re.compile(r"\b(select|find|get|show|display)\b", re.I),
            "insert": re.compile(r"\b(insert|add|create|put)\b", re.I),
            "update": re.compile(r"\b(update|modify|change|set)\b", re.I),
            "delete": re.compile(r"\b(delete|remove|drop)\b", re.I),
            "where": re.compile(r"\b(where|with|having)\b", re.I),
            "join": re.compile(r"\b(join|combine|merge)\b", re.I),
            "group": re.compile(r"\b(group|aggregate|summarize)\b", re.I),
            "order": re.compile(r"\b(order|sort)\b", re.I),
            "limit": re.compile(r"\b(limit|top|first)\b", re.I)
        }

    async def generate_query(self, text: str, schema: SchemaConfig) -> QueryResult:
        """Generate a SQL query from natural language text.

        Args:
            text: Natural language query text
            schema: Database schema configuration

        Returns:
            QueryResult containing the generated query and metadata

        Raises:
            ValueError: If the input text or schema is invalid
        """
        # Validate inputs
        if not text.strip():
            raise ValueError("Query text cannot be empty")
        
        if not schema.tables:
            raise ValueError("Schema must contain at least one table")

        # Analyze query intent
        operation_type = self._determine_operation(text)
        if operation_type == "delete" and self.config.safe_mode:
            raise ValueError("Delete operations are not allowed in safe mode")

        # Extract relevant information
        tables = self._identify_tables(text, schema)
        columns = self._identify_columns(text, schema, tables)
        conditions = self._extract_conditions(text, schema, tables)
        joins = self._determine_joins(tables, schema)

        # Generate the query
        query = self._build_query(
            operation_type,
            tables,
            columns,
            conditions,
            joins,
            schema.dialect
        )

        # Analyze the query
        complexity = self._estimate_complexity(query, schema)
        suggested_indexes = self._suggest_indexes(query, schema)
        warnings = self._analyze_performance(query, schema)

        return QueryResult(
            query=query,
            confidence=self._calculate_confidence(text, query),
            explanation=self._generate_explanation(query),
            warnings=warnings,
            suggested_indexes=suggested_indexes,
            estimated_complexity=complexity,
            tables_used=list(tables)
        )

    def _determine_operation(self, text: str) -> str:
        """Determine the type of SQL operation from the text."""
        for op_type, pattern in self._common_patterns.items():
            if pattern.search(text):
                return op_type
        return "select"  # Default to SELECT

    def _identify_tables(self, text: str, schema: SchemaConfig) -> Set[str]:
        """Identify referenced tables from the text."""
        tables = set()
        for table_name in schema.tables:
            if re.search(rf"\b{table_name}\b", text, re.I):
                tables.add(table_name)
        return tables

    def _identify_columns(
        self, text: str, schema: SchemaConfig, tables: Set[str]
    ) -> List[str]:
        """Identify referenced columns from the text."""
        columns = []
        for table in tables:
            table_schema = schema.tables[table]
            for col in table_schema.columns:
                if re.search(rf"\b{col.name}\b", text, re.I):
                    columns.append(f"{table}.{col.name}")
        return columns or ["*"]

    def _extract_conditions(
        self, text: str, schema: SchemaConfig, tables: Set[str]
    ) -> List[str]:
        """Extract WHERE conditions from the text."""
        conditions = []
        # Implementation would use NLP to extract conditions
        return conditions

    def _determine_joins(
        self, tables: Set[str], schema: SchemaConfig
    ) -> List[Tuple[str, str, str]]:
        """Determine necessary joins between tables."""
        joins = []
        processed = set()

        for table in tables:
            processed.add(table)
            table_schema = schema.tables[table]
            
            for col in table_schema.columns:
                if col.foreign_key and col.foreign_key.split(".")[0] in tables:
                    target_table, target_col = col.foreign_key.split(".")
                    if target_table not in processed:
                        joins.append((
                            "INNER",
                            target_table,
                            f"{table}.{col.name} = {target_table}.{target_col}"
                        ))

        return joins

    def _build_query(
        self,
        operation: str,
        tables: Set[str],
        columns: List[str],
        conditions: List[str],
        joins: List[Tuple[str, str, str]],
        dialect: SQLDialect
    ) -> str:
        """Build the SQL query string."""
        template = self._query_templates[operation]
        
        # Format components based on dialect
        if dialect == SQLDialect.POSTGRESQL:
            # PostgreSQL-specific formatting
            pass
        elif dialect == SQLDialect.MYSQL:
            # MySQL-specific formatting
            pass

        # Build the query using the template
        query_parts = {
            "columns": ", ".join(columns),
            "tables": ", ".join(tables),
            "joins": " ".join(
                self._query_templates["join"].format(
                    type=j[0], table=j[1], condition=j[2]
                ) for j in joins
            ),
            "where": f" WHERE {' AND '.join(conditions)}" if conditions else "",
            "group": "",  # Implement group by
            "having": "",  # Implement having
            "order": "",   # Implement order by
            "limit": ""    # Implement limit
        }

        return template.format(**query_parts).strip()

    def _estimate_complexity(self, query: str, schema: SchemaConfig) -> str:
        """Estimate the computational complexity of the query."""
        # Simple estimation based on operations
        if "DISTINCT" in query.upper():
            return "O(n log n)"
        elif "JOIN" in query.upper():
            return "O(n * m)"
        else:
            return "O(n)"

    def _suggest_indexes(
        self, query: str, schema: SchemaConfig
    ) -> List[IndexSchema]:
        """Suggest indexes that could improve query performance."""
        suggestions = []
        # Implementation would analyze query patterns and suggest appropriate indexes
        return suggestions

    def _analyze_performance(
        self, query: str, schema: SchemaConfig
    ) -> List[str]:
        """Analyze potential performance issues in the query."""
        warnings = []
        
        # Check for full table scans
        if " * " in query and "WHERE" not in query:
            warnings.append("Query performs a full table scan")

        # Check for cartesian products
        if query.upper().count("JOIN") > len(query.upper().split("ON")) - 1:
            warnings.append("Query may produce a cartesian product")

        return warnings

    def _calculate_confidence(self, text: str, query: str) -> float:
        """Calculate confidence score for the generated query."""
        # Implementation would use heuristics to estimate confidence
        return 0.85

    def _generate_explanation(self, query: str) -> str:
        """Generate a natural language explanation of the query."""
        # Implementation would explain the query's operation
        return f"This query {query.split()[0].lower()}s data from the database"

    def validate_schema(self, schema: Dict) -> List[ValidationError]:
        """Validate a database schema.

        Args:
            schema: Schema definition to validate

        Returns:
            List of validation errors
        """
        errors = []
        
        # Validate schema structure
        if not isinstance(schema, dict):
            errors.append(ValidationError(
                path="$",
                message="Schema must be a dictionary",
                severity="error"
            ))
            return errors

        # Validate tables
        for table_name, table in schema.items():
            table_path = f"$.{table_name}"
            
            # Check table name
            if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table_name):
                errors.append(ValidationError(
                    path=table_path,
                    message="Invalid table name",
                    severity="error",
                    suggestion="Use letters, numbers, and underscores only"
                ))

            # Validate columns
            if "columns" not in table:
                errors.append(ValidationError(
                    path=f"{table_path}.columns",
                    message="Table must have columns defined",
                    severity="error"
                ))
                continue

            # Check for primary key
            has_primary_key = any(
                col.primary_key for col in table.columns
            )
            if not has_primary_key:
                errors.append(ValidationError(
                    path=f"{table_path}.columns",
                    message="Table should have a primary key",
                    severity="warning",
                    suggestion="Add a primary key column"
                ))

        return errors
