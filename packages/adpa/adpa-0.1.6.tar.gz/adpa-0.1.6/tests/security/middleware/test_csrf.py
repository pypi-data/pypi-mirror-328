"""Test CSRF middleware functionality."""
import pytest
from datetime import datetime, timedelta
from fastapi import FastAPI, Request, Response
from fastapi.testclient import TestClient
from adpa.security.middleware.csrf import CSRFMiddleware, CSRFToken


@pytest.fixture
def app():
    """Create test FastAPI application."""
    app = FastAPI()
    app.add_middleware(
        CSRFMiddleware,
        secret_key="test_secret_key",
        token_expiry=3600
    )

    @app.get("/test")
    def test_get():
        return {"message": "success"}

    @app.post("/test")
    def test_post():
        return {"message": "success"}

    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return TestClient(app)


def test_should_allow_safe_methods(client):
    """Test that safe methods are allowed without CSRF token."""
    response = client.get("/test")
    assert response.status_code == 200
    assert "csrf_token" in response.cookies


def test_should_block_unsafe_methods_without_token(client):
    """Test that unsafe methods are blocked without CSRF token."""
    response = client.post("/test")
    assert response.status_code == 403
    assert response.json()["detail"] == "CSRF token missing"


def test_should_allow_valid_token(client):
    """Test that valid CSRF token is accepted."""
    # First get the token
    response = client.get("/test")
    csrf_token = response.cookies["csrf_token"]
    
    # Then make POST request with token
    response = client.post(
        "/test",
        headers={"X-CSRF-Token": csrf_token}
    )
    assert response.status_code == 200


def test_should_reject_invalid_token(client):
    """Test that invalid CSRF token is rejected."""
    response = client.post(
        "/test",
        headers={"X-CSRF-Token": "invalid_token"}
    )
    assert response.status_code == 403


def test_should_reject_expired_token(client, app):
    """Test that expired CSRF token is rejected."""
    # Create expired token
    expired_token = CSRFToken(
        token="test_token",
        expires=datetime.utcnow() - timedelta(hours=1)
    )
    
    response = client.post(
        "/test",
        headers={"X-CSRF-Token": expired_token.json()}
    )
    assert response.status_code == 403
    assert "expired" in response.json()["detail"].lower()


def test_should_use_custom_configuration(app):
    """Test custom middleware configuration."""
    middleware = CSRFMiddleware(
        secret_key="custom_key",
        token_expiry=7200,
        safe_methods={"GET", "HEAD"},
        token_header="X-Custom-CSRF",
        cookie_name="custom_csrf",
        cookie_secure=False,
        cookie_httponly=False,
        cookie_samesite="Strict"
    )
    
    assert middleware._token_expiry == 7200
    assert middleware._safe_methods == {"GET", "HEAD"}
    assert middleware._token_header == "X-Custom-CSRF"
    assert middleware._cookie_name == "custom_csrf"
    assert not middleware._cookie_secure
    assert not middleware._cookie_httponly
    assert middleware._cookie_samesite == "Strict"
