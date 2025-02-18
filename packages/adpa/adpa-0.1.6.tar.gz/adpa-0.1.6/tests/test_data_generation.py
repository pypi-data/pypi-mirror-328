"""Test suite for data generators and validation."""
import pytest
from datetime import datetime, timedelta
from typing import Dict, Any

from tests.utils.test_data_generators import (
    LLMGenerator,
    DatabaseGenerator,
    APIGenerator,
    SecurityGenerator
)

class TestLLMGenerator:
    """Test suite for LLM data generation."""
    
    @pytest.fixture
    def llm_gen(self):
        return LLMGenerator()
    
    def test_prompt_generation(self, llm_gen):
        """Test generation of different prompt types."""
        for template_type in llm_gen.PROMPT_TEMPLATES.keys():
            data = llm_gen.generate_prompt(template_type)
            
            assert isinstance(data, dict)
            assert "prompt" in data
            assert "template_type" in data
            assert "max_tokens" in data
            assert "temperature" in data
            
            assert data["template_type"] == template_type
            assert 50 <= data["max_tokens"] <= 2000
            assert 0.0 <= data["temperature"] <= 1.0
    
    def test_prompt_consistency(self, llm_gen):
        """Test that generated prompts are consistent with their template."""
        data = llm_gen.generate_prompt("question")
        assert data["prompt"].startswith("What is")
        
        data = llm_gen.generate_prompt("translation")
        assert "Translate" in data["prompt"]
        assert any(lang in data["prompt"] for lang in ["Spanish", "French", "German"])

class TestDatabaseGenerator:
    """Test suite for database data generation."""
    
    @pytest.fixture
    def db_gen(self):
        return DatabaseGenerator()
    
    @pytest.mark.parametrize("table_name", ["users", "products", "orders"])
    def test_record_generation(self, db_gen, table_name):
        """Test generation of different table records."""
        record = db_gen.generate_record(table_name)
        
        # Common fields
        assert "id" in record
        assert "created_at" in record
        assert "updated_at" in record
        assert "is_active" in record
        
        # Table-specific fields
        if table_name == "users":
            assert "username" in record
            assert "email" in record
            assert "@" in record["email"]
        elif table_name == "products":
            assert "name" in record
            assert "price" in record
            assert 10.0 <= record["price"] <= 1000.0
        elif table_name == "orders":
            assert "user_id" in record
            assert "total_amount" in record
            assert "status" in record
            assert record["status"] in ["pending", "processing", "shipped", "delivered"]

class TestAPIGenerator:
    """Test suite for API data generation."""
    
    @pytest.fixture
    def api_gen(self):
        return APIGenerator()
    
    @pytest.mark.parametrize("endpoint", ["/users", "/products", "/orders"])
    def test_request_generation(self, api_gen, endpoint):
        """Test generation of API requests."""
        request = api_gen.generate_request(endpoint)
        
        assert "request_id" in request
        assert "timestamp" in request
        assert "client_id" in request
        assert "api_version" in request
        assert request["api_version"].startswith("v")
        
        # Endpoint-specific data
        assert "data" in request
        if endpoint == "/users":
            assert "username" in request["data"]
            assert "email" in request["data"]
        elif endpoint == "/products":
            assert "name" in request["data"]
            assert "price" in request["data"]
        elif endpoint == "/orders":
            assert "user_id" in request["data"]
            assert "products" in request["data"]
            assert isinstance(request["data"]["products"], list)
    
    @pytest.mark.parametrize("status_code", [200, 201, 400, 401, 403, 404, 500])
    def test_response_generation(self, api_gen, status_code):
        """Test generation of API responses."""
        response = api_gen.generate_response(status_code)
        
        assert response["status_code"] == status_code
        assert "timestamp" in response
        assert "request_id" in response
        assert "success" in response
        
        if 200 <= status_code < 300:
            assert response["success"] is True
            assert "data" in response
            assert "id" in response["data"]
        else:
            assert response["success"] is False
            assert "error" in response
            assert "code" in response["error"]
            assert "message" in response["error"]

class TestSecurityGenerator:
    """Test suite for security data generation."""
    
    @pytest.fixture
    def sec_gen(self):
        return SecurityGenerator()
    
    @pytest.mark.parametrize("token_type", ["jwt", "oauth"])
    def test_auth_token_generation(self, sec_gen, token_type):
        """Test generation of authentication tokens."""
        token_data = sec_gen.generate_auth_token(token_type)
        
        assert "token_type" in token_data
        assert "user_id" in token_data
        assert "issued_at" in token_data
        assert "expires_at" in token_data
        assert "scope" in token_data
        assert "token" in token_data
        
        if token_type == "jwt":
            assert token_data["token"].startswith("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9")
        else:
            assert len(token_data["token"]) == 36  # UUID length
    
    @pytest.mark.parametrize("event_type", ["login", "logout", "access_denied", "permission_change"])
    def test_audit_log_generation(self, sec_gen, event_type):
        """Test generation of security audit logs."""
        log = sec_gen.generate_audit_log(event_type)
        
        assert "event_id" in log
        assert "event_type" in log
        assert log["event_type"] == event_type
        assert "timestamp" in log
        assert "user_id" in log
        assert "ip_address" in log
        assert "user_agent" in log
        assert "status" in log
        assert "details" in log
        
        # Validate details
        assert "location" in log["details"]
        assert "device" in log["details"]
        assert "severity" in log["details"]
        assert log["details"]["device"] in ["mobile", "desktop", "tablet"]
        assert log["details"]["severity"] in ["low", "medium", "high"]
