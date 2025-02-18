"""SQL validation layer for query verification."""
from typing import Dict, Any, List, Optional, Set
from pydantic import BaseModel, Field
import sqlparse
from sqlalchemy.engine import Engine
from sqlalchemy import text, exc


class ValidationError(Exception):
    """Base class for validation errors."""
    pass


class SecurityError(ValidationError):
    """Security-related validation errors."""
    pass


class SchemaError(ValidationError):
    """Schema-related validation errors."""
    pass


class PerformanceError(ValidationError):
    """Performance-related validation errors."""
    pass


class ValidationResult(BaseModel):
    """Result of validation checks."""
    valid: bool = Field(default=False, description="Overall validation status")
    errors: List[str] = Field(default_factory=list, description="Validation errors")
    warnings: List[str] = Field(
        default_factory=list,
        description="Validation warnings"
    )
    suggestions: List[str] = Field(
        default_factory=list,
        description="Improvement suggestions"
    )


class SecurityValidation(BaseModel):
    """Security validation configuration."""
    allowed_operations: Set[str] = Field(
        default={"SELECT"},
        description="Allowed SQL operations"
    )
    blocked_keywords: Set[str] = Field(
        default={
            "DROP", "DELETE", "TRUNCATE", "UPDATE", "INSERT",
            "GRANT", "REVOKE", "ALTER", "CREATE"
        },
        description="Blocked SQL keywords"
    )
    max_joins: int = Field(default=5, description="Maximum allowed joins")
    max_conditions: int = Field(default=10, description="Maximum WHERE conditions")
    max_unions: int = Field(default=2, description="Maximum UNION operations")
    max_subqueries: int = Field(default=3, description="Maximum subquery depth")


class SchemaValidation(BaseModel):
    """Schema validation configuration."""
    required_tables: Set[str] = Field(
        default_factory=set,
        description="Required tables"
    )
    required_columns: Dict[str, Set[str]] = Field(
        default_factory=dict,
        description="Required columns per table"
    )
    allowed_joins: List[str] = Field(
        default_factory=list,
        description="Allowed join conditions"
    )
    max_columns: int = Field(default=20, description="Maximum columns in SELECT")
    enforce_schema: bool = Field(
        default=True,
        description="Enforce schema validation"
    )


class PerformanceValidation(BaseModel):
    """Performance validation configuration."""
    max_rows: int = Field(default=1000, description="Maximum result rows")
    timeout_seconds: int = Field(default=30, description="Query timeout")
    min_index_usage: float = Field(
        default=0.5,
        description="Minimum index usage ratio"
    )
    max_table_scan: int = Field(
        default=2,
        description="Maximum full table scans"
    )
    max_memory_mb: int = Field(
        default=1024,
        description="Maximum memory usage in MB"
    )


class SQLValidator:
    """SQL query validator with comprehensive checks."""

    def __init__(
        self,
        engine: Engine,
        security_config: Optional[SecurityValidation] = None,
        schema_config: Optional[SchemaValidation] = None,
        performance_config: Optional[PerformanceValidation] = None
    ) -> None:
        """Initialize validator.

        Args:
            engine: SQLAlchemy engine
            security_config: Security validation config
            schema_config: Schema validation config
            performance_config: Performance validation config
        """
        self.engine = engine
        self.security_config = security_config or SecurityValidation()
        self.schema_config = schema_config or SchemaValidation()
        self.performance_config = performance_config or PerformanceValidation()

    def validate_query(self, sql: str) -> ValidationResult:
        """Validate SQL query comprehensively.

        Args:
            sql: SQL query to validate

        Returns:
            ValidationResult with status and messages
        """
        result = ValidationResult()

        try:
            # Parse query
            parsed = sqlparse.parse(sql)[0]

            # Security validation
            security_result = self._validate_security(parsed)
            result.errors.extend(security_result.errors)
            result.warnings.extend(security_result.warnings)

            # Schema validation
            schema_result = self._validate_schema(parsed)
            result.errors.extend(schema_result.errors)
            result.warnings.extend(schema_result.warnings)

            # Performance validation
            perf_result = self._validate_performance(parsed)
            result.errors.extend(perf_result.errors)
            result.warnings.extend(perf_result.warnings)

            # Set overall validity
            result.valid = not result.errors

            # Add suggestions
            result.suggestions = self._generate_suggestions(
                parsed,
                security_result,
                schema_result,
                perf_result
            )

        except Exception as e:
            result.errors.append(f"Validation error: {str(e)}")
            result.valid = False

        return result

    def _validate_security(self, parsed: Any) -> ValidationResult:
        """Validate query security.

        Args:
            parsed: Parsed SQL query

        Returns:
            ValidationResult for security checks
        """
        result = ValidationResult()

        # Check operation type
        operation = str(parsed.get_type()).upper()
        if operation not in self.security_config.allowed_operations:
            result.errors.append(
                f"Operation {operation} not allowed. Use SELECT only."
            )

        # Check for blocked keywords
        sql_str = str(parsed).upper()
        for keyword in self.security_config.blocked_keywords:
            if keyword in sql_str:
                result.errors.append(f"Blocked keyword found: {keyword}")

        # Count joins
        join_count = sql_str.count("JOIN")
        if join_count > self.security_config.max_joins:
            result.warnings.append(
                f"Query uses {join_count} joins (max {self.security_config.max_joins})"
            )

        # Count conditions
        where_clause = [
            token for token in parsed.tokens
            if isinstance(token, sqlparse.sql.Where)
        ]
        if where_clause:
            condition_count = str(where_clause[0]).count("AND") + \
                str(where_clause[0]).count("OR") + 1
            if condition_count > self.security_config.max_conditions:
                result.warnings.append(
                    f"Query uses {condition_count} conditions "
                    f"(max {self.security_config.max_conditions})"
                )

        # Count UNION operations
        union_count = sql_str.count("UNION")
        if union_count > self.security_config.max_unions:
            result.errors.append(
                f"Query uses {union_count} UNION operations "
                f"(max {self.security_config.max_unions})"
            )

        # Check subquery depth
        subquery_count = sql_str.count("SELECT") - 1
        if subquery_count > self.security_config.max_subqueries:
            result.errors.append(
                f"Query uses {subquery_count} subqueries "
                f"(max {self.security_config.max_subqueries})"
            )

        return result

    def _validate_schema(self, parsed: Any) -> ValidationResult:
        """Validate query schema.

        Args:
            parsed: Parsed SQL query

        Returns:
            ValidationResult for schema checks
        """
        result = ValidationResult()

        try:
            # Extract tables and columns
            tables = set()
            columns = set()
            for token in parsed.tokens:
                if isinstance(token, sqlparse.sql.Identifier):
                    if "." in str(token):
                        table, column = str(token).split(".")
                        tables.add(table.strip())
                        columns.add(column.strip())
                    else:
                        columns.add(str(token).strip())

            # Validate required tables
            if self.schema_config.enforce_schema:
                missing_tables = self.schema_config.required_tables - tables
                if missing_tables:
                    result.errors.append(
                        f"Missing required tables: {', '.join(missing_tables)}"
                    )

            # Validate required columns
            for table, required_cols in self.schema_config.required_columns.items():
                if table in tables:
                    missing_cols = required_cols - columns
                    if missing_cols:
                        result.errors.append(
                            f"Missing required columns for {table}: "
                            f"{', '.join(missing_cols)}"
                        )

            # Check column limit
            if len(columns) > self.schema_config.max_columns:
                result.warnings.append(
                    f"Query selects {len(columns)} columns "
                    f"(max {self.schema_config.max_columns})"
                )

        except Exception as e:
            result.errors.append(f"Schema validation error: {str(e)}")

        return result

    def _validate_performance(self, parsed: Any) -> ValidationResult:
        """Validate query performance.

        Args:
            parsed: Parsed SQL query

        Returns:
            ValidationResult for performance checks
        """
        result = ValidationResult()

        try:
            # Execute EXPLAIN
            with self.engine.connect() as conn:
                explain = conn.execute(
                    text(f"EXPLAIN ANALYZE {str(parsed)}")
                ).fetchall()

            # Analyze execution plan
            plan_str = "\n".join(str(row[0]) for row in explain)

            # Check for table scans
            table_scans = plan_str.count("Seq Scan")
            if table_scans > self.performance_config.max_table_scan:
                result.warnings.append(
                    f"Query performs {table_scans} table scans "
                    f"(max {self.performance_config.max_table_scan})"
                )

            # Check index usage
            indexes = plan_str.count("Index Scan") + plan_str.count("Index Only Scan")
            total_scans = table_scans + indexes
            if total_scans > 0:
                index_ratio = indexes / total_scans
                if index_ratio < self.performance_config.min_index_usage:
                    result.warnings.append(
                        f"Low index usage ratio: {index_ratio:.2f} "
                        f"(min {self.performance_config.min_index_usage})"
                    )

            # Check memory usage
            if "Memory:" in plan_str:
                memory_str = re.search(r"Memory: (\d+)kB", plan_str)
                if memory_str:
                    memory_kb = int(memory_str.group(1))
                    memory_mb = memory_kb / 1024
                    if memory_mb > self.performance_config.max_memory_mb:
                        result.warnings.append(
                            f"High memory usage: {memory_mb:.2f}MB "
                            f"(max {self.performance_config.max_memory_mb}MB)"
                        )

        except Exception as e:
            result.warnings.append(f"Performance validation error: {str(e)}")

        return result

    def _generate_suggestions(
        self,
        parsed: Any,
        security_result: ValidationResult,
        schema_result: ValidationResult,
        perf_result: ValidationResult
    ) -> List[str]:
        """Generate improvement suggestions.

        Args:
            parsed: Parsed SQL query
            security_result: Security validation result
            schema_result: Schema validation result
            perf_result: Performance validation result

        Returns:
            List of improvement suggestions
        """
        suggestions = []

        # Security suggestions
        if security_result.warnings:
            suggestions.append(
                "Consider simplifying the query by reducing joins and conditions"
            )

        # Schema suggestions
        if schema_result.warnings:
            suggestions.append(
                "Select only necessary columns instead of using SELECT *"
            )

        # Performance suggestions
        if perf_result.warnings:
            suggestions.extend([
                "Add appropriate indexes for frequently queried columns",
                "Use LIMIT clause to restrict result set size",
                "Consider materializing common subqueries"
            ])

        return suggestions
