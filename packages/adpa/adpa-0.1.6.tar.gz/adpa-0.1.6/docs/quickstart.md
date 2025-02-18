# Quick Start Guide

This guide will help you get started with ADPA (Advanced Data Processing and Analysis Framework) quickly.

## Installation

```bash
pip install adpa
```

## Basic Usage

### 1. Text to SQL Conversion

```python
from adpa.text2sql import Text2SQLConverter

# Initialize the converter
converter = Text2SQLConverter()

# Convert natural language to SQL
query = "Find all users who joined after 2024"
sql = converter.convert(query)
print(sql)
# Output: SELECT * FROM users WHERE joined_at > '2024-01-01'
```

### 2. Using Agents

```python
from adpa.agents import AgentSystem
from adpa.agents.types import Task

# Initialize the agent system
agent_system = AgentSystem()

# Create a task
task = Task(
    description="Analyze user activity patterns",
    data={"timeframe": "last_week"}
)

# Execute task
result = agent_system.execute_task(task)
print(result.summary)
```

### 3. LLM Integration

```python
from adpa.llms import LLMManager
from adpa.llms.config import LLMConfig

# Configure LLM
config = LLMConfig(
    provider="openai",
    model="gpt-4"
)

# Initialize LLM manager
llm = LLMManager(config)

# Generate text
response = llm.generate("Explain how databases work")
print(response)
```

### 4. Database Operations

```python
from adpa.database import DatabaseManager
from adpa.database.config import DBConfig

# Configure database connection
config = DBConfig(
    host="localhost",
    port=5432,
    database="mydb",
    username="user",
    password="pass"
)

# Initialize database manager
db = DatabaseManager(config)

# Execute query
results = db.execute_query("SELECT * FROM users LIMIT 5")
for row in results:
    print(row)
```

## Advanced Features

### 1. Monitoring

```python
from adpa.monitoring import Monitor

# Initialize monitoring
monitor = Monitor()

# Start monitoring
with monitor.track("my_operation"):
    # Your code here
    pass

# Get metrics
metrics = monitor.get_metrics()
print(metrics)
```

### 2. Security

```python
from adpa.security import SecurityManager
from adpa.security.auth import AuthConfig

# Configure security
config = AuthConfig(
    jwt_secret="your-secret",
    token_expiry=3600
)

# Initialize security manager
security = SecurityManager(config)

# Authenticate user
token = security.authenticate("username", "password")
```

## Configuration

Create a `.env` file in your project root:

```env
OPENAI_API_KEY=your-api-key
POSTGRES_URI=postgresql://user:pass@localhost:5432/db
```

Then in your code:

```python
from adpa import load_config

# Load configuration
config = load_config()
```

## Best Practices

1. Always use environment variables for sensitive data
2. Implement proper error handling
3. Use the monitoring system for production deployments
4. Regularly backup your database
5. Keep your dependencies up to date

## Common Patterns

### 1. Chaining Operations

```python
from adpa.core import Pipeline

# Create a processing pipeline
pipeline = Pipeline([
    Text2SQLConverter(),
    DatabaseManager(),
    DataAnalyzer()
])

# Process data
result = pipeline.process("Find monthly sales trends")
```

### 2. Error Handling

```python
from adpa.core.errors import ADPAError

try:
    result = converter.convert("complex query")
except ADPAError as e:
    print(f"Error: {e.message}")
    print(f"Suggestion: {e.suggestion}")
```

## Next Steps

- Read the [full documentation](https://adpa.readthedocs.io)
- Check out [example projects](https://github.com/achimdehnert/adpa/tree/main/examples)
- Join our [community](https://github.com/achimdehnert/adpa/discussions)
- Report [issues](https://github.com/achimdehnert/adpa/issues)

## Getting Help

- Documentation: [https://adpa.readthedocs.io](https://adpa.readthedocs.io)
- GitHub Issues: [https://github.com/achimdehnert/adpa/issues](https://github.com/achimdehnert/adpa/issues)
- Stack Overflow: Tag your questions with `adpa`
