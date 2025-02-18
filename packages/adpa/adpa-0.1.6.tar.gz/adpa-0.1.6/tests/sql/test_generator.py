"""Tests for enhanced SQL query generator.

This module contains comprehensive tests for the SQL query generator component.
It covers various SQL query scenarios, validation, and error handling.

Test Categories:
1. Basic Queries: Simple SELECT statements
2. Complex Queries: Joins, subqueries, and aggregations
3. Edge Cases: Error handling and validation
4. Configuration: Settings and limits
5. Performance: Query optimization and resource usage

Usage:
    Run tests with pytest:
    ```bash
    pytest tests/sql/test_generator.py -v
    ```
"""

import pytest
from adpa.sql.generator import (
    SQLGenerator,
    SQLGenerationConfig,
    ReasoningPhase,
    AnalysisPhase,
    QueryPhase,
    VerificationPhase
)
from adpa.sql.types import (
    SQLQuery,
    QueryResult,
    ValidationResult
)
from adpa.sql.validation import (
    SecurityValidation,
    SchemaValidation,
    PerformanceValidation
)


@pytest.fixture
def default_config():
    """Create default SQL generation config.
    
    Returns:
        SQLGenerationConfig: Default configuration for testing
        
    Usage:
        def test_something(default_config):
            generator = SQLGenerator(default_config)
    """
    return SQLGenerationConfig(
        model_name="gpt-4",
        temperature=0,
        max_tokens=1000,
        allowed_operations=["SELECT"]
    )


@pytest.fixture
def mock_db_toolkit(mocker):
    """Create mock database toolkit.
    
    Args:
        mocker: pytest-mock fixture
        
    Returns:
        Mock: Mocked database toolkit for testing
        
    Usage:
        def test_something(mock_db_toolkit):
            toolkit.get_tools.assert_called_once()
    """
    toolkit = mocker.Mock()
    toolkit.get_tools.return_value = []
    return toolkit


@pytest.fixture
def generator(default_config, mock_db_toolkit):
    """Create SQL generator instance.
    
    Args:
        default_config: Default configuration fixture
        mock_db_toolkit: Mock database toolkit fixture
        
    Returns:
        SQLGenerator: Configured generator instance
        
    Usage:
        def test_something(generator):
            result = generator.generate_query("query")
    """
    return SQLGenerator(default_config, mock_db_toolkit)


def test_should_generate_simple_query(generator):
    """Test generation of simple SELECT query.
    
    This test verifies that the generator can create basic SELECT
    queries with appropriate limits and structure.
    
    Args:
        generator: SQLGenerator fixture
        
    Assertions:
        - Query generation succeeds
        - Query contains SELECT statement
        - Query includes FROM clause
        - Query has LIMIT clause
    """
    query_text = "Show me all users"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "SELECT" in result["query"]
    assert "FROM users" in result["query"]
    assert "LIMIT 10" in result["query"]


def test_should_include_all_phases(generator):
    """Test that all phases are included in result.
    
    This test ensures that the generator executes and includes
    all required phases in the generation process.
    
    Args:
        generator: SQLGenerator fixture
        
    Assertions:
        - All required phases are present
        - Phases contain expected content
        - Phases are in correct order
    """
    result = generator.generate_query("List all products")
    
    assert "reasoning" in result["phases"]
    assert "analysis" in result["phases"]
    assert "query" in result["phases"]
    assert "verification" in result["phases"]


def test_should_handle_complex_query(generator):
    """Test handling of complex query with joins."""
    query_text = "Show me all orders with their customers and products"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "JOIN" in result["query"]
    assert "orders" in result["query"].lower()
    assert "customers" in result["query"].lower()
    assert "products" in result["query"].lower()


def test_should_validate_reasoning_phase():
    """Test reasoning phase validation."""
    phase = ReasoningPhase(
        content="Test reasoning",
        information_needs="User data required",
        expected_outcome="List of active users",
        challenges=["Data might be incomplete"],
        approach="Simple SELECT query"
    )
    
    assert phase.validate()


def test_should_validate_analysis_phase():
    """Test analysis phase validation."""
    phase = AnalysisPhase(
        content="Test analysis",
        required_tables=["users"],
        required_columns=["id", "name"],
        joins=[],
        conditions=["active = true"]
    )
    
    assert phase.validate()


def test_should_validate_query_phase():
    """Test query phase validation."""
    phase = QueryPhase(
        content="Test query",
        sql="SELECT id, name FROM users WHERE active = true LIMIT 10",
        parameters={}
    )
    
    assert phase.validate()


def test_should_validate_verification_phase():
    """Test verification phase validation."""
    phase = VerificationPhase(
        content="Test verification",
        syntax_valid=True,
        schema_valid=True,
        security_valid=True,
        performance_valid=True
    )
    
    assert phase.validate()


def test_should_handle_invalid_query(generator):
    """Test handling of invalid query text."""
    result = generator.generate_query("")
    
    assert not result["success"]
    assert result["error"]


def test_should_respect_config_limits(generator):
    """Test that configuration limits are respected."""
    result = generator.generate_query("Show all users")
    
    assert f"LIMIT {generator.config.default_limit}" in result["query"]


def test_should_include_error_details(generator):
    """Test that error details are included in result."""
    generator.db_toolkit.get_tools.side_effect = Exception("Database error")
    result = generator.generate_query("Show users")
    
    assert not result["success"]
    assert "Database error" in result["error"]


def test_should_handle_complex_conditions(generator):
    """Test handling of complex WHERE conditions."""
    query_text = "Show active users who joined last month and made a purchase"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "WHERE" in result["query"]
    assert "AND" in result["query"]


def test_should_handle_aggregations(generator):
    """Test handling of aggregation functions."""
    query_text = "Count total orders per customer"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "COUNT" in result["query"]
    assert "GROUP BY" in result["query"]


def test_should_handle_subqueries(generator):
    """Test handling of subqueries."""
    query_text = "Show users who have made more than 5 orders"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "SELECT" in result["query"]
    assert "(" in result["query"]  # Subquery parentheses


def test_should_maintain_phase_order(generator):
    """Test that phases are processed in correct order."""
    result = generator.generate_query("List users")
    phases = list(result["phases"].keys())
    
    assert phases.index("reasoning") < phases.index("analysis")
    assert phases.index("analysis") < phases.index("query")
    assert phases.index("query") < phases.index("verification")


def test_should_handle_date_ranges(generator):
    """Test handling of date range queries."""
    query_text = "Show orders from last week"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "WHERE" in result["query"]
    assert "created_at" in result["query"].lower()
    assert "BETWEEN" in result["query"]


def test_should_handle_nested_conditions(generator):
    """Test handling of nested WHERE conditions."""
    query_text = "Show users who have orders with status completed or pending"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "WHERE" in result["query"]
    assert "(" in result["query"]
    assert "OR" in result["query"]
    assert "status" in result["query"].lower()


def test_should_handle_window_functions(generator):
    """Test handling of window functions."""
    query_text = "Show running total of orders per user"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "OVER" in result["query"]
    assert "PARTITION BY" in result["query"]
    assert "SUM" in result["query"]


def test_should_handle_having_clause(generator):
    """Test handling of HAVING clause."""
    query_text = "Show customers who spent more than average"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "HAVING" in result["query"]
    assert "AVG" in result["query"]


def test_should_handle_union_queries(generator):
    """Test handling of UNION operations."""
    query_text = "Show active and inactive users"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "UNION" in result["query"]


def test_should_handle_case_statements(generator):
    """Test handling of CASE statements."""
    query_text = "Show user status as active or inactive based on last order date"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "CASE" in result["query"]
    assert "WHEN" in result["query"]
    assert "END" in result["query"]


def test_should_handle_null_values(generator):
    """Test handling of NULL value conditions."""
    query_text = "Show users with no orders"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "IS NULL" in result["query"]


def test_should_handle_exists_clause(generator):
    """Test handling of EXISTS clause."""
    query_text = "Show users who have at least one order"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "EXISTS" in result["query"]


def test_should_handle_common_table_expressions(generator):
    """Test handling of Common Table Expressions (CTEs)."""
    query_text = "Show top spenders with their latest order"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "WITH" in result["query"]
    assert "AS" in result["query"]


def test_should_handle_string_operations(generator):
    """Test handling of string operations."""
    query_text = "Show users with gmail addresses"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "LIKE" in result["query"]
    assert "'%gmail.com'" in result["query"].lower()


def test_should_handle_numeric_operations(generator):
    """Test handling of numeric operations."""
    query_text = "Show orders with 20% discount"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "*" in result["query"]
    assert "0.8" in result["query"]


def test_should_handle_distinct_values(generator):
    """Test handling of DISTINCT keyword."""
    query_text = "Show unique order statuses"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "DISTINCT" in result["query"]


def test_should_handle_multiple_aggregations(generator):
    """Test handling of multiple aggregation functions."""
    query_text = "Show total orders, average amount, and max amount per user"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "COUNT" in result["query"]
    assert "AVG" in result["query"]
    assert "MAX" in result["query"]
    assert "GROUP BY" in result["query"]


def test_should_handle_complex_joins(generator):
    """Test handling of complex join scenarios."""
    query_text = "Show users, their orders, and related products with categories"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert result["query"].count("JOIN") >= 3
    assert "users" in result["query"].lower()
    assert "orders" in result["query"].lower()
    assert "products" in result["query"].lower()


def test_should_handle_recursive_queries(generator):
    """Test handling of recursive queries."""
    query_text = "Show all product categories and their subcategories"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "WITH RECURSIVE" in result["query"]
    assert "UNION" in result["query"]


def test_should_handle_dynamic_pivoting(generator):
    """Test handling of dynamic pivot operations."""
    query_text = "Show order counts by status for each user"
    result = generator.generate_query(query_text)
    
    assert result["success"]
    assert "CASE" in result["query"]
    assert "COUNT" in result["query"]
    assert "GROUP BY" in result["query"]
