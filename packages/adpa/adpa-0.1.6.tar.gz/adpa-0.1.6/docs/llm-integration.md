# LLM Integration

ADPA provides a unified interface for multiple Language Model (LLM) providers, enabling seamless integration of various AI models into your applications.

## Supported Providers

### OpenAI
- Models: GPT-4, GPT-3.5-turbo
- Features: Chat completion, embeddings
- Configuration via `OPENAI_API_KEY`

### Google (Gemini)
- Models: Gemini Pro
- Features: Chat completion, embeddings
- Configuration via `GOOGLE_API_KEY`

### Groq
- Models: LLaMA2 variants
- Features: Chat completion
- Configuration via `GROQ_API_KEY`

## Configuration

### Model Configuration
Models are configured in `adpa/llms/config/model_configs.json`:

```json
{
  "openai": {
    "default": "gpt-4",
    "models": {
      "gpt-4": {
        "id": "gpt-4",
        "base_model": "gpt-4",
        "description": "Most capable GPT-4 model",
        "temperature": 0.7,
        "max_tokens": 8192
      }
    }
  }
}
```

### Environment Variables
Set the following environment variables:
```bash
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
```

## Usage Examples

### Basic Text Generation
```python
from adpa.llms.openai import OpenAILLM

# Initialize client
client = OpenAILLM("gpt-4")

# Generate text
result = await client.generate("Tell me about ADPA")
print(result["text"])
```

### Chat Completion
```python
from adpa.llms.gemini import GeminiLLM

# Initialize client
client = GeminiLLM("gemini-pro")

# Chat messages
messages = [
    {"role": "user", "content": "What is ADPA?"},
    {"role": "assistant", "content": "ADPA is an AI framework..."},
    {"role": "user", "content": "Tell me more"}
]

# Generate chat response
result = await client.generate(messages)
print(result["text"])
```

### Embeddings
```python
from adpa.llms.openai import OpenAILLM

# Initialize client
client = OpenAILLM("text-embedding-ada-002")

# Generate embeddings
result = await client.embed("ADPA is awesome")
print(result["embeddings"])
```

## Error Handling

ADPA provides comprehensive error handling through the `adpa.llms.errors` module:

### Error Categories
- `ConfigurationError`: Configuration-related issues
- `AuthenticationError`: API key and authentication issues
- `RateLimitError`: Rate limiting and quota issues
- `TokenLimitError`: Token limit exceeded
- `ValidationError`: Input validation issues
- `ProviderError`: Provider-specific errors
- `CapabilityError`: Model capability issues
- `NetworkError`: Network and connectivity issues
- `TimeoutError`: Request timeout issues

### Example Error Handling
```python
from adpa.llms.errors import LLMError, RateLimitError

try:
    result = await client.generate("test")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after: {e.details['retry_after']} seconds")
except LLMError as e:
    print(f"Error: {e.message}")
    print(f"Category: {e.category}")
    print(f"Details: {e.details}")
```

## Testing

ADPA includes comprehensive Robot Framework tests for LLM functionality:

### Running Tests
```bash
robot tests/robot/llm_tests.robot
```

### Test Categories
- Configuration validation
- Text generation
- Chat completion
- Embeddings
- Error handling
- Rate limiting
- Token validation

## Logging

ADPA uses Python's logging system for comprehensive logging:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("adpa.llms")

# Logs will include:
# - Request/response details
# - Error information
# - Performance metrics
# - Token usage
```

## Best Practices

1. **Error Handling**
   - Always wrap LLM calls in try-except blocks
   - Handle specific error types appropriately
   - Log errors with context

2. **Configuration**
   - Use environment variables for API keys
   - Configure model parameters in JSON
   - Set appropriate timeouts

3. **Performance**
   - Monitor token usage
   - Implement rate limiting
   - Cache results when appropriate

4. **Testing**
   - Run Robot Framework tests regularly
   - Mock API calls in tests
   - Test error scenarios

5. **Security**
   - Never commit API keys
   - Validate user input
   - Monitor usage and costs
