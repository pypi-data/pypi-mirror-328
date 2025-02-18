"""Integration tests for input sanitization."""
import pytest
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from adpa.security.sanitization.sanitizer import (
    InputSanitizer,
    SanitizationConfig,
    SanitizationMiddleware
)


@pytest.fixture
def app():
    """Create test FastAPI application with full middleware stack."""
    app = FastAPI()
    
    # Add sanitization middleware
    app.add_middleware(
        SanitizationMiddleware,
        skip_paths={"/health"}
    )
    
    @app.post("/api/comments")
    async def create_comment(request: Request):
        """Test endpoint for comment creation."""
        data = await request.json()
        return {
            "id": 1,
            "content": data.get("content", ""),
            "metadata": data.get("metadata", {})
        }
    
    @app.post("/api/users")
    async def create_user(request: Request):
        """Test endpoint for user creation with nested data."""
        data = await request.json()
        return {
            "id": 1,
            "profile": data.get("profile", {}),
            "settings": data.get("settings", {})
        }
    
    @app.get("/health")
    async def health():
        """Health check endpoint that should skip sanitization."""
        return {"status": "<healthy>"}
    
    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return TestClient(app)


def test_should_sanitize_comment_content(client):
    """Test sanitization of simple comment content."""
    response = client.post(
        "/api/comments",
        json={
            "content": "<script>alert('xss')</script><p>Hello World</p>",
            "metadata": {"source": "web"}
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "script" not in data["content"]
    assert "<p>Hello World</p>" in data["content"]


def test_should_handle_nested_user_data(client):
    """Test sanitization of nested user data."""
    response = client.post(
        "/api/users",
        json={
            "profile": {
                "bio": "<script>alert('xss')</script><p>About me</p>",
                "website": "javascript:alert('xss')"
            },
            "settings": {
                "theme": "<style>body{background:red}</style>dark"
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "script" not in data["profile"]["bio"]
    assert "javascript:" not in data["profile"]["website"]
    assert "style" not in data["settings"]["theme"]


def test_should_handle_large_payload(client):
    """Test handling of large nested payloads."""
    large_content = "x" * 5000
    response = client.post(
        "/api/comments",
        json={
            "content": f"<p>{large_content}</p>",
            "metadata": {
                "sections": [
                    {"text": "<script>alert('xss')</script>"} for _ in range(10)
                ]
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "script" not in str(data)
    assert len(data["content"]) == len(f"<p>{large_content}</p>")


def test_should_skip_health_check_sanitization(client):
    """Test that health check endpoint skips sanitization."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "<healthy>"}


def test_should_handle_malformed_json(client):
    """Test handling of malformed JSON data."""
    response = client.post(
        "/api/comments",
        data="invalid json{",
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422  # FastAPI's default validation error


def test_should_preserve_valid_html_attributes(client):
    """Test preservation of valid HTML attributes."""
    response = client.post(
        "/api/comments",
        json={
            "content": '<p class="text-bold">Hello <a href="https://example.com">World</a></p>'
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert 'class="text-bold"' in data["content"]
    assert 'href="https://example.com"' in data["content"]


def test_should_handle_concurrent_requests(client):
    """Test handling of concurrent requests with sanitization."""
    import asyncio
    import httpx
    
    async def make_requests():
        async with httpx.AsyncClient(app=client.app) as ac:
            tasks = []
            for i in range(10):
                task = ac.post(
                    "/api/comments",
                    json={
                        "content": f"<script>alert({i})</script><p>Comment {i}</p>"
                    }
                )
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            return responses
    
    responses = asyncio.run(make_requests())
    assert all(r.status_code == 200 for r in responses)
    assert all("script" not in r.json()["content"] for r in responses)


def test_should_maintain_json_structure(client):
    """Test that sanitization maintains the original JSON structure."""
    original_data = {
        "profile": {
            "name": "<script>John</script>",
            "details": {
                "bio": "<p>About <script>me</script></p>",
                "links": ["javascript:alert(1)", "https://example.com"],
                "tags": ["<script>tag1</script>", "<p>tag2</p>"]
            }
        }
    }
    
    response = client.post("/api/users", json=original_data)
    assert response.status_code == 200
    data = response.json()
    
    # Check structure is maintained
    assert "profile" in data
    assert "details" in data["profile"]
    assert isinstance(data["profile"]["details"]["links"], list)
    assert isinstance(data["profile"]["details"]["tags"], list)
    
    # Check sanitization was applied
    assert "script" not in str(data)
    assert "javascript:" not in str(data)
