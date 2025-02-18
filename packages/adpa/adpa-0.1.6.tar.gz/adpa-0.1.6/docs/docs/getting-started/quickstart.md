# Quick Start Guide

## Basic Usage

### 1. Text2SQL Example

```python
from adpa import Text2SQL
from adpa.text2sql.models import SchemaInfo

# Define your database schema
schema = SchemaInfo(
    tables=["users", "orders"],
    columns={
        "users": ["id", "name", "email", "joined_at"],
        "orders": ["id", "user_id", "product", "amount", "created_at"]
    }
)

# Initialize Text2SQL
text2sql = Text2SQL()

# Convert natural language to SQL
query = "Find all users who ordered more than $100 worth of products last month"
result = text2sql.translate(query, schema)

print(result.sql)
```

### 2. Agent Configuration

```python
from adpa.agents import Agent
from adpa.agents.models import AgentConfig

# Configure an agent
config = AgentConfig(
    name="research_assistant",
    type="research",
    team="Research Team",
    description="Specialized in research and analysis tasks",
    tools=["web_search", "document_analysis", "summarization"],
    llm_config={
        "primary_provider": "OpenAI",
        "model": "gpt-4"
    },
    max_concurrent_tasks=5,
    timeout=300
)

# Create and use the agent
agent = Agent(config)
result = agent.execute_task({
    "type": "research",
    "description": "Research latest AI developments"
})
```

### 3. UI Components

```python
import streamlit as st
from adpa.ui import AgentManager, QueryBuilder

# Initialize components
agent_manager = AgentManager()
query_builder = QueryBuilder()

# Create Streamlit app
st.title("ADPA Demo")

# Add agent management UI
with st.expander("Agent Management"):
    agent_manager.render()

# Add query builder
query = query_builder.render()
if query:
    st.write("Generated SQL:", query)
```

## Configuration

### Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
POSTGRES_URI=postgresql://user:pass@localhost:5432/db
```

### Load Configuration

```python
from adpa.config import load_config

config = load_config()
```

## Next Steps

- [Configuration Guide](configuration.md) for detailed setup
- [API Reference](../api/core.md) for complete API documentation
- [Examples](../examples/basic.md) for more usage examples
