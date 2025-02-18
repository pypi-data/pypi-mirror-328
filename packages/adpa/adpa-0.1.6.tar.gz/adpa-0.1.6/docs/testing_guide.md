# ADPA Framework Testing Guide

## Overview

The ADPA Framework implements a comprehensive testing strategy using both pytest for unit testing and Robot Framework for end-to-end testing. This guide explains how to run tests, add new tests, and understand test results.

## Prerequisites

- Python 3.8+
- pytest 7.0+
- Robot Framework 6.0+
- Database instance for integration tests

## Installation

```bash
pip install pytest
pip install robotframework
pip install robotframework-databaselibrary
pip install robotframework-requests
```

## Running Tests

### Unit Tests

Run all unit tests:
```bash
pytest tests/unit
```

Run specific test file:
```bash
pytest tests/unit/text2sql/test_validator.py
```

Run tests with coverage:
```bash
pytest --cov=adpa tests/unit
```

### Robot Framework Tests

Run all Robot Framework tests:
```bash
robot tests/robot
```

Run specific test suite:
```bash
robot tests/robot/text2sql/end_to_end_tests.robot
```

Run tests with tags:
```bash
robot --include smoke tests/robot
```

## Test Structure

### Unit Tests

```
tests/unit/
├── text2sql/
│   ├── test_validator.py
│   ├── test_context_manager.py
│   └── test_feedback_processor.py
└── ...
```

### Robot Framework Tests

```
tests/robot/
├── resources/
│   ├── common.robot
│   └── text2sql_common.robot
├── libraries/
│   └── Text2SQLLibrary.py
└── text2sql/
    ├── basic_queries.robot
    ├── advanced_queries.robot
    ├── feedback_loop.robot
    └── end_to_end_tests.robot
```

## Writing Tests

### Unit Test Guidelines

1. Use descriptive test names with format `test_should_*`
2. Keep tests focused and small
3. Use appropriate fixtures
4. Include error cases
5. Test edge cases
6. Add proper documentation

Example:
```python
@pytest.mark.asyncio
async def test_should_validate_complex_query(validator):
    """Test validation of complex query structure."""
    # Given
    query = SQLQuery(
        query="SELECT * FROM users WHERE id > 0",
        natural_question="Show active users",
        confidence_score=0.9
    )
    
    # When
    is_valid, error = await validator.validate_query(query)
    
    # Then
    assert is_valid
    assert error is None
```

### Robot Framework Test Guidelines

1. Use Gherkin-style syntax
2. Include proper documentation
3. Use appropriate tags
4. Create reusable keywords
5. Follow the Given-When-Then pattern

Example:
```robotframework
*** Test Cases ***
Test Should Convert Simple Question To Valid SQL
    [Tags]    smoke    critical    conversion
    [Documentation]    Test basic natural language to SQL conversion
    Given Clean Database Environment
    When User Asks "Show me all users"
    Then SQL Should Be Generated
    And Query Should Execute Successfully
```

## Test Categories

### Smoke Tests
Basic functionality tests tagged with `smoke`

### Integration Tests
Tests that verify component interaction tagged with `integration`

### Performance Tests
Tests that verify system performance tagged with `performance`

### Security Tests
Tests that verify security measures tagged with `security`

## Continuous Integration

Tests are automatically run on:
- Pull request creation
- Push to main branch
- Daily scheduled runs

### CI Pipeline Steps
1. Setup test environment
2. Run unit tests
3. Run integration tests
4. Generate coverage report
5. Run Robot Framework tests
6. Generate test reports

## Test Reports

### Unit Test Reports
- Coverage reports in HTML format
- JUnit XML reports for CI integration

### Robot Framework Reports
- Detailed HTML reports
- Log files
- XML output for CI integration

## Best Practices

1. **Test Independence**
   - Tests should not depend on each other
   - Clean up test data after each test

2. **Test Data Management**
   - Use fixtures for common test data
   - Clean up test databases between runs

3. **Error Handling**
   - Test both success and failure cases
   - Verify error messages and codes

4. **Performance**
   - Include performance assertions where relevant
   - Monitor test execution time

5. **Documentation**
   - Document test purpose and requirements
   - Include examples in documentation

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Verify database is running
   - Check connection strings
   - Ensure proper permissions

2. **Test Timeouts**
   - Adjust timeout settings
   - Check system resources
   - Verify test data size

3. **Failed Assertions**
   - Check test data setup
   - Verify expected values
   - Review test logs

## Contributing

When adding new tests:
1. Follow existing test patterns
2. Add appropriate documentation
3. Include both positive and negative cases
4. Add performance considerations
5. Update test documentation

## Version History

### v1.1.0 (2025-02-03)
- Added comprehensive Robot Framework tests
- Enhanced unit test coverage
- Improved test documentation
- Added performance testing
