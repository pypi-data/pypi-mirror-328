"""Custom exceptions for text-to-SQL conversion."""

from typing import Dict, List, Optional


class Text2SQLError(Exception):
    """Base exception for text-to-SQL errors."""

    def __init__(
        self,
        message: str,
        details: Optional[Dict] = None,
        suggestions: Optional[List[str]] = None
    ):
        """Initialize error with details and suggestions.
        
        Args:
            message: Error message
            details: Additional error details
            suggestions: Improvement suggestions
        """
        super().__init__(message)
        self.details = details or {}
        self.suggestions = suggestions or []


class MaxAttemptsExceeded(Text2SQLError):
    """Raised when maximum number of query generation attempts is exceeded."""
    pass


class ValidationError(Text2SQLError):
    """Raised when query validation fails."""
    pass


class ContextError(Text2SQLError):
    """Raised when there are issues with context gathering or processing."""
    pass


class ExecutionError(Text2SQLError):
    """Raised when query execution fails."""
    pass


class SchemaError(Text2SQLError):
    """Raised when there are issues with database schema."""
    pass


class SecurityError(Text2SQLError):
    """Raised when security checks fail."""
    pass


class OptimizationError(Text2SQLError):
    """Raised when query optimization fails."""
    pass
