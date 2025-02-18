"""Test suite for input sanitization module."""
import pytest
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from adpa.security.sanitization.sanitizer import (
    InputSanitizer,
    SanitizationConfig,
    SanitizationMiddleware
)


@pytest.fixture
def default_config():
    """Create default sanitization config."""
    return SanitizationConfig()


@pytest.fixture
def custom_config():
    """Create custom sanitization config."""
    return SanitizationConfig(
        allowed_html_tags=["p", "br"],
        allowed_html_attributes={"p": ["class"]},
        max_length=100,
        strip_comments=True,
        escape_sql=True
    )


@pytest.fixture
def default_sanitizer(default_config):
    """Create default sanitizer instance."""
    return InputSanitizer(default_config)


@pytest.fixture
def custom_sanitizer(custom_config):
    """Create custom sanitizer instance."""
    return InputSanitizer(custom_config)


@pytest.fixture
def app(default_sanitizer):
    """Create test FastAPI application."""
    app = FastAPI()
    app.add_middleware(
        SanitizationMiddleware,
        sanitizer=default_sanitizer,
        skip_paths={"/health"}
    )

    @app.post("/test")
    async def test_endpoint(request: Request):
        data = await request.json()
        return {"sanitized": data}

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return TestClient(app)


def test_should_sanitize_basic_string(default_sanitizer):
    """Test basic string sanitization."""
    input_str = "  Hello <script>alert('xss')</script> World  "
    expected = "Hello World"
    result = default_sanitizer.sanitize_string(input_str)
    assert "script" not in result
    assert result.strip() == expected.strip()


def test_should_allow_permitted_html(default_sanitizer):
    """Test that permitted HTML tags are preserved."""
    input_str = "<p>Hello <strong>World</strong></p>"
    result = default_sanitizer.sanitize_string(input_str)
    assert "<p>" in result
    assert "<strong>" in result


def test_should_handle_sql_injection(default_sanitizer):
    """Test SQL injection prevention."""
    input_str = "'; DROP TABLE users; --"
    result = default_sanitizer.sanitize_string(input_str)
    assert "'" not in result or "\\'" in result
    assert ";" not in result or "\\;" in result


def test_should_respect_max_length(custom_sanitizer):
    """Test maximum length restriction."""
    input_str = "x" * 101
    with pytest.raises(ValueError, match="exceeds maximum length"):
        custom_sanitizer.sanitize_string(input_str)


def test_should_sanitize_nested_dict(default_sanitizer):
    """Test nested dictionary sanitization."""
    input_dict = {
        "name": "<script>alert('xss')</script>John",
        "details": {
            "bio": "<p>Hello <script>alert('xss')</script>World</p>"
        }
    }
    result = default_sanitizer.sanitize_dict(input_dict)
    assert "script" not in result["name"]
    assert "script" not in result["details"]["bio"]
    assert "<p>" in result["details"]["bio"]


def test_should_sanitize_list_items(default_sanitizer):
    """Test list sanitization."""
    input_list = [
        "<script>alert('xss')</script>",
        {"text": "<script>alert('xss')</script>"},
        ["<script>alert('xss')</script>"]
    ]
    result = default_sanitizer.sanitize_list(input_list)
    assert all("script" not in str(item) for item in result)


def test_should_handle_middleware_json(client):
    """Test middleware with JSON payload."""
    response = client.post(
        "/test",
        json={
            "text": "<script>alert('xss')</script>Hello",
            "nested": {"html": "<p>Valid <script>Invalid</script></p>"}
        }
    )
    assert response.status_code == 200
    data = response.json()["sanitized"]
    assert "script" not in data["text"]
    assert "script" not in data["nested"]["html"]


def test_should_skip_specified_paths(client):
    """Test that specified paths are skipped."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_should_handle_custom_config():
    """Test sanitizer with custom configuration."""
    config = SanitizationConfig(
        allowed_html_tags=["div"],
        max_length=50,
        strip_comments=False
    )
    sanitizer = InputSanitizer(config)
    
    input_str = "<div>Valid</div><p>Invalid</p>"
    result = sanitizer.sanitize_string(input_str)
    assert "<div>" in result
    assert "<p>" not in result
