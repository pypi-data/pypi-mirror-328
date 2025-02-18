"""Tests for text2sql models."""

import pytest
from uuid import UUID

from adpa.text2sql.models import Column, Index, Schema, Table, QueryTemplate


def test_column_validation():
    """Test column name validation."""
    # Valid column
    column = Column(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="user_id",
        type="INTEGER"
    )
    assert column.name == "user_id"

    # Invalid column name
    with pytest.raises(ValueError, match="Column name must be a valid identifier"):
        Column(
            id=UUID("12345678-1234-5678-1234-567812345678"),
            name="2invalid",
            type="INTEGER"
        )


def test_index_validation():
    """Test index type validation."""
    # Valid index
    index = Index(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="idx_users_email",
        table="users",
        columns=["email"],
        type="btree"
    )
    assert index.type == "btree"

    # Invalid index type
    with pytest.raises(ValueError, match="Index type must be one of"):
        Index(
            id=UUID("12345678-1234-5678-1234-567812345678"),
            name="idx_users_email",
            table="users",
            columns=["email"],
            type="invalid"
        )


def test_table_validation():
    """Test table name validation."""
    # Valid table
    column = Column(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="id",
        type="INTEGER",
        primary_key=True
    )
    table = Table(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="users",
        columns=[column]
    )
    assert table.name == "users"

    # Invalid table name
    with pytest.raises(ValueError, match="Table name must be a valid identifier"):
        Table(
            id=UUID("12345678-1234-5678-1234-567812345678"),
            name="2users",
            columns=[column]
        )


def test_schema_validation():
    """Test schema dialect validation."""
    # Valid schema
    column = Column(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="id",
        type="INTEGER",
        primary_key=True
    )
    table = Table(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="users",
        columns=[column]
    )
    schema = Schema(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="public",
        tables={"users": table},
        dialect="postgresql"
    )
    assert schema.dialect == "postgresql"

    # Invalid dialect
    with pytest.raises(ValueError, match="Dialect must be one of"):
        Schema(
            id=UUID("12345678-1234-5678-1234-567812345678"),
            name="public",
            tables={"users": table},
            dialect="invalid"
        )


def test_query_template():
    """Test query template rendering."""
    template = QueryTemplate(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        name="select_by_id",
        template="SELECT * FROM {table} WHERE id = {id}"
    )
    
    rendered = template.render(table="users", id=1)
    assert rendered == "SELECT * FROM users WHERE id = 1"
