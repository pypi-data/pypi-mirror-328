"""Unit tests for Text2SQL functionality."""
import pytest

from adpa.text2sql import Text2SQL
from adpa.text2sql.models import SchemaInfo, SQLQuery


def test_text2sql_initialization():
    """Test Text2SQL class initialization."""
    text2sql = Text2SQL()
    assert text2sql is not None


def test_query_translation():
    """Test basic query translation."""
    text2sql = Text2SQL()
    query = "Find all users"
    schema = SchemaInfo(tables=["users"], columns={"users": ["id", "name", "email"]})
    result = text2sql.translate(query, schema)
    assert isinstance(result, SQLQuery)
    assert "SELECT" in result.sql
    assert "FROM users" in result.sql


def test_schema_validation():
    """Test schema validation during translation."""
    text2sql = Text2SQL()
    query = "Find all invalid_table"
    schema = SchemaInfo(tables=["users"], columns={"users": ["id", "name", "email"]})
    with pytest.raises(ValueError):
        text2sql.translate(query, schema)


def test_query_with_conditions():
    """Test query translation with conditions."""
    text2sql = Text2SQL()
    query = "Find users who joined last month"
    schema = SchemaInfo(tables=["users"], columns={"users": ["id", "name", "email", "joined_at"]})
    result = text2sql.translate(query, schema)
    assert isinstance(result, SQLQuery)
    assert "WHERE" in result.sql
    assert "joined_at" in result.sql


def test_query_with_joins():
    """Test query translation with joins."""
    text2sql = Text2SQL()
    query = "Find all orders by user John"
    schema = SchemaInfo(
        tables=["users", "orders"],
        columns={
            "users": ["id", "name", "email"],
            "orders": ["id", "user_id", "product", "amount"],
        },
    )
    result = text2sql.translate(query, schema)
    assert isinstance(result, SQLQuery)
    assert "JOIN" in result.sql
    assert "users" in result.sql
    assert "orders" in result.sql


def test_query_optimization():
    """Test query optimization."""
    text2sql = Text2SQL()
    query = "Find the total amount spent by each user"
    schema = SchemaInfo(
        tables=["users", "orders"],
        columns={"users": ["id", "name", "email"], "orders": ["id", "user_id", "amount"]},
    )
    result = text2sql.translate(query, schema)
    assert isinstance(result, SQLQuery)
    assert "GROUP BY" in result.sql
    assert result.is_optimized


def test_error_handling():
    """Test error handling for invalid inputs."""
    text2sql = Text2SQL()

    # Test with empty query
    with pytest.raises(ValueError):
        text2sql.translate("", SchemaInfo(tables=[], columns={}))

    # Test with invalid schema
    with pytest.raises(ValueError):
        text2sql.translate("Find users", None)

    # Test with ambiguous query
    query = "Find items"  # Ambiguous if multiple tables have similar columns
    schema = SchemaInfo(
        tables=["products", "inventory"],
        columns={"products": ["id", "name", "price"], "inventory": ["id", "name", "quantity"]},
    )
    with pytest.raises(ValueError):
        text2sql.translate(query, schema)
