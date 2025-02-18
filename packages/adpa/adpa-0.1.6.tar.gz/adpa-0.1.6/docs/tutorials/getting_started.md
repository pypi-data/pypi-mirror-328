# Getting Started with ADPA

## Installation

1. Install ADPA using pip:
```bash
pip install adpa
```

2. Create a new project:
```bash
mkdir myproject
cd myproject
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install development dependencies:
```bash
pip install "adpa[dev]"
```

## Basic Usage

### 1. Core Processing

```python
from adpa.core import CoreManager
from adpa.core.types import CoreConfig

# Create configuration
config = CoreConfig(
    max_threads=2,
    queue_size=100,
    batch_size=10
)

# Initialize manager
manager = CoreManager(config)

# Process request
request = {
    "type": "example",
    "data": {"value": 42}
}

result = await manager.process_request(request)
print(result.data)  # {"value": 42}
```

### 2. Text2SQL Generation

```python
from adpa.text2sql import SQLGenerator
from adpa.text2sql.types import GeneratorConfig

# Create generator
generator = SQLGenerator(GeneratorConfig(
    model="gpt-4",
    temperature=0.7
))

# Define schema
schema = {
    "users": {
        "columns": ["id", "name", "email"],
        "types": ["integer", "text", "text"]
    }
}

# Generate query
text = "Find all users with gmail addresses"
result = await generator.generate_query(text, schema)

print(result.query)
# SELECT * FROM users WHERE email LIKE '%@gmail.com'
```

### 3. Agent System

```python
from adpa.agents import AgentManager
from adpa.agents.types import AgentConfig

# Create manager
manager = AgentManager(AgentConfig(
    max_agents=5,
    timeout=30
))

# Deploy agent
agent = await manager.deploy_agent(
    agent_type="processor",
    config={
        "name": "example_agent",
        "tasks": ["data_processing"]
    }
)

# List agents
agents = await manager.list_agents(status="running")
```

### 4. Monitoring

```python
from adpa.monitoring import MetricsCollector
from adpa.monitoring.types import CollectorConfig

# Create collector
collector = MetricsCollector(CollectorConfig(
    interval=60,
    retention_days=7
))

# Collect metrics
metrics = await collector.collect_metrics([
    "cpu_usage",
    "memory_usage",
    "request_count"
])

print(metrics)
```

### 5. Security

```python
from adpa.security import SecurityManager
from adpa.security.types import SecurityConfig

# Create manager
security = SecurityManager(SecurityConfig(
    max_login_attempts=3,
    session_timeout=3600
))

# Generate token
token = await security.generate_token(
    user_id="user123",
    scopes=["read", "write"]
)

# Validate request
result = await security.validate_request(request)
if result.valid:
    # Process request
    pass
```

## Best Practices

### 1. Error Handling

```python
from adpa.core.errors import ProcessingError

try:
    result = await manager.process_request(request)
except ProcessingError as e:
    print(f"Processing failed: {e}")
except ValueError as e:
    print(f"Invalid request: {e}")
```

### 2. Configuration

```python
from adpa.utils import load_config, validate_config

# Load configuration
config = load_config("config.yaml")

# Validate configuration
if validate_config(config, schema):
    manager = CoreManager(config)
```

### 3. Async Usage

```python
import asyncio
from adpa.core import CoreManager

async def main():
    manager = CoreManager(config)
    
    # Process multiple requests
    tasks = [
        manager.process_request(request1),
        manager.process_request(request2)
    ]
    
    results = await asyncio.gather(*tasks)

asyncio.run(main())
```

### 4. Batch Processing

```python
from adpa.utils import process_batch

async def process_items(items):
    results = await process_batch(
        items,
        batch_size=100,
        processor=process_item
    )
    return results
```

## Next Steps

1. Check out the [API Reference](../api/reference.md) for detailed documentation
2. Read the [Development Guidelines](../development/guidelines.md)
3. See [Examples](../examples/) for more use cases
4. Join our [Community](https://github.com/yourusername/adpa/discussions)
