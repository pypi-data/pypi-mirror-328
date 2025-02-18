"""Tests for database models."""
import pytest
from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from adpa.database.models import (
    Base,
    User,
    Query,
    QueryResult,
    Dataset,
    DataTable,
    APIKey,
    AuditLog,
)


@pytest.fixture
def engine():
    """Create in-memory SQLite database."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    """Create database session."""
    with Session(engine) as session:
        yield session


def test_should_create_user(session):
    """Test user creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    session.add(user)
    session.commit()

    assert isinstance(user.id, UUID)
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.created_at is not None
    assert user.updated_at is not None


def test_should_validate_user_email(session):
    """Test user email validation."""
    with pytest.raises(ValueError, match="Invalid email address"):
        User(
            username="testuser",
            email="invalid-email",
            password_hash="hashedpassword",
        )


def test_should_validate_user_username(session):
    """Test username validation."""
    with pytest.raises(ValueError, match="Username must be at least 3 characters long"):
        User(
            username="ab",
            email="test@example.com",
            password_hash="hashedpassword",
        )


def test_should_create_query(session):
    """Test query creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    session.add(user)
    session.commit()

    query = Query(
        user_id=user.id,
        natural_query="Show me all users",
        sql_query="SELECT * FROM users",
        status="completed",
    )
    session.add(query)
    session.commit()

    assert isinstance(query.id, UUID)
    assert query.user_id == user.id
    assert query.natural_query == "Show me all users"
    assert query.sql_query == "SELECT * FROM users"
    assert query.status == "completed"
    assert query.created_at is not None
    assert query.updated_at is not None


def test_should_create_query_result(session):
    """Test query result creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    query = Query(
        user_id=user.id,
        natural_query="Show me all users",
        sql_query="SELECT * FROM users",
        status="completed",
    )
    session.add_all([user, query])
    session.commit()

    result = QueryResult(
        query_id=query.id,
        result_data={"rows": [{"id": 1, "name": "Test"}]},
        format="json",
    )
    session.add(result)
    session.commit()

    assert isinstance(result.id, UUID)
    assert result.query_id == query.id
    assert result.result_data == {"rows": [{"id": 1, "name": "Test"}]}
    assert result.format == "json"


def test_should_create_dataset(session):
    """Test dataset creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    session.add(user)
    session.commit()

    dataset = Dataset(
        owner_id=user.id,
        name="Test Dataset",
        schema={"columns": ["id", "name"]},
        format="csv",
    )
    session.add(dataset)
    session.commit()

    assert isinstance(dataset.id, UUID)
    assert dataset.owner_id == user.id
    assert dataset.name == "Test Dataset"
    assert dataset.schema == {"columns": ["id", "name"]}
    assert dataset.format == "csv"
    assert dataset.is_public is False


def test_should_create_data_table(session):
    """Test data table creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    dataset = Dataset(
        owner_id=user.id,
        name="Test Dataset",
        schema={"columns": ["id", "name"]},
        format="csv",
    )
    session.add_all([user, dataset])
    session.commit()

    table = DataTable(
        dataset_id=dataset.id,
        name="users",
        schema={"columns": ["id", "name"]},
    )
    session.add(table)
    session.commit()

    assert isinstance(table.id, UUID)
    assert table.dataset_id == dataset.id
    assert table.name == "users"
    assert table.schema == {"columns": ["id", "name"]}


def test_should_create_api_key(session):
    """Test API key creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    session.add(user)
    session.commit()

    api_key = APIKey(
        user_id=user.id,
        key="test-api-key",
        name="Test Key",
        expires_at=datetime.utcnow() + timedelta(days=30),
    )
    session.add(api_key)
    session.commit()

    assert isinstance(api_key.id, UUID)
    assert api_key.user_id == user.id
    assert api_key.key == "test-api-key"
    assert api_key.name == "Test Key"
    assert api_key.is_active is True
    assert api_key.expires_at is not None


def test_should_create_audit_log(session):
    """Test audit log creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
    )
    session.add(user)
    session.commit()

    log = AuditLog(
        user_id=user.id,
        action="create",
        resource_type="dataset",
        resource_id="123",
        status="success",
        details={"name": "Test Dataset"},
        ip_address="127.0.0.1",
        user_agent="Mozilla/5.0",
    )
    session.add(log)
    session.commit()

    assert isinstance(log.id, UUID)
    assert log.user_id == user.id
    assert log.action == "create"
    assert log.resource_type == "dataset"
    assert log.resource_id == "123"
    assert log.status == "success"
    assert log.details == {"name": "Test Dataset"}
    assert log.ip_address == "127.0.0.1"
    assert log.user_agent == "Mozilla/5.0"
