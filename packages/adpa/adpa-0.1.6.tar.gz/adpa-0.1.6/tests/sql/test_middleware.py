"""Tests for SQL middleware functionality."""
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from adpa.sql.middleware import SQLMiddleware
from adpa.sql.generator import SQLGenerator, SQLGenerationConfig
from adpa.sql.validation import SQLValidator


@pytest.fixture
def mock_generator(mocker):
    """Create mock SQL generator."""
    generator = mocker.Mock()
    generator.generate_query.return_value = {
        "success": True,
        "query": "SELECT id FROM users LIMIT 10",
        "phases": {
            "reasoning": {"content": "Test reasoning"},
            "analysis": {"content": "Test analysis"},
            "query": {"content": "Test query"},
            "verification": {"content": "Test verification"}
        }
    }
    return generator


@pytest.fixture
def mock_validator(mocker):
    """Create mock SQL validator."""
    validator = mocker.Mock()
    validator.validate_query.return_value = mocker.Mock(
        valid=True,
        errors=[],
        warnings=[],
        dict=lambda: {"valid": True}
    )
    return validator


@pytest.fixture
def app(mock_generator, mock_validator):
    """Create test FastAPI application."""
    app = FastAPI()
    app.add_middleware(
        SQLMiddleware,
        generator=mock_generator,
        validator=mock_validator,
        skip_paths={"/health"}
    )

    @app.post("/api/query")
    async def query():
        return {"status": "success"}

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return TestClient(app)


def test_should_process_valid_query(client, mock_generator, mock_validator):
    """Test processing of valid query."""
    response = client.post(
        "/api/query",
        json={"query": "Show all users"}
    )
    
    assert response.status_code == 200
    mock_generator.generate_query.assert_called_once()
    mock_validator.validate_query.assert_called_once()


def test_should_skip_health_check(client, mock_generator):
    """Test skipping of health check endpoint."""
    response = client.get("/health")
    
    assert response.status_code == 200
    mock_generator.generate_query.assert_not_called()


def test_should_handle_missing_query(client):
    """Test handling of missing query parameter."""
    response = client.post("/api/query", json={})
    
    assert response.status_code == 400
    assert "Missing query parameter" in response.json()["error"]


def test_should_handle_generation_failure(client, mock_generator):
    """Test handling of query generation failure."""
    mock_generator.generate_query.return_value = {
        "success": False,
        "error": "Generation failed"
    }
    
    response = client.post(
        "/api/query",
        json={"query": "Invalid query"}
    )
    
    assert response.status_code == 400
    assert "Generation failed" in response.json()["details"]


def test_should_handle_validation_failure(client, mock_validator):
    """Test handling of validation failure."""
    mock_validator.validate_query.return_value = mocker.Mock(
        valid=False,
        errors=["Validation error"],
        dict=lambda: {"valid": False}
    )
    
    response = client.post(
        "/api/query",
        json={"query": "Invalid query"}
    )
    
    assert response.status_code == 400
    assert "Validation failed" in response.json()["error"]


def test_should_update_request_body(client, mock_generator):
    """Test updating of request body with processed query."""
    response = client.post(
        "/api/query",
        json={"query": "Show users"}
    )
    
    assert response.status_code == 200
    assert mock_generator.generate_query.called


def test_should_handle_non_json_request(client):
    """Test handling of non-JSON request."""
    response = client.post(
        "/api/query",
        data="not json"
    )
    
    assert response.status_code != 200


def test_should_collect_metrics(client, mock_generator):
    """Test collection of middleware metrics."""
    # Make multiple requests
    for _ in range(3):
        client.post("/api/query", json={"query": "Test query"})
    
    # Make one failed request
    mock_generator.generate_query.return_value = {
        "success": False,
        "error": "Error"
    }
    client.post("/api/query", json={"query": "Failed query"})
    
    middleware = next(
        m for m in client.app.user_middleware
        if isinstance(m.cls, SQLMiddleware)
    )
    metrics = middleware.cls.get_metrics()
    
    assert metrics["requests"] == 4
    assert metrics["errors"] == 1
    assert "avg_generation_time" in metrics
    assert "avg_validation_time" in metrics


def test_should_handle_concurrent_requests(client):
    """Test handling of concurrent requests."""
    import asyncio
    import httpx
    
    async def make_requests():
        async with httpx.AsyncClient(app=client.app) as ac:
            tasks = []
            for _ in range(5):
                task = ac.post(
                    "/api/query",
                    json={"query": "Test query"}
                )
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            return responses
    
    responses = asyncio.run(make_requests())
    assert all(r.status_code == 200 for r in responses)


def test_should_log_requests(client, caplog):
    """Test request logging."""
    client.post("/api/query", json={"query": "Test query"})
    
    assert any("SQL request processed" in record.message for record in caplog.records)


def test_should_handle_timeout(client, mock_generator):
    """Test handling of timeout during query generation."""
    import time
    
    def slow_generation(*args, **kwargs):
        time.sleep(2)
        return {"success": True, "query": "SELECT 1"}
    
    mock_generator.generate_query.side_effect = slow_generation
    
    response = client.post(
        "/api/query",
        json={"query": "Slow query"},
        timeout=1
    )
    
    assert response.status_code != 200


def test_should_respect_content_type(client):
    """Test handling of different content types."""
    # Test with correct content type
    response1 = client.post(
        "/api/query",
        json={"query": "Test"},
        headers={"Content-Type": "application/json"}
    )
    assert response1.status_code == 200
    
    # Test with incorrect content type
    response2 = client.post(
        "/api/query",
        data="Test",
        headers={"Content-Type": "text/plain"}
    )
    assert response2.status_code != 200
