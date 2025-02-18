"""Unit tests for Text2SQL context manager."""

import pytest
from datetime import datetime, timedelta
import numpy as np
from typing import Dict, List

from adpa.text2sql.context.manager import ContextManager
from adpa.text2sql.models.query_models import SQLQuery
from adpa.text2sql.models.exceptions import ContextError


@pytest.fixture
def context_manager():
    """Fixture for context manager."""
    return ContextManager({
        "cache_ttl_minutes": 30,
        "max_history": 100
    })


@pytest.fixture
def sample_query():
    """Fixture for sample query."""
    return SQLQuery(
        query="SELECT * FROM users WHERE location = 'New York'",
        natural_question="Show me users from New York",
        confidence_score=0.9,
        generated_at=datetime.utcnow()
    )


@pytest.mark.asyncio
async def test_should_manage_schema_cache(context_manager):
    """Test schema cache management."""
    # Given/When
    schema = await context_manager.get_schema_context()
    
    # Then
    assert schema is not None
    assert context_manager._last_schema_update is not None


@pytest.mark.asyncio
async def test_should_respect_cache_ttl(context_manager):
    """Test cache TTL enforcement."""
    # Given
    await context_manager.get_schema_context()
    context_manager._last_schema_update = (
        datetime.utcnow() - timedelta(minutes=31)
    )
    
    # When
    schema1 = context_manager.schema_cache.get("schema")
    await context_manager.get_schema_context()
    schema2 = context_manager.schema_cache.get("schema")
    
    # Then
    assert schema1 != schema2


@pytest.mark.asyncio
async def test_should_maintain_query_history(context_manager, sample_query):
    """Test query history maintenance."""
    # Given/When
    await context_manager.add_to_history(sample_query)
    
    # Then
    assert len(context_manager.query_history) == 1
    assert context_manager.query_history[0] == sample_query


@pytest.mark.asyncio
async def test_should_limit_history_size(context_manager):
    """Test history size limitation."""
    # Given
    for i in range(150):
        query = SQLQuery(
            query=f"SELECT {i}",
            natural_question=f"Query {i}",
            confidence_score=0.9,
            generated_at=datetime.utcnow()
        )
        await context_manager.add_to_history(query)
    
    # Then
    assert len(context_manager.query_history) == 100
    assert context_manager.query_history[-1].query == "SELECT 149"


@pytest.mark.asyncio
async def test_should_find_relevant_history(context_manager):
    """Test finding relevant query history."""
    # Given
    queries = [
        "Show users from New York",
        "Display orders from California",
        "List products in stock",
        "Count users in New York"
    ]
    
    for q in queries:
        await context_manager.add_to_history(
            SQLQuery(
                query=f"SELECT * FROM table",
                natural_question=q,
                confidence_score=0.9,
                generated_at=datetime.utcnow()
            )
        )
    
    # When
    relevant = await context_manager.get_relevant_history(
        "Who are the users in New York?",
        limit=2
    )
    
    # Then
    assert len(relevant) == 2
    assert any("New York" in q.natural_question for q in relevant)


@pytest.mark.asyncio
async def test_should_handle_empty_history(context_manager):
    """Test handling of empty history."""
    # Given/When
    relevant = await context_manager.get_relevant_history("Any question")
    
    # Then
    assert relevant == []


@pytest.mark.asyncio
async def test_should_handle_context_errors(context_manager):
    """Test error handling in context operations."""
    # Given
    context_manager.schema_cache = None
    
    # When/Then
    with pytest.raises(ContextError) as exc:
        await context_manager.get_schema_context()
    assert "schema context" in str(exc.value).lower()


@pytest.mark.asyncio
async def test_should_format_documentation(context_manager):
    """Test documentation formatting."""
    # Given
    docs = [
        {"title": "Users Table", "content": "Contains user information"},
        {"title": "Orders Table", "content": "Contains order details"}
    ]
    
    # When
    formatted = context_manager._format_documentation(docs)
    
    # Then
    assert "Users Table" in formatted
    assert "Orders Table" in formatted
    assert "Contains user information" in formatted


@pytest.mark.asyncio
async def test_should_handle_embedding_errors(context_manager):
    """Test handling of embedding generation errors."""
    # Given/When/Then
    with pytest.raises(ContextError) as exc:
        await context_manager._get_embedding(None)
    assert "embedding" in str(exc.value).lower()


@pytest.mark.asyncio
async def test_should_maintain_context_consistency(context_manager, sample_query):
    """Test context consistency maintenance."""
    # Given
    await context_manager.add_to_history(sample_query)
    
    # When
    schema = await context_manager.get_schema_context()
    docs = await context_manager.get_documentation(sample_query.natural_question)
    history = await context_manager.get_relevant_history(
        sample_query.natural_question
    )
    
    # Then
    assert schema is not None
    assert docs is not None
    assert history is not None
    assert len(history) > 0
    assert history[0] == sample_query
