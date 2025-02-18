"""Core exceptions for ADPA framework."""
from typing import Any


class ADPAError(Exception):
    """Base exception for all ADPA errors."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        """Initialize ADPAError.

        Args:
            message: Error message
            details: Additional error details
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}


class ConfigurationError(ADPAError):
    """Raised when there is a configuration error."""

    pass


class ValidationError(ADPAError):
    """Raised when validation fails."""

    pass


class ProcessingError(ADPAError):
    """Raised when processing fails."""

    pass


class ResourceError(ADPAError):
    """Raised when a resource is unavailable."""

    pass


class AuthenticationError(ADPAError):
    """Raised when authentication fails."""

    pass


class AuthorizationError(ADPAError):
    """Raised when authorization fails."""

    pass


class RateLimitError(ADPAError):
    """Raised when rate limit is exceeded."""

    pass


class DatabaseError(ADPAError):
    """Raised when database operation fails."""

    pass


class NetworkError(ADPAError):
    """Raised when network operation fails."""

    pass


class TimeoutError(ADPAError):
    """Raised when operation times out."""

    pass


class ConcurrencyError(ADPAError):
    """Raised when concurrent operation fails."""

    pass


class NotFoundError(ADPAError):
    """Raised when resource is not found."""

    pass


class DuplicateError(ADPAError):
    """Raised when duplicate resource is detected."""

    pass


class InvalidOperationError(ADPAError):
    """Raised when operation is invalid."""

    pass


class LLMError(ADPAError):
    """Raised when LLM operation fails."""

    pass


class AgentError(ADPAError):
    """Raised when agent operation fails."""

    pass


class Text2SQLError(ADPAError):
    """Raised when Text2SQL operation fails."""

    pass


class MonitoringError(ADPAError):
    """Raised when monitoring operation fails."""

    pass


class SecurityError(ADPAError):
    """Raised when security check fails."""

    pass


def format_error(error: Exception) -> dict[str, Any]:
    """Format exception for error response.

    Args:
        error: Exception to format

    Returns:
        Formatted error dictionary
    """
    if isinstance(error, ADPAError):
        return {
            "error": error.__class__.__name__,
            "message": error.message,
            "details": error.details,
        }
    return {
        "error": error.__class__.__name__,
        "message": str(error),
        "details": {},
    }
