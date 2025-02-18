"""Unit tests for Text2SQL validator."""

import pytest
from typing import Dict, List, Tuple
import sqlparse
from datetime import datetime

from adpa.text2sql.validation.validator import QueryValidator
from adpa.text2sql.models.query_models import SQLQuery
from adpa.text2sql.models.exceptions import ValidationError


@pytest.fixture
def validator():
    """Fixture for query validator."""
    return QueryValidator()


@pytest.fixture
def sample_query():
    """Fixture for sample SQL query."""
    return SQLQuery(
        query="SELECT * FROM users WHERE location = 'New York'",
        natural_question="Show me users from New York",
        confidence_score=0.9,
        generated_at=datetime.utcnow()
    )


@pytest.mark.asyncio
async def test_should_validate_basic_syntax(validator, sample_query):
    """Test basic SQL syntax validation."""
    # Given/When
    is_valid, error, suggestions = await validator.validate_query(
        sample_query,
        [{"id": 1, "name": "John"}]
    )
    
    # Then
    assert is_valid
    assert error is None
    assert not suggestions


@pytest.mark.asyncio
async def test_should_detect_missing_select(validator):
    """Test detection of missing SELECT statement."""
    # Given
    query = SQLQuery(
        query="FROM users",
        natural_question="Invalid query",
        confidence_score=0.5,
        generated_at=datetime.utcnow()
    )
    
    # When
    is_valid, error, suggestions = await validator.validate_query(query, [])
    
    # Then
    assert not is_valid
    assert "Missing SQL command" in error
    assert any("SELECT" in s for s in suggestions)


@pytest.mark.asyncio
async def test_should_validate_column_references(validator):
    """Test validation of column references."""
    # Given
    query = SQLQuery(
        query="SELECT nonexistent_column FROM users",
        natural_question="Show invalid column",
        confidence_score=0.7,
        generated_at=datetime.utcnow()
    )
    
    # When
    is_valid, error, suggestions = await validator.validate_query(query, [])
    
    # Then
    assert not is_valid
    assert "column" in error.lower()
    assert suggestions


@pytest.mark.asyncio
async def test_should_validate_result_types(validator, sample_query):
    """Test validation of result data types."""
    # Given
    results = [
        {"id": 1, "name": "John"},
        {"id": "2", "name": "Jane"}  # Inconsistent id type
    ]
    
    # When
    is_valid, error, suggestions = await validator.validate_query(sample_query, results)
    
    # Then
    assert not is_valid
    assert "type" in error.lower()
    assert suggestions


@pytest.mark.asyncio
async def test_should_handle_empty_results(validator, sample_query):
    """Test handling of empty result sets."""
    # Given/When
    is_valid, error, suggestions = await validator.validate_query(sample_query, [])
    
    # Then
    assert not is_valid
    assert "no results" in error.lower()
    assert any("WHERE" in s for s in suggestions)


@pytest.mark.asyncio
async def test_should_validate_null_handling(validator, sample_query):
    """Test validation of NULL value handling."""
    # Given
    results = [
        {"id": 1, "name": None},
        {"id": 2, "name": None},
        {"id": 3, "name": None}
    ]
    
    # When
    is_valid, error, suggestions = await validator.validate_query(sample_query, results)
    
    # Then
    assert not is_valid
    assert "NULL" in error
    assert any("name" in s for s in suggestions)


@pytest.mark.asyncio
async def test_should_detect_unclosed_parentheses(validator):
    """Test detection of unclosed parentheses."""
    # Given
    query = SQLQuery(
        query="SELECT * FROM users WHERE (id > 0",
        natural_question="Show active users",
        confidence_score=0.8,
        generated_at=datetime.utcnow()
    )
    
    # When
    is_valid, error, suggestions = await validator.validate_query(query, [])
    
    # Then
    assert not is_valid
    assert "parentheses" in error.lower()
    assert any("parentheses" in s.lower() for s in suggestions)


@pytest.mark.asyncio
async def test_should_validate_complex_query(validator):
    """Test validation of complex query structure."""
    # Given
    query = SQLQuery(
        query="""
        SELECT u.name, COUNT(o.id) as order_count
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        WHERE u.status = 'active'
        GROUP BY u.name
        HAVING COUNT(o.id) > 5
        ORDER BY order_count DESC
        """,
        natural_question="Show active users with more than 5 orders",
        confidence_score=0.95,
        generated_at=datetime.utcnow()
    )
    
    # When
    is_valid, error, suggestions = await validator.validate_query(
        query,
        [{"name": "John", "order_count": 10}]
    )
    
    # Then
    assert is_valid
    assert error is None
    assert not suggestions


@pytest.mark.asyncio
async def test_should_validate_subqueries(validator):
    """Test validation of subqueries."""
    # Given
    query = SQLQuery(
        query="""
        SELECT *
        FROM users
        WHERE id IN (
            SELECT user_id
            FROM orders
            GROUP BY user_id
            HAVING COUNT(*) > 5
        )
        """,
        natural_question="Find users with more than 5 orders",
        confidence_score=0.9,
        generated_at=datetime.utcnow()
    )
    
    # When
    is_valid, error, suggestions = await validator.validate_query(
        query,
        [{"id": 1, "name": "John"}]
    )
    
    # Then
    assert is_valid
    assert error is None
    assert not suggestions
