# Basic Examples

## Text2SQL Examples

### Simple Queries

```python
from adpa import Text2SQL
from adpa.text2sql.models import SchemaInfo

# Define schema
schema = SchemaInfo(
    tables=["users"],
    columns={
        "users": ["id", "name", "email", "created_at"]
    }
)

# Initialize
text2sql = Text2SQL()

# Simple query
result = text2sql.translate("Find all users", schema)
print(result.sql)  # SELECT * FROM users

# Query with condition
result = text2sql.translate("Find users who joined today", schema)
print(result.sql)  # SELECT * FROM users WHERE DATE(created_at) = CURRENT_DATE
```

### Complex Queries

```python
# Define more complex schema
schema = SchemaInfo(
    tables=["users", "orders", "products"],
    columns={
        "users": ["id", "name", "email"],
        "orders": ["id", "user_id", "product_id", "quantity", "created_at"],
        "products": ["id", "name", "price", "category"]
    }
)

# Query with joins
query = "Find all users who bought products in the Electronics category"
result = text2sql.translate(query, schema)
print(result.sql)
"""
SELECT DISTINCT users.*
FROM users
JOIN orders ON users.id = orders.user_id
JOIN products ON orders.product_id = products.id
WHERE products.category = 'Electronics'
"""

# Aggregation query
query = "Show total spending by each user"
result = text2sql.translate(query, schema)
print(result.sql)
"""
SELECT users.name, SUM(products.price * orders.quantity) as total_spent
FROM users
JOIN orders ON users.id = orders.user_id
JOIN products ON orders.product_id = products.id
GROUP BY users.id, users.name
ORDER BY total_spent DESC
"""
```

## Agent Examples

### Research Agent

```python
from adpa.agents import Agent
from adpa.agents.models import AgentConfig, Task

# Configure research agent
config = AgentConfig(
    name="research_assistant",
    type="research",
    team="Research Team",
    description="Specialized in research and analysis",
    tools=["web_search", "document_analysis", "summarization"],
    llm_config={
        "primary_provider": "OpenAI",
        "model": "gpt-4"
    }
)

# Create agent
agent = Agent(config)

# Create research task
task = Task(
    id="task_1",
    type="research",
    description="Research latest developments in AI",
    priority=1
)

# Execute task
result = agent.execute_task(task)
print(result.summary)
```

### Development Agent

```python
# Configure development agent
config = AgentConfig(
    name="code_assistant",
    type="development",
    team="Engineering Team",
    description="Specialized in code analysis and generation",
    tools=["code_analysis", "code_generation", "test_generation"],
    llm_config={
        "primary_provider": "OpenAI",
        "model": "gpt-4"
    }
)

agent = Agent(config)

# Code review task
task = Task(
    id="review_1",
    type="code_review",
    description="Review pull request #123",
    priority=2
)

result = agent.execute_task(task)
print(result.review_comments)
```

## UI Examples

### Agent Management UI

```python
import streamlit as st
from adpa.ui import AgentManager

def main():
    st.title("Agent Management")

    # Initialize agent manager
    manager = AgentManager()

    # Add new agent section
    with st.expander("Add New Agent"):
        manager.render_add_form()

    # Display existing agents
    st.header("Existing Agents")
    manager.render_agent_list()

    # Display agent metrics
    st.header("Agent Metrics")
    manager.render_metrics()

if __name__ == "__main__":
    main()
```

### Query Builder UI

```python
import streamlit as st
from adpa.ui import QueryBuilder
from adpa.text2sql.models import SchemaInfo

def main():
    st.title("SQL Query Builder")

    # Define schema
    schema = SchemaInfo(
        tables=["users", "orders"],
        columns={
            "users": ["id", "name", "email"],
            "orders": ["id", "user_id", "amount"]
        }
    )

    # Initialize query builder
    builder = QueryBuilder(schema)

    # Render query interface
    query = builder.render()

    if query:
        st.write("Generated SQL:", query)

        # Execute query button
        if st.button("Execute Query"):
            results = builder.execute_query(query)
            st.dataframe(results)

if __name__ == "__main__":
    main()
```
