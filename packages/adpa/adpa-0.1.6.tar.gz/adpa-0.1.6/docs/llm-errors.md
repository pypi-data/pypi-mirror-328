# LLM Error Handling Guide

This guide covers error handling, resilience features, and monitoring capabilities in ADPA v1.1.0.

## Error Types

### 1. Base Errors
- `LLMError`: Base exception class
- `ConfigurationError`: Configuration issues
- `ValidationError`: Input validation
- `ProviderError`: Provider-specific errors

### 2. Network Errors
- `NetworkResilienceError`: Base network error
  - `connection_refused`: Connection issues
  - `timeout`: Request timeouts
  - `dns_error`: DNS resolution
  - `ssl_error`: SSL/TLS issues

### 3. Rate Limit Errors
- `RateLimitError`: Rate limiting issues
  - `requests_per_minute`: RPM limits
  - `tokens_per_minute`: TPM limits
  - `concurrent_requests`: Concurrency limits

### 4. Provider Errors
- `ProviderUnavailableError`: Provider down
- `ModelNotFoundError`: Invalid model
- `InvalidRequestError`: Bad request
- `AuthenticationError`: Auth issues

## Resilience Features

### 1. Provider Failover
```python
from adpa.llms.resilience.failover import FailoverManager, FailoverConfig

# Configure failover
manager = FailoverManager(
    primary="openai",
    secondaries=["gemini", "groq"],
    config=FailoverConfig(
        max_attempts=3,
        timeout=30.0,
        backoff_factor=2.0,
        jitter=0.1
    )
)

# Use with failover
try:
    result = await manager.execute_with_failover({
        "prompt": "Hello, world!",
        "max_tokens": 100
    })
except FailoverError as e:
    print(f"All providers failed: {e}")
```

### 2. Circuit Breaking
```python
from adpa.llms.resilience.circuit_breaker import CircuitBreaker, CircuitConfig

# Configure circuit breaker
breaker = CircuitBreaker(
    name="openai_breaker",
    config=CircuitConfig(
        failure_threshold=5,
        reset_timeout=60.0,
        half_open_timeout=5.0,
        success_threshold=2
    )
)

# Use with circuit breaker
try:
    result = await breaker.execute(request, operation)
except CircuitBreakerError as e:
    print(f"Circuit is open: {e}")
```

### 3. Error Tracking
```python
from adpa.llms.errors.tracking import ErrorTracker

# Initialize tracker
tracker = ErrorTracker()

# Record errors
tracker.record_error(
    error_type="network",
    message="Connection refused"
)

# Check status
status = tracker.get_status()
print(f"Error rate: {status['error_rate']:.1%}")
print(f"Is blocked: {status['is_blocked']}")
```

### 4. Metrics Monitoring
```python
from adpa.llms.monitoring.metrics import ProviderMetrics

# Initialize metrics
metrics = ProviderMetrics()

# Record success
metrics.record_success(
    latency=0.5,
    tokens=150,
    cost=0.002
)

# Record error
metrics.record_error(
    error_type="timeout",
    message="Request timed out"
)

# Get metrics
print(f"Success rate: {metrics.get_success_rate():.1%}")
print(f"Error rate: {metrics.get_error_rate():.1%}")
print(f"Avg latency: {metrics.average_latency:.2f}s")
```

## Best Practices

### 1. Error Handling
- Always use try/except blocks
- Handle specific exceptions first
- Log error details and context
- Implement proper retries

### 2. Failover Strategy
- Configure appropriate timeouts
- Set reasonable retry limits
- Use exponential backoff
- Monitor failover metrics

### 3. Circuit Breaking
- Set appropriate thresholds
- Monitor breaker state
- Handle recovery properly
- Log state transitions

### 4. Monitoring
- Track error rates
- Monitor latencies
- Analyze patterns
- Set up alerts

## Implementation Example

```python
from adpa.llms.resilience import (
    FailoverManager,
    CircuitBreaker,
    ErrorTracker,
    ProviderMetrics
)

class ResilientLLMClient:
    def __init__(self):
        # Initialize components
        self.failover = FailoverManager(
            primary="openai",
            secondaries=["gemini", "groq"]
        )
        self.breaker = CircuitBreaker("main_breaker")
        self.tracker = ErrorTracker()
        self.metrics = ProviderMetrics()
        
    async def generate(self, prompt: str) -> str:
        try:
            # Check circuit breaker
            if self.tracker.is_blocked:
                raise CircuitBreakerError("Circuit is open")
            
            # Try with failover
            start_time = time.time()
            result = await self.failover.execute_with_failover({
                "prompt": prompt,
                "max_tokens": 100
            })
            
            # Record success
            latency = time.time() - start_time
            self.metrics.record_success(
                latency=latency,
                tokens=result["usage"]["total_tokens"]
            )
            
            return result["text"]
            
        except Exception as e:
            # Record error
            if isinstance(e, NetworkResilienceError):
                self.metrics.record_error("network", str(e))
            elif isinstance(e, RateLimitError):
                self.metrics.record_error("rate_limit", str(e))
            else:
                self.metrics.record_error("api", str(e))
            
            # Update error tracking
            self.tracker.record_error(
                error_type=type(e).__name__,
                message=str(e)
            )
            
            raise
```

## Monitoring Dashboard

The Streamlit demo includes a comprehensive monitoring dashboard:

1. **Provider Status**
   - Real-time availability
   - Success/error rates
   - Response times

2. **Error Tracking**
   - Error history
   - Error types
   - Error patterns

3. **Circuit Breaker**
   - Current state
   - Failure counts
   - Recovery status

4. **Metrics**
   - Success rates
   - Error rates
   - Latency trends

## Next Steps
1. Review the [Performance Guide](llm-performance.md)
2. Check the [Security Guide](llm-security.md)
3. Explore the [Architecture Guide](architecture.md)
