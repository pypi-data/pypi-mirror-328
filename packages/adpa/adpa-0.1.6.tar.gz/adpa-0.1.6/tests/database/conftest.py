"""Test configuration for database tests."""
from __future__ import annotations

import os
import pytest
from pathlib import Path
from typing import Generator

from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from adpa.database.models import Base


@pytest.fixture(scope="session")
def test_db_url() -> str:
    """Get test database URL.

    Returns:
        Test database URL
    """
    return "sqlite:///:memory:?check_same_thread=False"


@pytest.fixture(scope="session")
def engine(test_db_url: str) -> Generator[Engine, None, None]:
    """Create test database engine.

    Args:
        test_db_url: Test database URL

    Yields:
        Database engine
    """
    engine = create_engine(
        test_db_url,
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


@pytest.fixture(scope="session")
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
