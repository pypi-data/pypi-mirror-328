"""Tests for Text-to-SQL hybrid coordinator."""

import pytest
import asyncio
from unittest.mock import Mock, patch
from datetime import datetime

from adpa.text2sql.hybrid.coordinator import Text2SQLCoordinator
from adpa.text2sql.models.query_models import QueryResult, QueryIntent

@pytest.fixture
def coordinator():
    """Create Text2SQLCoordinator instance."""
    config = {
        "connection_params": {
            "host": "localhost",
            "database": "test_db"
        },
        "max_history": 10
    }
    return Text2SQLCoordinator(config)

@pytest.fixture
def sample_schema():
    """Sample database schema."""
    return {
        "tables": {
            "users": {
                "columns": ["id", "name", "email"],
                "primary_key": "id"
            },
            "orders": {
                "columns": ["id", "user_id", "total"],
                "primary_key": "id",
                "foreign_keys": {
                    "user_id": "users.id"
                }
            }
        }
    }

@pytest.mark.asyncio
async def test_should_process_simple_query(coordinator, sample_schema):
    """Test processing a simple query."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.db_manager.execute_query = Mock(return_value=[
        {"id": 1, "name": "Test User"}
    ])
    
    # Process query
    result = await coordinator.process_query(
        "Find all users"
    )
    
    # Verify result
    assert isinstance(result, QueryResult)
    assert result.natural_query == "Find all users"
    assert "SELECT" in result.sql_query.upper()
    assert len(result.results) == 1
    assert result.results[0]["name"] == "Test User"

@pytest.mark.asyncio
async def test_should_handle_invalid_query(coordinator, sample_schema):
    """Test handling invalid query."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.validator.validate = Mock(return_value=(False, "Invalid query"))
    
    # Process invalid query
    with pytest.raises(ValueError) as exc:
        await coordinator.process_query(
            "Invalid query that should fail"
        )
    
    assert "Invalid query" in str(exc.value)

@pytest.mark.asyncio
async def test_should_maintain_history(coordinator, sample_schema):
    """Test query history maintenance."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.db_manager.execute_query = Mock(return_value=[])
    
    # Process multiple queries
    for i in range(15):  # More than max_history
        await coordinator.process_query(f"Query {i}")
    
    # Verify history size
    assert len(coordinator._processing_history) == 10  # max_history
    assert coordinator._processing_history[-1]["result"]["natural_query"] == "Query 14"

@pytest.mark.asyncio
async def test_should_cache_schema(coordinator, sample_schema):
    """Test schema caching."""
    # Mock get_schema
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    
    # First call should get schema
    await coordinator._get_schema()
    assert coordinator.db_manager.get_schema.call_count == 1
    
    # Second call within cache period should use cached
    await coordinator._get_schema()
    assert coordinator.db_manager.get_schema.call_count == 1

@pytest.mark.asyncio
async def test_should_handle_nlp_agent_error(coordinator, sample_schema):
    """Test handling NLP agent error."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.nlp_agent.process = Mock(side_effect=Exception("NLP error"))
    
    # Process query with NLP error
    with pytest.raises(Exception) as exc:
        await coordinator.process_query("Query that fails NLP")
    
    assert "NLP error" in str(exc.value)

@pytest.mark.asyncio
async def test_should_optimize_query(coordinator, sample_schema):
    """Test query optimization."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.db_manager.execute_query = Mock(return_value=[])
    
    # Mock NLP agent
    coordinator.nlp_agent.process = Mock(return_value=QueryIntent(
        original_text="Find users",
        entities=[],
        relationships=[],
        query_type="select",
        embeddings=[],
        confidence=0.9,
        context={}
    ))
    
    # Process query
    result = await coordinator.process_query("Find users")
    
    # Verify optimization steps
    assert "optimizations" in result.metadata
    assert isinstance(result.metadata["optimizations"], list)

@pytest.mark.asyncio
async def test_should_track_performance(coordinator, sample_schema):
    """Test performance tracking."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.db_manager.execute_query = Mock(return_value=[])
    
    # Process query
    result = await coordinator.process_query("Find users")
    
    # Verify performance metrics
    assert "performance" in result.metadata
    assert isinstance(result.metadata["performance"], dict)
    
@pytest.mark.asyncio
async def test_should_handle_concurrent_requests(coordinator, sample_schema):
    """Test handling concurrent requests."""
    # Mock dependencies
    coordinator.db_manager.get_schema = Mock(return_value=sample_schema)
    coordinator.db_manager.execute_query = Mock(return_value=[])
    
    # Process multiple queries concurrently
    queries = ["Query 1", "Query 2", "Query 3"]
    tasks = [
        coordinator.process_query(query)
        for query in queries
    ]
    
    results = await asyncio.gather(*tasks)
    
    # Verify all queries processed
    assert len(results) == len(queries)
    for result in results:
        assert isinstance(result, QueryResult)
