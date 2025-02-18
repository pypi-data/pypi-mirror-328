# Text-to-SQL Component Documentation

## Overview

The Text-to-SQL component is a core part of the ADPA Framework that translates natural language queries into SQL statements. It uses advanced NLP techniques and LLM integration to provide accurate and contextually aware SQL translations.

## Architecture

### Components

1. **Query Processor**
   - Input validation
   - Query normalization
   - Context extraction
   - Entity recognition

2. **Schema Manager**
   - Database schema loading
   - Schema validation
   - Relationship mapping
   - Type inference

3. **Translation Engine**
   - LLM integration
   - Query template matching
   - SQL generation
   - Query optimization

4. **Validation Engine**
   - Syntax validation
   - Security checks
   - Performance analysis
   - Result verification

## Usage

### Basic Query Translation

```python
from adpa.text2sql import SQLTranslator

translator = SQLTranslator()
query = "Find all users who signed up last month"

sql_query = translator.translate(query)
print(sql_query)
# Output: SELECT * FROM users WHERE signup_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
#         AND signup_date < DATE_TRUNC('month', CURRENT_DATE)
```

### Advanced Features

1. **Context-Aware Queries**
```python
translator.set_context({
    "user_role": "admin",
    "org_id": 123
})

query = "Show me all active projects"
sql_query = translator.translate(query)
# Includes role-based access and organization filtering
```

2. **Schema-Aware Translation**
```python
translator.load_schema("path/to/schema.json")
query = "List employees in the sales department"
sql_query = translator.translate(query)
# Uses correct table and column names from schema
```

## Configuration

### 1. LLM Configuration

```python
config = {
    "model": "gpt-4",
    "temperature": 0.3,
    "max_tokens": 500,
    "stop_sequences": [";", "--"]
}
translator = SQLTranslator(llm_config=config)
```

### 2. Security Settings

```python
security_config = {
    "allow_mutations": False,
    "allowed_tables": ["users", "products"],
    "blocked_keywords": ["DROP", "DELETE"],
    "max_joins": 3
}
translator = SQLTranslator(security_config=security_config)
```

## Error Handling

### 1. Translation Errors

```python
try:
    sql_query = translator.translate("some query")
except TranslationError as e:
    print(f"Translation failed: {e}")
except ValidationError as e:
    print(f"Validation failed: {e}")
except SecurityError as e:
    print(f"Security check failed: {e}")
```

### 2. Error Types

- `TranslationError`: Failed to translate query
- `ValidationError`: Generated SQL is invalid
- `SecurityError`: Query violates security rules
- `SchemaError`: Query conflicts with schema
- `ContextError`: Missing required context

## Performance Optimization

### 1. Query Optimization

```python
optimizer_config = {
    "enable_caching": True,
    "cache_size": 1000,
    "optimization_level": "medium",
    "timeout": 5.0
}
translator = SQLTranslator(optimizer_config=optimizer_config)
```

### 2. Caching

```python
from adpa.text2sql.cache import QueryCache

cache = QueryCache(max_size=1000)
translator = SQLTranslator(cache=cache)
```

## Security Best Practices

1. **Input Validation**
   - Sanitize input queries
   - Validate context data
   - Check parameter types
   - Enforce length limits

2. **Access Control**
   - Implement role-based access
   - Table-level permissions
   - Column-level security
   - Row-level security

3. **Query Restrictions**
   - Limit query complexity
   - Restrict dangerous operations
   - Set timeout limits
   - Monitor query patterns

## Monitoring

### 1. Performance Metrics

```python
from adpa.monitoring import MetricsCollector

metrics = MetricsCollector()
translator = SQLTranslator(metrics=metrics)

# Collect metrics
metrics.record_translation_time(duration)
metrics.record_query_complexity(complexity)
```

### 2. Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("text2sql")

# Log translation events
logger.info("Translation started", extra={"query": query})
logger.error("Translation failed", extra={"error": str(e)})
```

## Testing

### 1. Unit Tests

```python
def test_simple_translation():
    translator = SQLTranslator()
    query = "Find user by id 123"
    sql = translator.translate(query)
    assert "SELECT" in sql
    assert "FROM users" in sql
    assert "WHERE id = 123" in sql
```

### 2. Integration Tests

```python
def test_with_database():
    translator = SQLTranslator()
    db = Database()
    
    query = "Find active users"
    sql = translator.translate(query)
    results = db.execute(sql)
    
    assert results is not None
    assert len(results) > 0
```

## Troubleshooting

### Common Issues

1. **Poor Translation Quality**
   - Check input query clarity
   - Verify schema loading
   - Review context data
   - Check LLM configuration

2. **Performance Issues**
   - Enable query caching
   - Optimize schema loading
   - Adjust timeout settings
   - Monitor resource usage

3. **Security Violations**
   - Review security config
   - Check access controls
   - Validate input data
   - Monitor query patterns
