# Input Sanitization

## Overview
The ADPA Framework provides comprehensive input sanitization to prevent common security vulnerabilities such as XSS (Cross-Site Scripting) and SQL injection attacks.

## Features
- HTML sanitization with configurable allowed tags and attributes
- SQL injection prevention
- XSS protection
- Configurable maximum input length
- Support for nested data structures
- FastAPI middleware integration

## Installation
The input sanitization module is included in the ADPA Framework core package:

```bash
pip install adpa
```

## Basic Usage

### Simple String Sanitization
```python
from adpa.security.sanitization.sanitizer import InputSanitizer

sanitizer = InputSanitizer()
clean_text = sanitizer.sanitize_string("<script>alert('xss')</script>Hello World")
print(clean_text)  # Output: Hello World
```

### Custom Configuration
```python
from adpa.security.sanitization.sanitizer import SanitizationConfig, InputSanitizer

config = SanitizationConfig(
    allowed_html_tags=["p", "br", "strong"],
    allowed_html_attributes={"p": ["class"]},
    max_length=1000,
    strip_comments=True,
    escape_sql=True
)

sanitizer = InputSanitizer(config)
```

### FastAPI Integration
```python
from fastapi import FastAPI
from adpa.security.sanitization.sanitizer import SanitizationMiddleware

app = FastAPI()
app.add_middleware(
    SanitizationMiddleware,
    skip_paths=["/health"]
)
```

## Configuration Options

### SanitizationConfig
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| allowed_html_tags | List[str] | ["p", "br", "strong", ...] | HTML tags to allow |
| allowed_html_attributes | Dict[str, List[str]] | {"*": ["class"], ...} | Allowed HTML attributes |
| max_length | int | 10000 | Maximum input length |
| strip_comments | bool | True | Remove HTML comments |
| escape_sql | bool | True | Escape SQL special chars |

## Security Considerations

### XSS Prevention
The sanitizer removes potentially dangerous HTML tags and attributes:
```python
input_text = '<script>alert("xss")</script><p>Hello</p>'
clean_text = sanitizer.sanitize_string(input_text)
# Output: <p>Hello</p>
```

### SQL Injection Prevention
SQL special characters are escaped:
```python
input_text = "'; DROP TABLE users; --"
clean_text = sanitizer.sanitize_string(input_text)
# Output: \'; DROP TABLE users\; \-\-
```

## Best Practices

1. **Always Validate Input**
   ```python
   # Validate and sanitize all user input
   user_input = request.form.get("comment")
   clean_input = sanitizer.sanitize_string(user_input)
   ```

2. **Use Custom Configurations**
   ```python
   # Restrict allowed HTML based on context
   config = SanitizationConfig(
       allowed_html_tags=["p", "br"],
       max_length=500
   )
   ```

3. **Handle Nested Data**
   ```python
   # Sanitize complex data structures
   data = {
       "title": user_title,
       "content": user_content,
       "tags": user_tags
   }
   clean_data = sanitizer.sanitize_dict(data)
   ```

## Error Handling

### Maximum Length Exceeded
```python
try:
    clean_text = sanitizer.sanitize_string(very_long_text)
except ValueError as e:
    logger.error(f"Input validation failed: {e}")
    raise HTTPException(status_code=400, detail="Input too long")
```

## Testing

Run the test suite:
```bash
pytest tests/security/sanitization/test_sanitizer.py -v
```

## Performance Considerations

1. **Configure Maximum Length**
   - Set appropriate `max_length` to prevent DoS attacks
   - Consider your application's requirements

2. **Skip Paths When Possible**
   ```python
   app.add_middleware(
       SanitizationMiddleware,
       skip_paths=["/health", "/metrics"]
   )
   ```

3. **Cache Sanitized Results**
   - Consider caching sanitized results for static content
   - Use appropriate cache invalidation strategies

## Contributing

See our [Contributing Guide](../contributing.md) for details on:
- Setting up the development environment
- Running tests
- Submitting pull requests
