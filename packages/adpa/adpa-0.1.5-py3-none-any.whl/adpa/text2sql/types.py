"""Type definitions for the text2sql module."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union


class SQLDialect(Enum):
    """Supported SQL dialects."""
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    SQLITE = "sqlite"
    MSSQL = "mssql"


class ColumnType(Enum):
    """Common SQL column types."""
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    DECIMAL = "DECIMAL"
    VARCHAR = "VARCHAR"
    TEXT = "TEXT"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    TIMESTAMP = "TIMESTAMP"
    JSON = "JSON"
    JSONB = "JSONB"
    UUID = "UUID"


@dataclass(frozen=True)
class GeneratorConfig:
    """Configuration for SQL generation."""
    temperature: float = 0.3
    max_tokens: int = 500
    model: str = "gpt-4"
    dialect: SQLDialect = SQLDialect.POSTGRESQL
    max_query_length: int = 1000
    include_comments: bool = True
    safe_mode: bool = True  # Prevents destructive operations
    timeout: int = 30


@dataclass(frozen=True)
class ColumnSchema:
    """Schema definition for a database column."""
    name: str
    type: ColumnType
    nullable: bool = True
    default: Optional[str] = None
    primary_key: bool = False
    unique: bool = False
    foreign_key: Optional[str] = None  # Format: "table.column"
    check_constraint: Optional[str] = None
    description: Optional[str] = None


@dataclass(frozen=True)
class IndexSchema:
    """Schema definition for a database index."""
    name: str
    columns: List[str]
    unique: bool = False
    type: str = "btree"  # btree, hash, gist, etc.
    where: Optional[str] = None  # Partial index condition


@dataclass(frozen=True)
class TableSchema:
    """Schema definition for a single table."""
    name: str
    columns: List[ColumnSchema]
    indexes: List[IndexSchema] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    description: Optional[str] = None


@dataclass(frozen=True)
class SchemaConfig:
    """Database schema configuration."""
    tables: Dict[str, TableSchema]
    version: str = "1.0.0"
    dialect: SQLDialect = SQLDialect.POSTGRESQL
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class QueryResult:
    """Result of SQL query generation."""
    query: str
    confidence: float
    explanation: str
    warnings: List[str]
    suggested_indexes: List[IndexSchema]
    estimated_complexity: str  # O(n), O(n log n), etc.
    tables_used: List[str]


@dataclass(frozen=True)
class ValidationError:
    """Schema validation error."""
    path: str  # JSON path to the error
    message: str
    severity: str  # "error", "warning"
    suggestion: Optional[str] = None
