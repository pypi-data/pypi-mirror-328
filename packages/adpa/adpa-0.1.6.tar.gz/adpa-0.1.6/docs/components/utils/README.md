# ADPA Utils

## Overview

The ADPA Utils module provides a comprehensive set of utilities and helper functions for common tasks across the ADPA framework. These utilities are designed to be reusable, efficient, and well-tested.

## Categories

### 1. Database Utilities

```python
from adpa.utils.database import ConnectionManager, QueryBuilder

class ConnectionManager:
    """Manage database connections."""
    
    async def get_connection(self, database: str) -> Connection:
        """Get database connection from pool.
        
        Args:
            database: Database name
            
        Returns:
            Database connection
        """
        return await self.pool.acquire()
    
    async def execute_query(self, query: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Execute SQL query.
        
        Args:
            query: SQL query
            params: Query parameters
            
        Returns:
            Query results
        """
        async with self.get_connection() as conn:
            return await conn.fetch_all(query, params)
```

### 2. Cache Utilities

```python
from adpa.utils.cache import CacheManager

class CacheManager:
    """Manage caching operations."""
    
    async def get(self, key: str) -> Any:
        """Get value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value
        """
        return await self.redis.get(key)
    
    async def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """Set cache value.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds
        """
        await self.redis.set(key, value, ex=ttl)
```

### 3. Validation Utilities

```python
from adpa.utils.validation import Validator
from pydantic import BaseModel

class Validator:
    """Validate data against schemas."""
    
    def validate_model(self, data: Dict[str, Any], model: Type[BaseModel]) -> BaseModel:
        """Validate data against Pydantic model.
        
        Args:
            data: Data to validate
            model: Pydantic model class
            
        Returns:
            Validated model instance
        """
        return model(**data)
    
    def validate_query(self, query: str) -> bool:
        """Validate SQL query.
        
        Args:
            query: SQL query
            
        Returns:
            True if valid
        """
        return self.sql_validator.is_valid(query)
```

### 4. Security Utilities

```python
from adpa.utils.security import SecurityUtils

class SecurityUtils:
    """Security utility functions."""
    
    def hash_password(self, password: str) -> str:
        """Hash password securely.
        
        Args:
            password: Plain text password
            
        Returns:
            Hashed password
        """
        return self.hasher.hash(password)
    
    def verify_token(self, token: str) -> Dict[str, Any]:
        """Verify JWT token.
        
        Args:
            token: JWT token
            
        Returns:
            Token payload
        """
        return self.jwt.decode(token)
```

### 5. Logging Utilities

```python
from adpa.utils.logging import LogManager

class LogManager:
    """Manage application logging."""
    
    def setup_logging(self, config: Dict[str, Any]) -> None:
        """Setup logging configuration.
        
        Args:
            config: Logging configuration
        """
        logging.config.dictConfig(config)
    
    def log_error(self, error: Exception, context: Dict[str, Any]) -> None:
        """Log error with context.
        
        Args:
            error: Exception instance
            context: Error context
        """
        self.logger.error(str(error), extra=context)
```

### 6. File Utilities

```python
from adpa.utils.files import FileManager

class FileManager:
    """Manage file operations."""
    
    async def save_file(self, file: UploadFile, path: str) -> str:
        """Save uploaded file.
        
        Args:
            file: Uploaded file
            path: Save path
            
        Returns:
            File path
        """
        file_path = Path(path) / file.filename
        await self.write_file(file, file_path)
        return str(file_path)
    
    async def read_json(self, path: str) -> Dict[str, Any]:
        """Read JSON file.
        
        Args:
            path: File path
            
        Returns:
            JSON content
        """
        async with aiofiles.open(path, 'r') as f:
            return json.loads(await f.read())
```

### 7. Date Utilities

```python
from adpa.utils.dates import DateUtils

class DateUtils:
    """Date manipulation utilities."""
    
    def parse_date(self, date_str: str) -> datetime:
        """Parse date string.
        
        Args:
            date_str: Date string
            
        Returns:
            Datetime object
        """
        return dateutil.parser.parse(date_str)
    
    def format_date(self, date: datetime, format: str = "%Y-%m-%d") -> str:
        """Format date.
        
        Args:
            date: Datetime object
            format: Date format
            
        Returns:
            Formatted date string
        """
        return date.strftime(format)
```

## Configuration

Configure utilities using YAML:

```yaml
utils:
  database:
    pool_size: 20
    max_overflow: 10
    timeout: 30
    
  cache:
    backend: redis
    ttl: 3600
    max_size: 1000MB
    
  logging:
    level: INFO
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    handlers:
      - console
      - file
```

## Usage Examples

### 1. Database Operations

```python
from adpa.utils.database import ConnectionManager

# Initialize
conn_manager = ConnectionManager()

# Execute query
results = await conn_manager.execute_query(
    "SELECT * FROM users WHERE age > :age",
    {"age": 18}
)
```

### 2. Caching

```python
from adpa.utils.cache import CacheManager

# Initialize
cache = CacheManager()

# Cache data
await cache.set("user:123", user_data, ttl=3600)

# Get cached data
user = await cache.get("user:123")
```

### 3. Validation

```python
from adpa.utils.validation import Validator
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Validate data
validator = Validator()
user = validator.validate_model(data, User)
```

## Best Practices

1. **Error Handling**
   - Use try-except blocks
   - Log errors properly
   - Return meaningful messages
   - Clean up resources

2. **Performance**
   - Use connection pooling
   - Implement caching
   - Batch operations
   - Optimize I/O

3. **Security**
   - Validate input
   - Sanitize data
   - Use secure defaults
   - Follow best practices

4. **Testing**
   - Unit test utilities
   - Mock external services
   - Test edge cases
   - Measure coverage

## Next Steps

1. [Utils API Reference](../../api_reference/utils.md)
2. [Utils Examples](../../examples/utils.md)
3. [Utils Development Guide](../../development/utils.md)
