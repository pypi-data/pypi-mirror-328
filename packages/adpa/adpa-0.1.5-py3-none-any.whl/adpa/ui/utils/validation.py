"""Input validation utilities for the UI."""

import re
from typing import Any, Dict, List, Optional, Tuple

class InputValidator:
    """Validates user input in the UI."""

    @staticmethod
    def validate_query(query: str) -> Tuple[bool, Optional[str]]:
        """Validate a user query.
        
        Args:
            query: The query string to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not query:
            return False, "Query cannot be empty"
        if len(query) < 3:
            return False, "Query must be at least 3 characters long"
        if len(query) > 1000:
            return False, "Query must be less than 1000 characters"
        return True, None

    @staticmethod
    def validate_file_upload(
        file: Any,
        allowed_types: Optional[List[str]] = None,
        max_size_mb: int = 10
    ) -> Tuple[bool, Optional[str]]:
        """Validate an uploaded file.
        
        Args:
            file: The uploaded file object
            allowed_types: List of allowed file extensions
            max_size_mb: Maximum file size in MB
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not file:
            return False, "No file uploaded"

        # Check file type
        if allowed_types:
            file_type = file.name.split(".")[-1].lower()
            if file_type not in allowed_types:
                return False, f"File type must be one of: {', '.join(allowed_types)}"

        # Check file size
        if file.size > max_size_mb * 1024 * 1024:
            return False, f"File size must be less than {max_size_mb}MB"

        return True, None

    @staticmethod
    def validate_config(config: Dict[str, Any], required_fields: List[str]) -> Tuple[bool, Optional[str]]:
        """Validate a configuration dictionary.
        
        Args:
            config: The configuration dictionary
            required_fields: List of required field names
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        for field in required_fields:
            if field not in config:
                return False, f"Missing required field: {field}"
            if config[field] is None:
                return False, f"Field cannot be None: {field}"
        return True, None

    @staticmethod
    def validate_email(email: str) -> Tuple[bool, Optional[str]]:
        """Validate an email address.
        
        Args:
            email: The email address to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            return False, "Invalid email address"
        return True, None

    @staticmethod
    def validate_url(url: str) -> Tuple[bool, Optional[str]]:
        """Validate a URL.
        
        Args:
            url: The URL to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        pattern = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
        if not re.match(pattern, url):
            return False, "Invalid URL"
        return True, None
