# Test Example: Database Agent

Version 0.7.0

## Overview
This example demonstrates how to write tests for the Database Agent component.

## Example Test

```python
import pytest
from adpa.agents import DatabaseAgent
from adpa.models import Query

def test_database_agent_query():
    """
    Test that the DatabaseAgent can execute a simple query.
    
    This test demonstrates:
    - Agent initialization
    - Query execution
    - Result validation
    """
    # Arrange
    agent = DatabaseAgent()
    test_query = Query(
        text="SELECT * FROM users LIMIT 1",
        parameters={}
    )
    
    # Act
    result = agent.execute_query(test_query)
    
    # Assert
    assert result is not None
    assert len(result) == 1
    assert "id" in result[0]

def test_database_agent_error_handling():
    """
    Test that the DatabaseAgent handles errors appropriately.
    """
    # Arrange
    agent = DatabaseAgent()
    invalid_query = Query(
        text="SELECT * FROM nonexistent_table",
        parameters={}
    )
    
    # Act & Assert
    with pytest.raises(TableNotFoundError):
        agent.execute_query(invalid_query)
```

## Running the Tests

```bash
# Run all database agent tests
pytest tests/agents/test_database_agent.py -v

# Run specific test
pytest tests/agents/test_database_agent.py::test_database_agent_query -v
```

## Key Points
- Tests follow Arrange-Act-Assert pattern
- Clear test names and docstrings
- Proper error handling testing
- Use of pytest fixtures (not shown)

## Related Examples
- [API Test Example](/docs/examples/test_api_example.md)
- [Agent Test Example](/docs/examples/test_agent_example.md)

---

## Additional Resources
- [Testing Guide](/docs/testing/index.md)
- [Database Agent Documentation](/docs/database-agent.md)

## Contributing
For contributions to examples, please see our [Contributing Guide](/docs/development.md#contributing).

## Support
If you encounter any issues or have questions, please:
1. Check our [Error Reference](/docs/errors.md)
2. Search existing [GitHub Issues](https://github.com/achimdehnert/adpa-framework/issues)
3. Create a new issue if needed

*Last updated: 2025-01-12*
