"""Input sanitization module for ADPA Framework.

This module provides comprehensive input sanitization and validation capabilities
to prevent XSS, SQL injection, and other input-based attacks.
"""
from typing import Any, Dict, List, Optional, Union, Set
import re
from pydantic import BaseModel, Field, validator
from html import escape
import bleach
from fastapi import Request


class SanitizationConfig(BaseModel):
    """Configuration for input sanitization."""
    
    allowed_html_tags: Set[str] = Field(
        default={
            "p", "br", "strong", "em", "u", "ul", "ol", "li",
            "h1", "h2", "h3", "h4", "h5", "h6"
        },
        description="HTML tags that are allowed in input"
    )
    allowed_html_attributes: Dict[str, List[str]] = Field(
        default={
            "*": ["class", "id", "style"],
            "a": ["href", "title", "target", "rel"],
            "img": ["src", "alt", "title", "width", "height"]
        },
        description="Allowed HTML attributes for specific tags"
    )
    max_length: int = Field(
        default=10000,
        gt=0,
        description="Maximum length of input string"
    )
    strip_comments: bool = Field(
        default=True,
        description="Whether to strip HTML comments"
    )
    escape_sql: bool = Field(
        default=True,
        description="Whether to escape SQL special characters"
    )
    url_schemes: Set[str] = Field(
        default={"http", "https"},
        description="Allowed URL schemes"
    )
    
    class Config:
        """Pydantic model configuration."""
        frozen = True


class InputSanitizer:
    """Main sanitization class for handling various types of input."""
    
    def __init__(self, config: Optional[SanitizationConfig] = None) -> None:
        """Initialize sanitizer with configuration.
        
        Args:
            config: Optional sanitization configuration
        """
        self.config = config or SanitizationConfig()
        self._sql_regex = re.compile(r"[;'\"]")
        self._xss_regex = re.compile(r"<script.*?>.*?</script>", re.I | re.S)
        self._url_regex = re.compile(
            r"^(?P<scheme>[a-z]+)://[^\s/$.?#].[^\s]*$",
            re.I
        )
    
    def sanitize_string(self, value: str) -> str:
        """Sanitize a string input.
        
        Args:
            value: Input string to sanitize
            
        Returns:
            Sanitized string
            
        Raises:
            ValueError: If input exceeds max length
        """
        if len(value) > self.config.max_length:
            raise ValueError(f"Input exceeds maximum length of {self.config.max_length}")
        
        # Basic cleaning
        value = value.strip()
        
        # HTML sanitization
        value = bleach.clean(
            value,
            tags=self.config.allowed_html_tags,
            attributes=self.config.allowed_html_attributes,
            strip=True,
            strip_comments=self.config.strip_comments
        )
        
        # SQL injection prevention
        if self.config.escape_sql:
            value = self._sql_regex.sub(lambda m: f"\\{m.group()}", value)
        
        return value
    
    def sanitize_url(self, url: str) -> str:
        """Sanitize a URL string.
        
        Args:
            url: URL to sanitize
            
        Returns:
            Sanitized URL
            
        Raises:
            ValueError: If URL is invalid or uses disallowed scheme
        """
        match = self._url_regex.match(url)
        if not match:
            raise ValueError("Invalid URL format")
        
        scheme = match.group("scheme").lower()
        if scheme not in self.config.url_schemes:
            raise ValueError(f"URL scheme '{scheme}' not allowed")
        
        return url
    
    def sanitize_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively sanitize a dictionary of values.
        
        Args:
            data: Dictionary to sanitize
            
        Returns:
            Sanitized dictionary
        """
        result = {}
        for key, value in data.items():
            if isinstance(value, str):
                result[key] = self.sanitize_string(value)
            elif isinstance(value, dict):
                result[key] = self.sanitize_dict(value)
            elif isinstance(value, list):
                result[key] = self.sanitize_list(value)
            else:
                result[key] = value
        return result
    
    def sanitize_list(self, data: List[Any]) -> List[Any]:
        """Recursively sanitize a list of values.
        
        Args:
            data: List to sanitize
            
        Returns:
            Sanitized list
        """
        result = []
        for item in data:
            if isinstance(item, str):
                result.append(self.sanitize_string(item))
            elif isinstance(item, dict):
                result.append(self.sanitize_dict(item))
            elif isinstance(item, list):
                result.append(self.sanitize_list(item))
            else:
                result.append(item)
        return result


class SanitizationMiddleware:
    """FastAPI middleware for automatic input sanitization."""
    
    def __init__(
        self,
        sanitizer: Optional[InputSanitizer] = None,
        skip_paths: Optional[List[str]] = None
    ) -> None:
        """Initialize middleware.
        
        Args:
            sanitizer: Optional custom sanitizer instance
            skip_paths: Optional list of paths to skip sanitization
        """
        self.sanitizer = sanitizer or InputSanitizer()
        self.skip_paths = set(skip_paths or [])
    
    async def __call__(self, request: Request, call_next: Any) -> Any:
        """Process the request and sanitize input.
        
        Args:
            request: FastAPI request
            call_next: Next middleware in chain
            
        Returns:
            Response from next middleware
        """
        if request.url.path in self.skip_paths:
            return await call_next(request)
            
        # Clone and sanitize request
        body = await request.body()
        if body:
            try:
                data = await request.json()
                if isinstance(data, dict):
                    sanitized_data = self.sanitizer.sanitize_dict(data)
                    # Update request state with sanitized data
                    setattr(request.state, "sanitized_data", sanitized_data)
            except ValueError:
                pass  # Not JSON data
                
        response = await call_next(request)
        return response
