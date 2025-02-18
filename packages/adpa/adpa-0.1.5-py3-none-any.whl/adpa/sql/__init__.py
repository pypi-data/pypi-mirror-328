"""
SQL module for ADPA framework.

This module provides SQL query generation, validation, and middleware components:
- Query generation with structured reasoning
- Query validation and security checks
- SQL middleware for request processing
"""

from adpa.sql.generator import (
    SQLGenerator,
    SQLGenerationConfig,
    ReasoningPhase,
    AnalysisPhase,
    QueryPhase,
    VerificationPhase
)
from adpa.sql.validation import (
    SQLValidator,
    ValidationResult,
    SecurityValidation,
    SchemaValidation,
    PerformanceValidation
)
from adpa.sql.middleware import SQLMiddleware

__all__ = [
    "SQLGenerator",
    "SQLGenerationConfig",
    "ReasoningPhase",
    "AnalysisPhase",
    "QueryPhase",
    "VerificationPhase",
    "SQLValidator",
    "ValidationResult",
    "SecurityValidation",
    "SchemaValidation",
    "PerformanceValidation",
    "SQLMiddleware"
]
