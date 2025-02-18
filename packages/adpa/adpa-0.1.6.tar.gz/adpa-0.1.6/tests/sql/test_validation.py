"""Tests for SQL validation functionality."""
import pytest
from sqlalchemy import create_engine
from adpa.sql.validation import (
    SQLValidator,
    SecurityValidation,
    SchemaValidation,
    PerformanceValidation,
    ValidationError,
    SecurityError,
    SchemaError,
    PerformanceError
)


@pytest.fixture
def mock_engine(mocker):
    """Create mock SQLAlchemy engine."""
    engine = mocker.Mock()
    engine.connect.return_value.__enter__.return_value = mocker.Mock()
    return engine


@pytest.fixture
def security_config():
    """Create security validation config."""
    return SecurityValidation(
        allowed_operations=["SELECT"],
        blocked_keywords=["DROP", "DELETE", "TRUNCATE"],
        max_joins=3,
        max_conditions=5
    )


@pytest.fixture
def schema_config():
    """Create schema validation config."""
    return SchemaValidation(
        required_tables=["users", "orders"],
        required_columns={
            "users": ["id", "email"],
            "orders": ["id", "user_id"]
        },
        allowed_joins=["users.id = orders.user_id"]
    )


@pytest.fixture
def performance_config():
    """Create performance validation config."""
    return PerformanceValidation(
        max_rows=1000,
        timeout_seconds=30,
        min_index_usage=0.5
    )


@pytest.fixture
def validator(mock_engine, security_config, schema_config, performance_config):
    """Create SQL validator instance."""
    return SQLValidator(
        mock_engine,
        security_config,
        schema_config,
        performance_config
    )


def test_should_validate_simple_select(validator):
    """Test validation of simple SELECT query."""
    sql = "SELECT id, email FROM users LIMIT 10"
    result = validator.validate_query(sql)
    
    assert result.valid
    assert not result.errors
    assert not result.warnings


def test_should_reject_unsafe_operation(validator):
    """Test rejection of unsafe SQL operation."""
    sql = "DROP TABLE users"
    result = validator.validate_query(sql)
    
    assert not result.valid
    assert any("Operation DROP not allowed" in error for error in result.errors)


def test_should_validate_joins(validator):
    """Test validation of JOIN conditions."""
    sql = """
        SELECT u.id, u.email, o.id
        FROM users u
        JOIN orders o ON u.id = o.user_id
        LIMIT 10
    """
    result = validator.validate_query(sql)
    
    assert result.valid
    assert not result.errors


def test_should_detect_excessive_joins(validator):
    """Test detection of excessive JOIN operations."""
    sql = """
        SELECT u.id, o.id, p.id, i.id
        FROM users u
        JOIN orders o ON u.id = o.user_id
        JOIN products p ON o.product_id = p.id
        JOIN items i ON p.item_id = i.id
        LIMIT 10
    """
    result = validator.validate_query(sql)
    
    assert result.warnings
    assert any("joins" in warning.lower() for warning in result.warnings)


def test_should_validate_required_columns(validator):
    """Test validation of required columns."""
    sql = "SELECT name FROM users LIMIT 10"
    result = validator.validate_query(sql)
    
    assert not result.valid
    assert any("Required column missing" in error for error in result.errors)


def test_should_check_performance(validator):
    """Test performance validation."""
    # Mock EXPLAIN result
    validator.engine.connect().__enter__().execute().fetchall.return_value = [
        {"rows": 2000, "index_usage": 0.3}
    ]
    
    sql = "SELECT * FROM users JOIN orders ON users.id = orders.user_id"
    result = validator.validate_query(sql)
    
    assert result.warnings
    assert any("large result set" in warning.lower() for warning in result.warnings)
    assert any("poor index usage" in warning.lower() for warning in result.warnings)


def test_should_generate_suggestions(validator):
    """Test generation of improvement suggestions."""
    sql = """
        SELECT *
        FROM users u
        JOIN orders o ON u.id = o.user_id
        WHERE u.active = true
    """
    result = validator.validate_query(sql)
    
    assert result.suggestions
    assert any("LIMIT clause" in suggestion for suggestion in result.suggestions)


def test_should_handle_malformed_sql(validator):
    """Test handling of malformed SQL."""
    sql = "SELECT * FRO users"  # Intentional typo
    result = validator.validate_query(sql)
    
    assert not result.valid
    assert result.errors


def test_should_validate_conditions(validator):
    """Test validation of WHERE conditions."""
    sql = """
        SELECT id FROM users
        WHERE active = true
        AND verified = true
        AND age > 18
        AND country = 'US'
        AND status = 'active'
        AND role = 'user'
    """
    result = validator.validate_query(sql)
    
    assert result.warnings
    assert any("conditions" in warning.lower() for warning in result.warnings)


def test_should_handle_security_error(validator):
    """Test handling of security validation error."""
    with pytest.raises(SecurityError):
        validator._validate_security("DROP TABLE users")


def test_should_handle_schema_error(validator):
    """Test handling of schema validation error."""
    with pytest.raises(SchemaError):
        validator._validate_schema("SELECT * FROM nonexistent_table")


def test_should_handle_performance_error(validator):
    """Test handling of performance validation error."""
    with pytest.raises(PerformanceError):
        validator._validate_performance("SELECT * FROM huge_table")


def test_should_validate_complex_query(validator):
    """Test validation of complex but valid query."""
    sql = """
        SELECT u.id, u.email, COUNT(o.id) as order_count
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        WHERE u.active = true
        GROUP BY u.id, u.email
        HAVING COUNT(o.id) > 0
        ORDER BY order_count DESC
        LIMIT 10
    """
    result = validator.validate_query(sql)
    
    assert result.valid
    assert not result.errors
