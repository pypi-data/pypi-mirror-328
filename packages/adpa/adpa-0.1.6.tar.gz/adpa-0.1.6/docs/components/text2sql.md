# Text2SQL Module

## Overview

The Text2SQL module is a core component of the ADPA Framework that converts natural language queries into valid SQL statements. It uses advanced language models and structured reasoning to generate accurate and secure SQL queries.

## Features

### 1. Query Generation
- Natural language understanding
- Structured reasoning phases
- Query validation
- Error handling

### 2. Security
- Input validation
- SQL injection prevention
- Query sanitization
- Access control

### 3. Performance
- Query optimization
- Execution planning
- Resource management
- Caching

### 4. Error Handling
- Detailed error messages
- Recovery suggestions
- Logging
- Monitoring

## Architecture

### Components

1. **Generator**
   - Natural language processing
   - Context management
   - Query construction
   - Validation

2. **Validator**
   - Syntax checking
   - Schema validation
   - Security checks
   - Performance analysis

3. **Middleware**
   - Request processing
   - Response handling
   - Error management
   - Metrics collection

## Usage

### Basic Example
```python
from adpa.sql import SQLGenerator, SQLGenerationConfig

# Configure generator
config = SQLGenerationConfig(
    model_name="gpt-4",
    temperature=0,
    max_tokens=1000
)

# Initialize generator
generator = SQLGenerator(config)

# Generate query
result = generator.generate_query(
    "Find all active users who joined last month"
)

if result["success"]:
    print(f"Generated SQL: {result['query']}")
    print(f"Phases: {result['phases']}")
else:
    print(f"Error: {result['error']}")
```

### Advanced Example
```python
from adpa.sql import SQLValidator, SecurityValidation

# Configure validator
security_config = SecurityValidation(
    allowed_operations={"SELECT"},
    max_joins=5,
    max_conditions=10
)

# Initialize validator
validator = SQLValidator(engine, security_config)

# Validate query
result = validator.validate_query(sql)

if result.valid:
    print("Query is valid")
    print(f"Suggestions: {result.suggestions}")
else:
    print(f"Errors: {result.errors}")
    print(f"Warnings: {result.warnings}")
```

## Configuration

### Generator Configuration
```python
SQLGenerationConfig(
    model_name="gpt-4",
    temperature=0,
    max_tokens=1000,
    allowed_operations=["SELECT"],
    default_limit=10
)
```

### Validator Configuration
```python
SecurityValidation(
    allowed_operations={"SELECT"},
    blocked_keywords={"DROP", "DELETE", "TRUNCATE"},
    max_joins=5,
    max_conditions=10
)

SchemaValidation(
    required_tables={"users", "orders"},
    max_columns=20,
    enforce_schema=True
)

PerformanceValidation(
    max_rows=1000,
    timeout_seconds=30,
    min_index_usage=0.5
)
```

## Best Practices

1. **Security**
   - Always validate input
   - Use parameterized queries
   - Limit query complexity
   - Monitor query patterns

2. **Performance**
   - Use appropriate indexes
   - Limit result sets
   - Monitor execution time
   - Cache common queries

3. **Error Handling**
   - Provide clear messages
   - Log all errors
   - Include context
   - Suggest solutions

4. **Maintenance**
   - Monitor usage patterns
   - Update configurations
   - Review performance
   - Update documentation

## Common Issues

### 1. Query Generation
- Complex queries
- Ambiguous input
- Missing context
- Invalid syntax

### 2. Performance
- Slow queries
- Resource usage
- Memory limits
- Timeouts

### 3. Security
- Injection attempts
- Invalid access
- Resource abuse
- Data exposure

## Future Development

1. **Enhanced Features**
   - Multi-database support
   - Complex query patterns
   - Natural language improvements
   - Performance optimization

2. **Security**
   - Advanced validation
   - Threat detection
   - Access patterns
   - Audit logging

3. **Integration**
   - External services
   - Custom databases
   - Monitoring tools
   - Analytics systems
