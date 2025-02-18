"""Tests for the ADPA configuration system."""
import os
import pytest
from typing import Dict, Optional
from pydantic import BaseModel, ValidationError

from adpa.core.config import (
    ConfigValidator,
    DatabaseConfig,
    APIConfig,
    ApplicationConfig,
    validate_environment
)


class TestConfig(BaseModel):
    """Test configuration model."""
    name: str
    value: Optional[str] = None
    enabled: bool = True


@pytest.fixture
def env_vars():
    """Fixture for environment variables."""
    original_env = dict(os.environ)
    
    # Set test environment variables
    test_vars = {
        "OPENAI_API_KEY": "test-openai-key",
        "ANTHROPIC_API_KEY": "test-anthropic-key",
        "AZURE_API_KEY": "test-azure-key",
        "AZURE_ENDPOINT": "https://test.azure.com",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": "5432",
        "POSTGRES_USER": "test_user",
        "POSTGRES_PASSWORD": "test_pass",
        "POSTGRES_DATABASE": "test_db",
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development",
        "FLASK_DEBUG": "1"
    }
    
    os.environ.update(test_vars)
    yield test_vars
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


def test_config_validator_initialization():
    """Test configuration validator initialization."""
    validator = ConfigValidator()
    assert validator is not None
    assert hasattr(validator, "validate")


def test_database_config_validation(env_vars):
    """Test database configuration validation."""
    # Test valid configuration
    config = DatabaseConfig(
        host=env_vars["POSTGRES_HOST"],
        port=int(env_vars["POSTGRES_PORT"]),
        user=env_vars["POSTGRES_USER"],
        password=env_vars["POSTGRES_PASSWORD"],
        database=env_vars["POSTGRES_DATABASE"]
    )
    assert config.validate() is True
    
    # Test invalid port
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host="localhost",
            port=-1,  # Invalid port
            user="test",
            password="test",
            database="test"
        )
    
    # Test invalid credentials
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host="localhost",
            port=5432,
            user="",  # Empty username
            password="test",
            database="test"
        )


def test_api_config_validation(env_vars):
    """Test API configuration validation."""
    # Test valid configuration
    config = APIConfig(
        openai_api_key=env_vars["OPENAI_API_KEY"],
        anthropic_api_key=env_vars["ANTHROPIC_API_KEY"],
        azure_api_key=env_vars["AZURE_API_KEY"],
        azure_endpoint=env_vars["AZURE_ENDPOINT"]
    )
    assert config.validate() is True
    
    # Test invalid API key format
    with pytest.raises(ValidationError):
        APIConfig(
            openai_api_key="invalid-key",  # Invalid format
            anthropic_api_key=env_vars["ANTHROPIC_API_KEY"],
            azure_api_key=env_vars["AZURE_API_KEY"],
            azure_endpoint=env_vars["AZURE_ENDPOINT"]
        )
    
    # Test invalid endpoint URL
    with pytest.raises(ValidationError):
        APIConfig(
            openai_api_key=env_vars["OPENAI_API_KEY"],
            anthropic_api_key=env_vars["ANTHROPIC_API_KEY"],
            azure_api_key=env_vars["AZURE_API_KEY"],
            azure_endpoint="invalid-url"  # Invalid URL
        )


def test_application_config_validation(env_vars):
    """Test application configuration validation."""
    # Test valid configuration
    config = ApplicationConfig(
        flask_app=env_vars["FLASK_APP"],
        flask_env=env_vars["FLASK_ENV"],
        flask_debug=bool(int(env_vars["FLASK_DEBUG"]))
    )
    assert config.validate() is True
    
    # Test invalid environment
    with pytest.raises(ValidationError):
        ApplicationConfig(
            flask_app="app.py",
            flask_env="invalid",  # Invalid environment
            flask_debug=True
        )


def test_environment_validation(env_vars):
    """Test complete environment validation."""
    result = validate_environment()
    assert result["status"] == "success"
    assert "config" in result
    
    # Test with missing required variables
    os.environ.pop("OPENAI_API_KEY")
    result = validate_environment()
    assert result["status"] == "error"
    assert "missing required variable" in result["message"].lower()


def test_config_type_validation():
    """Test configuration type validation."""
    validator = ConfigValidator()
    
    # Test valid configuration
    config = TestConfig(name="test", value="value")
    assert validator.validate_type(config) is True
    
    # Test invalid type
    with pytest.raises(TypeError):
        validator.validate_type("not a config object")


def test_config_value_ranges():
    """Test configuration value range validation."""
    validator = ConfigValidator()
    
    # Test port range validation
    assert validator.validate_port(1) is True
    assert validator.validate_port(65535) is True
    assert validator.validate_port(0) is False
    assert validator.validate_port(65536) is False
    
    # Test timeout range validation
    assert validator.validate_timeout(1) is True
    assert validator.validate_timeout(3600) is True
    assert validator.validate_timeout(0) is False
    assert validator.validate_timeout(-1) is False


def test_config_format_validation():
    """Test configuration format validation."""
    validator = ConfigValidator()
    
    # Test API key format
    assert validator.validate_api_key("sk-1234567890abcdef") is True
    assert validator.validate_api_key("invalid-key") is False
    
    # Test URL format
    assert validator.validate_url("https://api.example.com") is True
    assert validator.validate_url("not-a-url") is False


def test_config_cross_field_validation():
    """Test cross-field configuration validation."""
    # Test database URI construction
    db_config = DatabaseConfig(
        host="localhost",
        port=5432,
        user="test",
        password="test",
        database="test"
    )
    uri = db_config.get_uri()
    assert uri == "postgresql://test:test@localhost:5432/test"
    
    # Test SSL requirements
    db_config.ssl_required = True
    assert "sslmode=require" in db_config.get_uri()


def test_config_inheritance():
    """Test configuration inheritance and overrides."""
    base_config = {
        "timeout": 30,
        "retries": 3,
        "logging": {"level": "INFO"}
    }
    
    # Test config inheritance
    child_config = {
        "timeout": 60,  # Override
        "new_option": "value"  # Add new
    }
    
    validator = ConfigValidator()
    merged = validator.merge_configs(base_config, child_config)
    
    assert merged["timeout"] == 60  # Overridden
    assert merged["retries"] == 3  # Inherited
    assert merged["logging"]["level"] == "INFO"  # Inherited nested
    assert merged["new_option"] == "value"  # Added


def test_config_security_validation():
    """Test security-related configuration validation."""
    validator = ConfigValidator()
    
    # Test password strength
    assert validator.validate_password("weak") is False
    assert validator.validate_password("StrongP@ssw0rd") is True
    
    # Test SSL configuration
    assert validator.validate_ssl_config({"enabled": True, "verify": False}) is False
    assert validator.validate_ssl_config({"enabled": True, "verify": True}) is True


def test_config_environment_override():
    """Test environment variable override behavior."""
    # Test with environment override
    os.environ["TEST_TIMEOUT"] = "60"
    validator = ConfigValidator()
    config = {"timeout": 30}  # Default value
    
    merged = validator.apply_environment_overrides(config, prefix="TEST_")
    assert merged["timeout"] == 60  # Overridden by environment
    
    # Test without environment override
    os.environ.pop("TEST_TIMEOUT")
    merged = validator.apply_environment_overrides(config, prefix="TEST_")
    assert merged["timeout"] == 30  # Default preserved
