"""Database manager for ADPA framework."""
import asyncio
import logging
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Dict, List, Optional, Sequence, TypeVar, overload

from sqlalchemy import URL, Engine, create_engine, text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Session, sessionmaker

from ..core.exceptions import DatabaseError
from ..core.types import DBConfig

logger = logging.getLogger(__name__)
T = TypeVar("T")


class DatabaseManager:
    """Database manager for handling database connections and operations."""

    def __init__(self, config: DBConfig) -> None:
        """Initialize database manager.

        Args:
            config: Database configuration
        """
        self.config = config
        self._sync_engine: Optional[Engine] = None
        self._async_engine: Optional[AsyncEngine] = None
        self._sync_session_factory: Optional[sessionmaker[Session]] = None
        self._async_session_factory: Optional[async_sessionmaker[AsyncSession]] = None

    def _create_url(self) -> URL:
        """Create database URL from configuration.

        Returns:
            Database URL
        """
        return URL.create(
            "postgresql+asyncpg",
            username=self.config["user"],
            password=self.config["password"],
            host=self.config["host"],
            port=self.config["port"],
            database=self.config["database"],
        )

    def _create_engines(self) -> None:
        """Create database engines."""
        url = self._create_url()
        
        if not self._sync_engine:
            self._sync_engine = create_engine(
                url.set(drivername="postgresql+psycopg"),
                pool_size=self.config.get("pool_size", 5),
                max_overflow=self.config.get("max_overflow", 10),
                pool_timeout=30,
                pool_recycle=1800,
                echo=False,
            )
            self._sync_session_factory = sessionmaker(
                bind=self._sync_engine,
                expire_on_commit=False,
            )

        if not self._async_engine:
            self._async_engine = create_async_engine(
                url,
                pool_size=self.config.get("pool_size", 5),
                max_overflow=self.config.get("max_overflow", 10),
                pool_timeout=30,
                pool_recycle=1800,
                echo=False,
            )
            self._async_session_factory = async_sessionmaker(
                bind=self._async_engine,
                expire_on_commit=False,
            )

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get async database session.

        Yields:
            Database session

        Raises:
            DatabaseError: If session creation fails
        """
        if not self._async_session_factory:
            self._create_engines()
            if not self._async_session_factory:
                raise DatabaseError("Failed to create async session factory")

        session = self._async_session_factory()
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise DatabaseError(f"Database session error: {e}") from e
        finally:
            await session.close()

    @overload
    async def execute(
        self, query: str, params: Optional[Dict[str, Any]] = None
    ) -> Sequence[Dict[str, Any]]:
        ...

    @overload
    async def execute(
        self, query: str, params: Optional[Dict[str, Any]] = None, result_type: type[T] = None
    ) -> Sequence[T]:
        ...

    async def execute(
        self,
        query: str,
        params: Optional[Dict[str, Any]] = None,
        result_type: Optional[type[T]] = None,
    ) -> Sequence[Dict[str, Any]] | Sequence[T]:
        """Execute SQL query.

        Args:
            query: SQL query
            params: Query parameters
            result_type: Optional type for result mapping

        Returns:
            Query results

        Raises:
            DatabaseError: If query execution fails
        """
        async with self.session() as session:
            try:
                result = await session.execute(text(query), params or {})
                if result_type:
                    return [result_type(**row._mapping) for row in result]
                return [dict(row._mapping) for row in result]
            except Exception as e:
                raise DatabaseError(f"Query execution error: {e}") from e

    async def execute_many(
        self, queries: List[tuple[str, Optional[Dict[str, Any]]]]
    ) -> List[Sequence[Dict[str, Any]]]:
        """Execute multiple SQL queries in a transaction.

        Args:
            queries: List of (query, params) tuples

        Returns:
            List of query results

        Raises:
            DatabaseError: If query execution fails
        """
        async with self.session() as session:
            try:
                results = []
                for query, params in queries:
                    result = await session.execute(text(query), params or {})
                    results.append([dict(row._mapping) for row in result])
                return results
            except Exception as e:
                raise DatabaseError(f"Batch query execution error: {e}") from e

    async def get_status(self) -> Dict[str, Any]:
        """Get database status.

        Returns:
            Database status information

        Raises:
            DatabaseError: If status check fails
        """
        async with self.session() as session:
            try:
                version = await session.execute(text("SELECT version()"))
                connections = await session.execute(
                    text(
                        """
                        SELECT count(*) as active_connections
                        FROM pg_stat_activity
                        WHERE state = 'active'
                        """
                    )
                )
                size = await session.execute(
                    text(
                        """
                        SELECT pg_size_pretty(pg_database_size(current_database()))
                        as db_size
                        """
                    )
                )

                return {
                    "version": version.scalar(),
                    "active_connections": connections.scalar(),
                    "database_size": size.scalar(),
                    "pool_size": self.config.get("pool_size", 5),
                    "max_overflow": self.config.get("max_overflow", 10),
                }
            except Exception as e:
                raise DatabaseError(f"Status check error: {e}") from e

    async def migrate(self) -> None:
        """Run database migrations.

        Raises:
            DatabaseError: If migration fails
        """
        # TODO: Implement migration logic using alembic
        raise NotImplementedError("Migration not implemented")

    async def backup(self, path: str) -> None:
        """Backup database.

        Args:
            path: Backup file path

        Raises:
            DatabaseError: If backup fails
        """
        # TODO: Implement backup logic
        raise NotImplementedError("Backup not implemented")

    async def restore(self, path: str) -> None:
        """Restore database from backup.

        Args:
            path: Backup file path

        Raises:
            DatabaseError: If restore fails
        """
        # TODO: Implement restore logic
        raise NotImplementedError("Restore not implemented")

    async def close(self) -> None:
        """Close database connections."""
        if self._async_engine:
            await self._async_engine.dispose()
            self._async_engine = None
            self._async_session_factory = None

        if self._sync_engine:
            self._sync_engine.dispose()
            self._sync_engine = None
            self._sync_session_factory = None
