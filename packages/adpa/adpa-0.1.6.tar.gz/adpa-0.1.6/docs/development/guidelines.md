# Development Guidelines

## Code Organization

### Project Structure
```
adpa/
├── src/
│   └── adpa/
│       ├── core/         # Core functionality
│       ├── api/          # API endpoints
│       ├── text2sql/     # Text2SQL component
│       ├── agents/       # Agent system
│       ├── monitoring/   # Monitoring system
│       ├── security/     # Security features
│       └── utils/        # Utility functions
├── tests/               # Test suite
├── docs/               # Documentation
├── examples/           # Example code
└── scripts/           # Development scripts
```

### File Organization
- Maximum file length: 500 lines
- One class per file (with exceptions for small related classes)
- Related functionality grouped in modules
- Clear separation of concerns

## Coding Style

### General Guidelines
1. Follow PEP 8 with specified modifications
2. Use type hints for all functions
3. Write clear, self-documenting code
4. Keep functions focused and small
5. Use descriptive variable names

### Naming Conventions
```python
# Classes use PascalCase
class UserManager:
    pass

# Functions and variables use snake_case
def process_data():
    user_count = 0

# Constants use SCREAMING_SNAKE_CASE
MAX_RETRIES = 3

# Private members use _prefix
def _internal_method():
    pass

# Protected members use __prefix
def __protected_method():
    pass
```

### Documentation
```python
def process_user_data(
    user_id: str,
    data: Dict[str, Any],
    options: Optional[Dict[str, Any]] = None
) -> ProcessingResult:
    """Process user data with given options.
    
    Args:
        user_id: Unique identifier for the user
        data: User data to process
        options: Optional processing configuration
        
    Returns:
        ProcessingResult containing processed data
        
    Raises:
        ValueError: If user_id is empty or data is invalid
        ProcessingError: If processing fails
        
    Example:
        >>> result = process_user_data("user123", {"name": "John"})
        >>> print(result.success)
        True
    """
    pass
```

## Testing

### Test Organization
```python
# test_user_manager.py

import pytest
from adpa.core import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

class TestUserManager:
    def test_should_create_user_when_valid_data(self, user_manager):
        # Arrange
        user_data = {"name": "John"}
        
        # Act
        result = user_manager.create_user(user_data)
        
        # Assert
        assert result.success is True
        assert result.user.name == "John"
```

### Test Guidelines
1. Use descriptive test names
2. Follow Arrange-Act-Assert pattern
3. One assertion per test (with reasonable exceptions)
4. Use appropriate fixtures
5. Mock external dependencies
6. Test edge cases and error conditions

## Error Handling

### Guidelines
1. Use specific exception types
2. Provide helpful error messages
3. Log errors appropriately
4. Clean up resources in finally blocks
5. Don't catch bare exceptions

### Example
```python
class UserNotFoundError(Exception):
    """Raised when user is not found."""
    pass

def get_user(user_id: str) -> User:
    """Get user by ID.
    
    Args:
        user_id: User ID to look up
        
    Returns:
        User object
        
    Raises:
        UserNotFoundError: If user does not exist
        DatabaseError: If database operation fails
    """
    try:
        user = db.query(User).filter_by(id=user_id).first()
        if user is None:
            raise UserNotFoundError(f"User {user_id} not found")
        return user
    except DatabaseError as e:
        logger.error(f"Database error: {e}")
        raise
```

## Performance

### Guidelines
1. Profile before optimizing
2. Use appropriate data structures
3. Batch operations when possible
4. Cache expensive operations
5. Use async where appropriate

### Example
```python
class DataProcessor:
    def __init__(self):
        self.cache = LRUCache(maxsize=1000)
    
    async def process_batch(
        self,
        items: List[Dict[str, Any]]
    ) -> List[ProcessingResult]:
        """Process multiple items in batch.
        
        Args:
            items: List of items to process
            
        Returns:
            List of processing results
        """
        results = []
        batch_size = 100
        
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            batch_results = await asyncio.gather(
                *(self.process_item(item) for item in batch)
            )
            results.extend(batch_results)
        
        return results
```

## Security

### Guidelines
1. Validate all input
2. Use parameterized queries
3. Follow principle of least privilege
4. Don't store secrets in code
5. Use secure defaults

### Example
```python
class UserAuth:
    def __init__(self, config: SecurityConfig):
        self.min_password_length = config.min_password_length
        self.max_login_attempts = config.max_login_attempts
    
    def validate_password(self, password: str) -> bool:
        """Validate password strength.
        
        Args:
            password: Password to validate
            
        Returns:
            True if password meets requirements
        """
        if len(password) < self.min_password_length:
            return False
            
        # Check for complexity requirements
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        return all([has_upper, has_lower, has_digit, has_special])
```

## API Design

### Guidelines
1. Use RESTful principles
2. Version your APIs
3. Use consistent naming
4. Provide comprehensive documentation
5. Include proper error responses

### Example
```python
@router.post("/api/v1/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    """Create new user.
    
    Args:
        user: User creation data
        current_user: Currently authenticated user
        
    Returns:
        Created user data
        
    Raises:
        HTTPException: If user creation fails
    """
    try:
        return await user_service.create_user(user)
    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except DuplicateUserError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )
```

## Logging

### Guidelines
1. Use appropriate log levels
2. Include relevant context
3. Don't log sensitive data
4. Use structured logging
5. Include request IDs

### Example
```python
import structlog

logger = structlog.get_logger()

class PaymentProcessor:
    def process_payment(
        self,
        payment_id: str,
        amount: Decimal
    ) -> PaymentResult:
        """Process payment.
        
        Args:
            payment_id: Payment identifier
            amount: Payment amount
            
        Returns:
            Payment processing result
        """
        logger.info(
            "processing_payment",
            payment_id=payment_id,
            amount=str(amount)
        )
        
        try:
            result = self._do_process_payment(payment_id, amount)
            
            logger.info(
                "payment_processed",
                payment_id=payment_id,
                success=result.success
            )
            
            return result
            
        except Exception as e:
            logger.exception(
                "payment_failed",
                payment_id=payment_id,
                error=str(e)
            )
            raise
```

## Configuration Management

### Guidelines
1. Use environment variables for secrets
2. Use configuration files for other settings
3. Validate configuration at startup
4. Provide sensible defaults
5. Document all configuration options

### Example
```python
from pydantic import BaseSettings, Field

class AppConfig(BaseSettings):
    """Application configuration.
    
    Attributes:
        database_url: Database connection URL
        api_key: API authentication key
        debug: Debug mode flag
        max_connections: Maximum database connections
    """
    
    database_url: str = Field(
        ...,
        env="DATABASE_URL",
        description="Database connection URL"
    )
    
    api_key: str = Field(
        ...,
        env="API_KEY",
        description="API authentication key"
    )
    
    debug: bool = Field(
        False,
        env="DEBUG",
        description="Debug mode flag"
    )
    
    max_connections: int = Field(
        100,
        env="MAX_CONNECTIONS",
        description="Maximum database connections"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```
