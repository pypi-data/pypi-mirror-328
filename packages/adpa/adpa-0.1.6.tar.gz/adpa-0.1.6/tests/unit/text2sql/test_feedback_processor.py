"""Unit tests for Text2SQL feedback processor."""

import pytest
from datetime import datetime
from typing import Dict, List
from unittest.mock import Mock, patch

from adpa.text2sql.core.feedback_processor import Text2SQLFeedbackProcessor
from adpa.text2sql.models.query_models import SQLQuery, QueryContext, QueryResult, QueryMetrics
from adpa.text2sql.models.exceptions import MaxAttemptsExceeded, ValidationError


@pytest.fixture
def mock_llm_client():
    """Fixture for mocked LLM client."""
    client = Mock()
    client.generate_sql.return_value = {
        "sql": "SELECT * FROM users WHERE location = 'New York'",
        "confidence": 0.9
    }
    return client


@pytest.fixture
def mock_db_client():
    """Fixture for mocked database client."""
    client = Mock()
    client.execute_query.return_value = [
        {"id": 1, "name": "John", "location": "New York"},
        {"id": 2, "name": "Jane", "location": "New York"}
    ]
    return client


@pytest.fixture
def mock_context_manager():
    """Fixture for mocked context manager."""
    manager = Mock()
    manager.get_schema_context.return_value = "CREATE TABLE users (id INT, name TEXT, location TEXT)"
    manager.get_documentation.return_value = "Users table contains user information"
    manager.get_relevant_history.return_value = []
    return manager


@pytest.fixture
def processor(mock_llm_client, mock_db_client, mock_context_manager):
    """Fixture for Text2SQL processor."""
    with patch("adpa.text2sql.core.feedback_processor.LLMClient") as llm_mock, \
         patch("adpa.text2sql.core.feedback_processor.DatabaseClient") as db_mock, \
         patch("adpa.text2sql.core.feedback_processor.ContextManager") as ctx_mock:
        
        llm_mock.return_value = mock_llm_client
        db_mock.return_value = mock_db_client
        ctx_mock.return_value = mock_context_manager
        
        processor = Text2SQLFeedbackProcessor({
            "max_attempts": 3,
            "min_confidence": 0.7
        })
        yield processor


@pytest.mark.asyncio
async def test_should_process_simple_query_successfully(processor):
    """Test successful processing of a simple query."""
    # Given
    question = "Show me users from New York"
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert isinstance(result, QueryResult)
    assert "SELECT * FROM users" in result.query.query
    assert "New York" in result.query.query
    assert result.is_valid
    assert len(result.results) == 2


@pytest.mark.asyncio
async def test_should_improve_query_through_feedback(processor, mock_llm_client):
    """Test query improvement through feedback loop."""
    # Given
    question = "Find high-value customers"
    mock_llm_client.generate_sql.side_effect = [
        {"sql": "SELECT * FROM users", "confidence": 0.6},  # First attempt
        {"sql": "SELECT * FROM users WHERE value > 1000", "confidence": 0.9}  # Improved
    ]
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert "value > 1000" in result.query.query
    assert result.query.confidence_score > 0.8
    assert mock_llm_client.generate_sql.call_count == 2


@pytest.mark.asyncio
async def test_should_handle_validation_errors(processor, mock_llm_client):
    """Test handling of validation errors."""
    # Given
    question = "Show me invalid data"
    mock_llm_client.generate_sql.return_value = {
        "sql": "SELECT * FROM nonexistent_table",
        "confidence": 0.9
    }
    
    # When/Then
    with pytest.raises(ValidationError) as exc:
        await processor.process_query(question)
    assert "table does not exist" in str(exc.value)


@pytest.mark.asyncio
async def test_should_respect_max_attempts(processor, mock_llm_client):
    """Test max attempts limit."""
    # Given
    question = "Complex question"
    mock_llm_client.generate_sql.return_value = {
        "sql": "INVALID SQL",
        "confidence": 0.5
    }
    
    # When/Then
    with pytest.raises(MaxAttemptsExceeded) as exc:
        await processor.process_query(question)
    assert mock_llm_client.generate_sql.call_count == 3


@pytest.mark.asyncio
async def test_should_use_context_for_better_results(processor, mock_context_manager):
    """Test context utilization."""
    # Given
    question = "Show me user orders"
    mock_context_manager.get_relevant_history.return_value = [
        SQLQuery(
            query="SELECT * FROM users WHERE id = 1",
            natural_question="Show me user 1",
            confidence_score=0.9,
            generated_at=datetime.utcnow()
        )
    ]
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert result.is_valid
    assert mock_context_manager.get_relevant_history.called
    assert mock_context_manager.get_schema_context.called


@pytest.mark.asyncio
async def test_should_track_performance_metrics(processor):
    """Test performance metrics tracking."""
    # Given
    question = "Show me all users"
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert result.query.metrics is not None
    assert result.query.metrics.execution_time > 0
    assert result.query.metrics.result_count == 2


@pytest.mark.asyncio
async def test_should_handle_empty_results_gracefully(processor, mock_db_client):
    """Test handling of queries with no results."""
    # Given
    question = "Show me users from Mars"
    mock_db_client.execute_query.return_value = []
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert result.is_valid
    assert len(result.results) == 0
    assert result.query.metrics.result_count == 0


@pytest.mark.asyncio
async def test_should_validate_query_structure(processor, mock_llm_client):
    """Test SQL query structure validation."""
    # Given
    question = "Show me users"
    mock_llm_client.generate_sql.side_effect = [
        {"sql": "SELECT FROM users", "confidence": 0.9},  # Invalid SQL
        {"sql": "SELECT * FROM users", "confidence": 0.9}  # Valid SQL
    ]
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert result.is_valid
    assert "SELECT * FROM users" in result.query.query
    assert mock_llm_client.generate_sql.call_count == 2


@pytest.mark.asyncio
async def test_should_handle_complex_queries(processor):
    """Test handling of complex queries."""
    # Given
    question = "Show me average order value by user segment in 2024"
    
    # When
    result = await processor.process_query(question)
    
    # Then
    assert result.is_valid
    assert "GROUP BY" in result.query.query.upper()
    assert "AVG" in result.query.query.upper()
    assert "2024" in result.query.query
