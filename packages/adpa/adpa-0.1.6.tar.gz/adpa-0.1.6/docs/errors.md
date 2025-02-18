# ADPA Error Reference

Version 0.7.0

## Overview
This document provides a comprehensive list of error codes and their resolutions in the ADPA framework.

For development guidelines, see [Development Guide](/docs/development.md).

## Common Error Types

### LLMAPIError
Base error class for API-related issues.

```python
try:
    response = await chat_model.ainvoke("Hello")
except LLMAPIError as e:
    print(f"API Error: {e}")
```

#### Common Scenarios
1. **Rate Limiting**
   ```
   LLMAPIError: Rate limit exceeded. Please wait before retrying.
   ```
   - Cause: Too many requests in a short time
   - Solution: System will automatically retry with backoff

2. **Network Issues**
   ```
   LLMAPIError: Connection timeout after 10s
   ```
   - Cause: Network connectivity problems
   - Solution: Check internet connection, system will retry

3. **Authentication**
   ```
   LLMAPIError: Invalid API key provided
   ```
   - Cause: Missing or invalid API key
   - Solution: Check OPENAI_API_KEY environment variable

## Error Handling

### Retry Behavior
The system automatically retries on recoverable errors:

```python
# Example with retry
try:
    response = await chat_model.ainvoke("Hello")
except LLMAPIError as e:
    if e.is_retryable:
        print("Error was retried automatically")
    else:
        print("Non-retryable error")
```

### Logging
Errors are logged with context:

```
[ERROR] Max retries (3) reached. Last error: Rate limit exceeded
Details:
- Attempt: 3/3
- Delay: 4s
- Error Type: RateLimitError
```

## Troubleshooting Steps

### 1. Check API Key
```bash
# Verify API key is set
echo $OPENAI_API_KEY
```

### 2. Check Network
```bash
# Test API connectivity
curl https://api.openai.com/v1/models
```

### 3. Check Logs
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Best Practices

### 1. Handle Errors Appropriately
```python
try:
    response = await chat_model.ainvoke("Hello")
except LLMAPIError as e:
    logger.error(f"API Error: {e}")
    # Handle gracefully
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    # Handle other errors
```

### 2. Use Async Context Managers
```python
async with ChatModel(client) as chat:
    response = await chat.ainvoke("Hello")
```

### 3. Monitor Retry Patterns
```python
# Future enhancement
chat_model.get_retry_statistics()
```

## Error Prevention

### 1. Rate Limiting
- Use appropriate delays between requests
- Monitor rate limit headers
- Implement request queuing

### 2. Network Resilience
- Set appropriate timeouts
- Handle connection pooling
- Use circuit breakers

### 3. Error Recovery
- Implement fallback options
- Cache responses where appropriate
- Use dead letter queues

## Contributing
Found a new error pattern? Please:
1. Document the error
2. Create a test case
3. Submit a pull request
