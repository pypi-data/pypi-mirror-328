"""
Core ADPA framework exceptions.
"""
from typing import Optional, Any


class ADPAError(Exception):
    """Base exception for ADPA framework."""
    
    def __init__(self, message: str, details: Optional[Any] = None):
        """Initialize exception.
        
        Args:
            message: Error message
            details: Optional error details
        """
        super().__init__(message)
        self.details = details


class ConfigurationError(ADPAError):
    """Configuration error."""
    pass


class ValidationError(ADPAError):
    """Validation error."""
    pass


class ProcessingError(ADPAError):
    """Processing error."""
    pass


class PluginError(ADPAError):
    """Plugin error."""
    pass


class StateError(ADPAError):
    """State error."""
    pass


class WorkflowError(ADPAError):
    """Workflow error."""
    pass


class AgentError(ADPAError):
    """Agent error."""
    pass


class SecurityError(ADPAError):
    """Security error."""
    pass


class ResourceError(ADPAError):
    """Resource error."""
    pass


class CacheError(ADPAError):
    """Cache error."""
    pass


class DatabaseError(ADPAError):
    """Database error."""
    pass


class NetworkError(ADPAError):
    """Network error."""
    pass


class TimeoutError(ADPAError):
    """Timeout error."""
    pass
