# Text-to-SQL Agent API Reference

## Overview
Documentation for the agent-based components of the Text-to-SQL module.

## Base Agent

### BaseTextToSQLAgent

```python
class BaseTextToSQLAgent:
    def __init__(
        self,
        config: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> None:
        """Initialize base agent.

        Args:
            config: Agent configuration
            context: Optional context data
        """

    async def process(
        self,
        input_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Process input data.

        Args:
            input_data: Data to process

        Returns:
            Dict containing processed results

        Raises:
            AgentError: If processing fails
        """

    async def update_context(
        self,
        context: Dict[str, Any]
    ) -> None:
        """Update agent context.

        Args:
            context: New context data
        """
```

## Specialized Agents

### NLPAgent

Natural language processing and understanding agent.

```python
class NLPAgent(BaseTextToSQLAgent):
    async def extract_intent(
        self,
        query: str
    ) -> Dict[str, Any]:
        """Extract intent from natural language query.

        Args:
            query: Natural language query

        Returns:
            Dict containing:
                - intent: Query intent
                - entities: Extracted entities
                - confidence: Confidence score
        """

    async def enhance_query(
        self,
        query: str,
        context: Dict[str, Any]
    ) -> str:
        """Enhance query with context.

        Args:
            query: Original query
            context: Context information

        Returns:
            Enhanced query
        """
```

### OptimizerAgent

Query optimization and performance tuning agent.

```python
class OptimizerAgent(BaseTextToSQLAgent):
    async def optimize_query(
        self,
        query: str,
        schema: Dict[str, Any]
    ) -> Tuple[str, List[str]]:
        """Optimize SQL query.

        Args:
            query: SQL query to optimize
            schema: Database schema

        Returns:
            Tuple of:
                - Optimized query
                - List of optimization notes
        """

    async def suggest_indexes(
        self,
        query: str,
        schema: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Suggest indexes for query.

        Args:
            query: SQL query
            schema: Database schema

        Returns:
            List of suggested indexes with:
                - table: Table name
                - columns: Column list
                - type: Index type
                - reason: Justification
        """
```

### SecurityAgent

Security and compliance checking agent.

```python
class SecurityAgent(BaseTextToSQLAgent):
    async def check_security(
        self,
        query: str,
        context: Dict[str, Any]
    ) -> SecurityResult:
        """Check query security.

        Args:
            query: SQL query
            context: Security context

        Returns:
            SecurityResult with:
                - is_safe: Boolean
                - issues: List of issues
                - risk_level: Risk assessment
        """

    async def sanitize_query(
        self,
        query: str
    ) -> str:
        """Sanitize SQL query.

        Args:
            query: Query to sanitize

        Returns:
            Sanitized query
        """
```

### MonitorAgent

System monitoring and metrics collection agent.

```python
class MonitorAgent(BaseTextToSQLAgent):
    async def collect_metrics(
        self
    ) -> Dict[str, Any]:
        """Collect system metrics.

        Returns:
            Dict containing:
                - cpu_usage: CPU metrics
                - memory_usage: Memory metrics
                - query_stats: Query statistics
                - latency: Response times
        """

    async def detect_anomalies(
        self,
        metrics: Dict[str, Any]
    ) -> List[AnomalyReport]:
        """Detect system anomalies.

        Args:
            metrics: System metrics

        Returns:
            List of anomaly reports
        """
```

## Models

### SecurityResult

```python
class SecurityResult(BaseModel):
    is_safe: bool
    issues: List[SecurityIssue] = Field(default_factory=list)
    risk_level: RiskLevel
    timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        frozen = True
```

### AnomalyReport

```python
class AnomalyReport(BaseModel):
    type: AnomalyType
    severity: SeverityLevel
    description: str
    metrics: Dict[str, float]
    timestamp: datetime = Field(default_factory=datetime.now)
    suggested_actions: List[str] = Field(default_factory=list)

    class Config:
        frozen = True
```

## Constants

### Configuration Defaults

```python
DEFAULT_AGENT_CONFIG = {
    "batch_size": 100,
    "timeout_seconds": 30,
    "retry_attempts": 3,
    "cache_ttl": 3600
}
```

### Security Levels

```python
RISK_LEVELS = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}
```

## Error Types

### AgentError

```python
class AgentError(Exception):
    """Base error for agent operations."""
    pass
```

### ProcessingError

```python
class ProcessingError(AgentError):
    """Raised when processing fails."""
    pass
```

### SecurityError

```python
class SecurityError(AgentError):
    """Raised for security violations."""
    pass
```

## Best Practices

### 1. Error Handling

- Always use appropriate error types
- Include error context
- Log error details
- Implement retry logic

### 2. Performance

- Use connection pooling
- Implement caching
- Process in batches
- Monitor resource usage

### 3. Security

- Validate all input
- Sanitize queries
- Use prepared statements
- Implement access control

## Examples

### Basic Usage

```python
# Initialize agents
nlp_agent = NLPAgent(config)
optimizer_agent = OptimizerAgent(config)
security_agent = SecurityAgent(config)

# Process query
intent = await nlp_agent.extract_intent(query)
optimized_query = await optimizer_agent.optimize_query(intent["sql"])
security_result = await security_agent.check_security(optimized_query)

if security_result.is_safe:
    # Execute query
    pass
```

### Advanced Usage

```python
# Initialize monitor
monitor = MonitorAgent(config)

# Start monitoring
async def monitor_system():
    while True:
        metrics = await monitor.collect_metrics()
        anomalies = await monitor.detect_anomalies(metrics)
        
        for anomaly in anomalies:
            if anomaly.severity >= SeverityLevel.HIGH:
                await handle_anomaly(anomaly)
        
        await asyncio.sleep(60)
