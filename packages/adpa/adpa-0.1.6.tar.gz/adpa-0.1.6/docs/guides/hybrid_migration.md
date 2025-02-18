# Migrating to Hybrid Text-to-SQL Architecture

## Overview
This guide explains how to migrate from the traditional object-oriented Text-to-SQL implementation to the new hybrid architecture that combines OOP and agent-based components.

## Architecture Changes

### Traditional Architecture (Legacy)

```
adpa/text2sql/legacy_v1/
├── engine.py          # Monolithic conversion engine
├── validator.py       # Basic query validation
└── utils.py          # Utility functions
```

### New Hybrid Architecture

```
adpa/text2sql/
├── core/             # OOP Components
│   ├── database.py   # Database operations
│   └── validator.py  # Query validation
├── agents/           # Agent Components
│   ├── nlp_agent.py      # Natural language processing
│   ├── optimizer_agent.py # Query optimization
│   ├── security_agent.py  # Security checks
│   └── monitor_agent.py   # System monitoring
└── hybrid/
    └── coordinator.py     # Component orchestration
```

## Migration Steps

### 1. Preparation
1. Back up your existing implementation
2. Review current code dependencies
3. Document custom modifications
4. Identify critical functionality

### 2. Core Components Migration
1. Move database operations to `core/database.py`
2. Enhance validation in `core/validator.py`
3. Update import statements
4. Run tests to verify functionality

### 3. Agent Integration

```python
# Initialize required agents
from adpa.text2sql.agents import NLPAgent, OptimizerAgent, SecurityAgent, MonitorAgent

nlp_agent = NLPAgent(model="default")
optimizer = OptimizerAgent(rules={"max_joins": 3})
security = SecurityAgent(checks=["sql_injection", "access_control"])
monitor = MonitorAgent(metrics=["latency", "success_rate"])

# Create coordinator
from adpa.text2sql.hybrid import Coordinator

coordinator = Coordinator(
    agents={
        "nlp": nlp_agent,
        "optimizer": optimizer,
        "security": security,
        "monitor": monitor
    }
)
```

### 4. Configuration Updates

```python
# Update configuration
config = {
    "agents": {
        "nlp": {
            "model": "default",
            "device": "cpu"
        },
        "optimizer": {
            "rules": {"max_joins": 3}
        },
        "security": {
            "checks": ["sql_injection", "access_control"]
        },
        "monitor": {
            "metrics": ["latency", "success_rate"]
        }
    },
    "coordinator": {
        "timeout": 30,
        "max_retries": 3
    }
}
```

### 5. Code Updates

```python
# Old code
from adpa.text2sql.legacy_v1 import TextToSQLEngine

engine = TextToSQLEngine()
result = engine.convert("Show all employees")

# New code
from adpa.text2sql.hybrid import HybridEngine

engine = HybridEngine(config)
result = await engine.convert("Show all employees")
```

## Testing

### 1. Unit Tests

```python
# Test agent functionality
def test_nlp_agent():
    agent = NLPAgent()
    result = agent.process("Show all employees")
    assert "intent" in result
    assert "entities" in result

# Test coordinator
def test_coordinator():
    coordinator = Coordinator(agents={...})
    result = coordinator.process("Show all employees")
    assert result.success
```

### 2. Integration Tests

```python
# Test full pipeline
async def test_conversion():
    engine = HybridEngine(config)
    result = await engine.convert("Show all employees")
    assert result.sql == "SELECT * FROM employees"
```

## Performance Monitoring

### 1. Metrics Collection

```python
# Monitor performance
metrics = monitor.get_metrics()
print(f"Average latency: {metrics['avg_latency']}ms")
print(f"Success rate: {metrics['success_rate']}%")
```

### 2. Error Handling

```python
try:
    result = await engine.convert("Show all employees")
except AgentError as e:
    print(f"Agent error: {e}")
except CoordinatorError as e:
    print(f"Coordination error: {e}")
```

## Best Practices

### Performance
- Use async operations where possible
- Implement caching for frequent queries
- Monitor agent performance
- Optimize resource usage
- Configure timeouts appropriately

### Security
- Enable all security checks
- Validate all inputs
- Monitor for suspicious patterns
- Implement rate limiting
- Log security events

### Maintenance
- Keep agents updated
- Monitor system health
- Regular performance reviews
- Update configurations
- Maintain documentation

## Resources
- [API Documentation](../api/text2sql_agents.md)
- [Security Guide](security_guide.md)
- [Performance Guide](performance_guide.md)
- [Example Code](../examples/text2sql/)
