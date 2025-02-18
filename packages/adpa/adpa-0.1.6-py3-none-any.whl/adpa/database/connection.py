"""
Database connection management.
"""
from typing import Optional, Dict, Any
import logging
from contextlib import contextmanager
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from adpa.database.config import DatabaseConfig

logger = logging.getLogger(__name__)

class DatabaseConnection:
    """Manage database connections and sessions."""
    
    def __init__(
        self,
        config: DatabaseConfig,
        engine_kwargs: Optional[Dict[str, Any]] = None
    ):
        """Initialize database connection.
        
        Args:
            config: Database configuration
            engine_kwargs: Additional SQLAlchemy engine arguments
        """
        self.config = config
        self._engine: Optional[Engine] = None
        self._session_factory = None
        self._engine_kwargs = engine_kwargs or {}
    
    @property
    def engine(self) -> Engine:
        """Get SQLAlchemy engine.
        
        Returns:
            Database engine
        
        Raises:
            RuntimeError: If engine is not initialized
        """
        if self._engine is None:
            raise RuntimeError("Database engine not initialized")
        return self._engine
    
    def initialize(self) -> None:
        """Initialize database connection."""
        if self._engine is not None:
            return
        
        try:
            # Create engine
            engine_config = {
                **self.config.engine_config,
                **self._engine_kwargs
            }
            
            self._engine = create_engine(
                self.config.connection_string,
                **engine_config
            )
            
            # Create session factory
            self._session_factory = sessionmaker(
                bind=self._engine,
                expire_on_commit=False
            )
            
            logger.info("Database connection initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise
    
    def dispose(self) -> None:
        """Dispose of database connection."""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None
            self._session_factory = None
            logger.info("Database connection disposed")
    
    @contextmanager
    def session(self) -> Session:
        """Get database session.
        
        Yields:
            Database session
        
        Raises:
            RuntimeError: If session factory is not initialized
        """
        if self._session_factory is None:
            raise RuntimeError("Database not initialized")
        
        session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def check_connection(self) -> bool:
        """Check if database connection is working.
        
        Returns:
            True if connection is working
        """
        try:
            with self.session() as session:
                session.execute("SELECT 1")
            return True
        except Exception as e:
            logger.error(f"Database connection check failed: {e}")
            return False
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get database metadata.
        
        Returns:
            Dictionary with database metadata
        """
        return {
            "host": self.config.host,
            "port": self.config.port,
            "database": self.config.database,
            "schema": self.config.schema,
            "pool_size": self.config.pool_size,
            "max_overflow": self.config.max_overflow
        }
    
    def __enter__(self) -> "DatabaseConnection":
        """Context manager entry.
        
        Returns:
            Self
        """
        self.initialize()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.dispose()
