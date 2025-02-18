"""Data validation utilities for test data."""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
import re
import uuid

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

class DataValidator:
    """Validator for generated test data."""
    
    @staticmethod
    def validate_uuid(value: str) -> bool:
        """Validate UUID format."""
        try:
            uuid.UUID(str(value))
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_timestamp(timestamp: str) -> bool:
        """Validate ISO timestamp format."""
        try:
            datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return True
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def validate_ip_address(ip: str) -> bool:
        """Validate IPv4 address format."""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(pattern, ip):
            return False
        return all(0 <= int(x) <= 255 for x in ip.split('.'))

class LLMDataValidator(DataValidator):
    """Validator for LLM-related test data."""
    
    def validate_prompt(self, data: Dict[str, Any]) -> List[str]:
        """Validate LLM prompt data."""
        errors = []
        
        required_fields = ['prompt', 'template_type', 'max_tokens', 'temperature']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        if 'max_tokens' in data:
            if not isinstance(data['max_tokens'], int) or not 1 <= data['max_tokens'] <= 4096:
                errors.append("max_tokens must be an integer between 1 and 4096")
        
        if 'temperature' in data:
            if not isinstance(data['temperature'], (int, float)) or not 0 <= data['temperature'] <= 1:
                errors.append("temperature must be a float between 0 and 1")
        
        if 'timestamp' in data and not self.validate_timestamp(data['timestamp']):
            errors.append("Invalid timestamp format")
        
        return errors

class DatabaseDataValidator(DataValidator):
    """Validator for database-related test data."""
    
    def validate_record(self, data: Dict[str, Any], table_name: str) -> List[str]:
        """Validate database record data."""
        errors = []
        
        # Common fields
        if 'id' in data and not self.validate_uuid(data['id']):
            errors.append("Invalid UUID format for id")
        
        for timestamp_field in ['created_at', 'updated_at']:
            if timestamp_field in data and not self.validate_timestamp(data[timestamp_field]):
                errors.append(f"Invalid timestamp format for {timestamp_field}")
        
        # Table-specific validation
        if table_name == 'users':
            if 'email' in data and not self.validate_email(data['email']):
                errors.append("Invalid email format")
            if 'username' in data and not re.match(r'^[a-zA-Z0-9_]{3,30}$', data['username']):
                errors.append("Invalid username format")
        
        elif table_name == 'products':
            if 'price' in data:
                if not isinstance(data['price'], (int, float)) or data['price'] < 0:
                    errors.append("Invalid price value")
            if 'stock' in data:
                if not isinstance(data['stock'], int) or data['stock'] < 0:
                    errors.append("Invalid stock value")
        
        return errors

class APIDataValidator(DataValidator):
    """Validator for API-related test data."""
    
    def validate_request(self, data: Dict[str, Any]) -> List[str]:
        """Validate API request data."""
        errors = []
        
        required_fields = ['request_id', 'timestamp', 'client_id', 'api_version']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        if 'request_id' in data and not self.validate_uuid(data['request_id']):
            errors.append("Invalid UUID format for request_id")
        
        if 'timestamp' in data and not self.validate_timestamp(data['timestamp']):
            errors.append("Invalid timestamp format")
        
        if 'api_version' in data and not re.match(r'^v\d+$', data['api_version']):
            errors.append("Invalid API version format")
        
        return errors
    
    def validate_response(self, data: Dict[str, Any]) -> List[str]:
        """Validate API response data."""
        errors = []
        
        required_fields = ['status_code', 'timestamp', 'request_id', 'success']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        if 'status_code' in data:
            if not isinstance(data['status_code'], int) or not 100 <= data['status_code'] <= 599:
                errors.append("Invalid status code")
        
        if data.get('success', True) and 'data' not in data:
            errors.append("Success response must include data")
        elif not data.get('success', True) and 'error' not in data:
            errors.append("Error response must include error details")
        
        return errors

class SecurityDataValidator(DataValidator):
    """Validator for security-related test data."""
    
    def validate_auth_token(self, data: Dict[str, Any]) -> List[str]:
        """Validate authentication token data."""
        errors = []
        
        required_fields = ['token_type', 'user_id', 'issued_at', 'expires_at', 'scope', 'token']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        if 'user_id' in data and not self.validate_uuid(data['user_id']):
            errors.append("Invalid UUID format for user_id")
        
        for timestamp_field in ['issued_at', 'expires_at']:
            if timestamp_field in data and not self.validate_timestamp(data[timestamp_field]):
                errors.append(f"Invalid timestamp format for {timestamp_field}")
        
        if 'token' in data and data.get('token_type') == 'jwt':
            if not data['token'].startswith('eyJ'):
                errors.append("Invalid JWT format")
        
        return errors
    
    def validate_audit_log(self, data: Dict[str, Any]) -> List[str]:
        """Validate security audit log data."""
        errors = []
        
        required_fields = ['event_id', 'event_type', 'timestamp', 'user_id', 'ip_address', 
                         'user_agent', 'status', 'details']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        if 'event_id' in data and not self.validate_uuid(data['event_id']):
            errors.append("Invalid UUID format for event_id")
        
        if 'ip_address' in data and not self.validate_ip_address(data['ip_address']):
            errors.append("Invalid IP address format")
        
        if 'status' in data and data['status'] not in ['success', 'failure']:
            errors.append("Invalid status value")
        
        return errors
