"""Database configuration for the UI."""
from typing import Optional, Generator
import os
from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from adpa.database.models.base import Base
from adpa.utils.logger import get_logger

# Setup logging
logger = get_logger(__name__)

# Database URL from environment or default
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/adpa"
)

# Create engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_engine() -> Engine:
    """Get SQLAlchemy engine instance.
    
    Returns:
        Engine: SQLAlchemy engine instance
    """
    return engine


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Get database session with automatic cleanup.
    
    Yields:
        Session: Database session
        
    Raises:
        SQLAlchemyError: If database operations fail
    """
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


def init_db(drop_all: bool = False) -> None:
    """Initialize database schema.
    
    Args:
        drop_all: Whether to drop all tables before creation
    
    Raises:
        SQLAlchemyError: If schema operations fail
    """
    try:
        if drop_all:
            logger.warning("Dropping all tables...")
            Base.metadata.drop_all(bind=engine)
        
        logger.info("Creating database schema...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database schema created successfully")
        
    except SQLAlchemyError as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        raise


def check_connection() -> bool:
    """Check database connection.
    
    Returns:
        bool: True if connection is successful, False otherwise
    """
    try:
        with get_db() as db:
            db.execute("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"Database connection check failed: {str(e)}")
        return False
