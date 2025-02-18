"""
ADPA Text2SQL Module.

This module provides functionality for converting natural language queries to SQL,
with support for schema validation, query optimization, and security features.

Features:
    - Natural language to SQL conversion
    - Schema learning and adaptation
    - Context management
    - Query validation
    - Vector store integration
    - Feedback processing
    - Performance monitoring
    - Security checks
"""

from adpa.text2sql.generator import SQLGenerator
from adpa.text2sql.types import (
    GeneratorConfig, SchemaConfig, QueryResult,
    QueryFeedback, QueryContext, QueryMetrics
)
from adpa.text2sql.models import (
    Column, Table, Index, Schema,
    DatabaseConfig, ValidationResult
)
from adpa.text2sql.validation import SQLValidator
from adpa.text2sql.utils import (
    analyze_query_complexity,
    extract_table_references,
    suggest_indexes,
    suggest_joins
)

__all__ = [
    # Main components
    "SQLGenerator",
    
    # Configuration
    "GeneratorConfig",
    "SchemaConfig",
    "DatabaseConfig",
    
    # Models
    "Column",
    "Table",
    "Index",
    "Schema",
    "QueryResult",
    "QueryFeedback",
    "QueryContext",
    "QueryMetrics",
    "ValidationResult",
    
    # Utilities
    "SQLValidator",
    "analyze_query_complexity",
    "extract_table_references",
    "suggest_indexes",
    "suggest_joins"
]

__version__ = "1.4.1"
