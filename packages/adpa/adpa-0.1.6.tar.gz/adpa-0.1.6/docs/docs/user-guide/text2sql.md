# Text2SQL Guide

## Overview

The Text2SQL module converts natural language queries into SQL statements. It supports complex queries, joins, aggregations, and parameterization.

## Basic Usage

### Simple Queries

```python
from adpa import Text2SQL
from adpa.text2sql.models import SchemaInfo

# Define schema
schema = SchemaInfo(
    tables=["users"],
    columns={
        "users": ["id", "name", "email"]
    }
)

# Initialize
text2sql = Text2SQL()

# Convert query
result = text2sql.translate("Find all users", schema)
print(result.sql)  # SELECT * FROM users
```

### Complex Queries

```python
# Define complex schema
schema = SchemaInfo(
    tables=["users", "orders", "products"],
    columns={
        "users": ["id", "name", "email"],
        "orders": ["id", "user_id", "product_id", "amount"],
        "products": ["id", "name", "price", "category"]
    },
    relationships=[
        ("orders.user_id", "users.id"),
        ("orders.product_id", "products.id")
    ]
)

# Query with joins
query = """
Find all users who bought products
in the Electronics category with
total amount greater than $1000
"""

result = text2sql.translate(query, schema)
print(result.sql)
"""
SELECT DISTINCT u.*
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN products p ON o.product_id = p.id
WHERE p.category = 'Electronics'
GROUP BY u.id
HAVING SUM(o.amount) > 1000
"""
```

## Advanced Features

### Query Parameters

```python
# Parameterized query
query = "Find users who joined after $date"
params = {"date": "2024-01-01"}

result = text2sql.translate(query, schema, params)
print(result.sql)  # SELECT * FROM users WHERE joined_at > :date
print(result.params)  # {'date': '2024-01-01'}
```

### Query Templates

```python
from adpa.text2sql.templates import QueryTemplate

# Define template
template = QueryTemplate(
    name="users_by_criteria",
    pattern="Find users where {criteria}",
    sql_template="SELECT * FROM users WHERE {conditions}"
)

# Register template
text2sql.register_template(template)

# Use template
result = text2sql.translate(
    "Find users where age > 25 and city = 'New York'",
    schema
)
```

### Query Optimization

```python
# Enable optimization
text2sql.set_optimization_level("high")

# Optimize specific query
result = text2sql.translate(query, schema)
optimized = text2sql.optimize_query(result.sql)

print("Original:", result.sql)
print("Optimized:", optimized.sql)
```

## Schema Management

### Schema Definition

```python
from adpa.text2sql.models import (
    SchemaInfo,
    TableInfo,
    ColumnInfo,
    Relationship
)

# Detailed schema
schema = SchemaInfo(
    tables=["users", "orders"],
    columns={
        "users": [
            ColumnInfo(
                name="id",
                type="integer",
                primary_key=True
            ),
            ColumnInfo(
                name="email",
                type="string",
                unique=True
            )
        ],
        "orders": [
            ColumnInfo(
                name="id",
                type="integer",
                primary_key=True
            ),
            ColumnInfo(
                name="user_id",
                type="integer",
                foreign_key="users.id"
            )
        ]
    },
    relationships=[
        Relationship(
            from_="orders.user_id",
            to="users.id",
            type="many_to_one"
        )
    ]
)
```

### Schema Validation

```python
# Validate schema
validation_result = text2sql.validate_schema(schema)
if not validation_result.is_valid:
    print("Schema errors:", validation_result.errors)

# Auto-fix schema issues
fixed_schema = text2sql.fix_schema(schema)
```

## Error Handling

### Query Validation

```python
try:
    result = text2sql.translate(query, schema)
except QueryParseError as e:
    print("Parse error:", e.message)
    print("Suggestion:", e.suggestion)
except SchemaError as e:
    print("Schema error:", e.message)
    print("Missing tables:", e.missing_tables)
except SQLGenerationError as e:
    print("Generation error:", e.message)
    print("Partial SQL:", e.partial_sql)
```

### Custom Error Handling

```python
from adpa.text2sql.errors import ErrorHandler

class CustomErrorHandler(ErrorHandler):
    def handle_parse_error(self, error):
        # Custom handling
        pass

    def handle_schema_error(self, error):
        # Custom handling
        pass

text2sql.set_error_handler(CustomErrorHandler())
```

## Best Practices

1. Schema Design
   - Use clear table and column names
   - Define relationships explicitly
   - Include column types
   - Document schema changes

2. Query Writing
   - Be specific in natural language
   - Include relevant conditions
   - Use appropriate parameters
   - Consider query complexity

3. Performance
   - Enable query optimization
   - Use parameterized queries
   - Cache frequent queries
   - Monitor query execution time

4. Error Handling
   - Validate input queries
   - Check schema consistency
   - Handle all error types
   - Provide helpful error messages
