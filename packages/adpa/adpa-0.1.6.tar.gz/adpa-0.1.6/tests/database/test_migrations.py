"""Tests for database migrations."""
from __future__ import annotations

import os
import pytest
from pathlib import Path
from typing import Generator
from unittest.mock import MagicMock, patch

from alembic import command
from alembic.config import Config
from sqlalchemy import URL, create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from adpa.database.config import DatabaseConfig
from adpa.database.models import Base


@pytest.fixture
def alembic_config() -> Config:
    """Create Alembic configuration.

    Returns:
        Alembic configuration
    """
    migrations_path = Path(__file__).parent.parent.parent / "src" / "adpa" / "database" / "migrations"
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", str(migrations_path))
    alembic_cfg.set_main_option("sqlalchemy.url", "sqlite:///:memory:?check_same_thread=False")
    return alembic_cfg


@pytest.fixture(scope="session")
def engine() -> Generator[Engine, None, None]:
    """Create test database engine.

    Yields:
        Database engine
    """
    engine = create_engine(
        "sqlite:///:memory:?check_same_thread=False",
        future=True,
        echo=bool(os.getenv("SQLALCHEMY_ECHO", False)),
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(engine: Engine) -> Generator[Session, None, None]:
    """Create test database session.

    Args:
        engine: Database engine

    Yields:
        Database session
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_should_create_all_tables(session: Session) -> None:
    """Test table creation.

    Args:
        session: Database session
    """
    # Get list of tables
    result = session.execute(
        text(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
            """
        )
    )
    tables = [row[0] for row in result]

    # Verify all models have corresponding tables
    expected_tables = {
        table.name
        for table in Base.metadata.sorted_tables
    }

    assert set(tables) == expected_tables


def test_should_run_migrations_offline(alembic_config: Config) -> None:
    """Test offline migrations.

    Args:
        alembic_config: Alembic configuration
    """
    with patch.dict(os.environ, {
        "POSTGRES_DRIVER": "sqlite",
        "POSTGRES_DATABASE": ":memory:",
    }):
        command.upgrade(alembic_config, "head")
        command.downgrade(alembic_config, "base")


def test_should_run_migrations_online(alembic_config: Config, session: Session) -> None:
    """Test online migrations.

    Args:
        alembic_config: Alembic configuration
        session: Database session
    """
    with patch.dict(os.environ, {
        "POSTGRES_DRIVER": "sqlite",
        "POSTGRES_DATABASE": ":memory:",
    }):
        command.upgrade(alembic_config, "head")
        
        # Verify all tables exist
        result = session.execute(
            text(
                """
                SELECT name FROM sqlite_master
                WHERE type='table' AND name NOT LIKE 'sqlite_%'
                ORDER BY name;
                """
            )
        )
        tables = [row[0] for row in result]

        expected_tables = {
            table.name
            for table in Base.metadata.sorted_tables
        }
        assert set(tables) == expected_tables

        # Test downgrade
        command.downgrade(alembic_config, "base")


def test_should_handle_database_config() -> None:
    """Test database configuration handling."""
    with patch.dict(os.environ, {
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": "5432",
        "POSTGRES_DATABASE": "test_db",
        "POSTGRES_USER": "test_user",
        "POSTGRES_PASSWORD": "test_password",
        "POSTGRES_SCHEMA": "public",
        "POSTGRES_POOL_SIZE": "5",
        "POSTGRES_MAX_OVERFLOW": "10",
        "POSTGRES_POOL_TIMEOUT": "30",
        "POSTGRES_POOL_RECYCLE": "1800",
        "POSTGRES_ECHO": "true",
        "POSTGRES_DRIVER": "postgresql",
    }):
        db_config = DatabaseConfig.from_env()
        assert db_config.host == "localhost"
        assert db_config.port == 5432
        assert db_config.database == "test_db"
        assert db_config.user == "test_user"
        assert db_config.password == "test_password"
        assert db_config.schema == "public"
        assert db_config.pool_size == 5
        assert db_config.max_overflow == 10
        assert db_config.pool_timeout == 30
        assert db_config.pool_recycle == 1800
        assert db_config.echo is True
        assert db_config.driver == "postgresql"
