"""Tests for SQL validation."""

import pytest
from uuid import UUID

from adpa.text2sql.models import Column, Schema, Table
from adpa.text2sql.validation import SQLValidator


@pytest.fixture
def validator():
    """Create SQLValidator instance."""
    return SQLValidator()


@pytest.fixture
def sample_schema():
    """Create sample schema for testing."""
    id_column = Column(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="id",
        type="INTEGER",
        primary_key=True
    )
    name_column = Column(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="name",
        type="VARCHAR"
    )
    users_table = Table(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="users",
        columns=[id_column, name_column]
    )
    return Schema(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="public",
        tables={"users": users_table}
    )


def test_validate_query_injection(validator):
    """Test SQL injection detection."""
    # Valid query
    query = "SELECT * FROM users WHERE id = 1"
    errors = validator.validate_query(query)
    assert not errors

    # Query with injection attempt
    query = "SELECT * FROM users; DROP TABLE users;"
    errors = validator.validate_query(query)
    assert len(errors) == 1
    assert "dangerous SQL pattern" in errors[0].message


def test_validate_query_quotes(validator):
    """Test quote matching validation."""
    # Valid quotes
    query = "SELECT * FROM users WHERE name = 'John'"
    errors = validator.validate_query(query)
    assert not errors

    # Mismatched quotes
    query = "SELECT * FROM users WHERE name = 'John"
    errors = validator.validate_query(query)
    assert len(errors) == 1
    assert "Mismatched quotes" in errors[0].message


def test_validate_schema_compatibility(validator, sample_schema):
    """Test schema compatibility validation."""
    # Valid query
    query = "SELECT id, name FROM users"
    errors = validator.validate_schema_compatibility(query, sample_schema)
    assert not errors

    # Invalid table
    query = "SELECT * FROM customers"
    errors = validator.validate_schema_compatibility(query, sample_schema)
    assert len(errors) == 1
    assert "table 'customers' not found" in errors[0].message

    # Invalid column
    query = "SELECT email FROM users"
    errors = validator.validate_schema_compatibility(query, sample_schema)
    assert len(errors) == 1
    assert "Column 'email' not found" in errors[0].message


def test_sanitize_query(validator):
    """Test query sanitization."""
    # Remove comments
    query = "SELECT * FROM users -- Get all users"
    sanitized = validator.sanitize_query(query)
    assert sanitized == "SELECT * FROM users"

    # Remove multiple semicolons
    query = "SELECT * FROM users;;;"
    sanitized = validator.sanitize_query(query)
    assert sanitized == "SELECT * FROM users"

    # Normalize whitespace
    query = "SELECT   *   FROM    users"
    sanitized = validator.sanitize_query(query)
    assert sanitized == "SELECT * FROM users"
