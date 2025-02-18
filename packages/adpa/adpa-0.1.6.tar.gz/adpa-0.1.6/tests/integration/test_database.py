"""Integration tests for database functionality."""
import pytest
from sqlalchemy import text

from adpa.database import Database


@pytest.fixture
def test_db():
    """Create a test database connection."""
    db = Database(
        host="localhost",
        port=5432,
        user="test_user",
        password="test_password",  # This is just for testing
        database="test_db",
    )

    # Set up test data
    with db.engine.connect() as conn:
        conn.execute(
            text(
                "CREATE TABLE IF NOT EXISTS users ("
                "id SERIAL PRIMARY KEY, "
                "name VARCHAR(100), "
                "email VARCHAR(100), "
                "joined_at TIMESTAMP DEFAULT NOW()"
                ")"
            )
        )
        conn.execute(
            text("INSERT INTO users (name, email) VALUES (:name, :email)"),
            {"name": "John Doe", "email": "john@example.com"},
        )
        conn.commit()

    yield db

    # Clean up
    with db.engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS users"))
        conn.commit()


def test_should_connect_to_database(test_db):
    """Test database connection."""
    assert test_db.engine is not None
    with test_db.engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_should_execute_query_with_params(test_db):
    """Test query execution with parameters."""
    with test_db.engine.connect() as conn:
        result = conn.execute(
            text("SELECT name FROM users WHERE email = :email"),
            {"email": "john@example.com"},
        )
        row = result.fetchone()
        assert row is not None
        assert row.name == "John Doe"
