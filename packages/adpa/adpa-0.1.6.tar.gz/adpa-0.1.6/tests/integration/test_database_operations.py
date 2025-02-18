"""Integration tests for database operations."""
import asyncio
import pytest
from typing import AsyncGenerator, Dict, List

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from adpa.database.models import Base, Query, Result
from adpa.database.operations import (
    create_query,
    get_query_by_id,
    update_query_status,
    delete_query,
    list_queries
)


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def db_engine():
    """Create a test database engine."""
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture
async def db_session(db_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create a test database session."""
    async_session = sessionmaker(
        db_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


@pytest.fixture
async def sample_query(db_session: AsyncSession) -> Dict:
    """Create a sample query for testing."""
    query_data = {
        "text": "Select all employees from HR department",
        "generated_sql": "SELECT * FROM employees WHERE department = 'HR'",
        "status": "completed",
        "metadata": {"department": "HR", "table": "employees"}
    }
    query = await create_query(db_session, **query_data)
    await db_session.commit()
    return {**query_data, "id": query.id}


@pytest.mark.asyncio
async def test_should_create_query(db_session: AsyncSession):
    """Test query creation."""
    query_data = {
        "text": "List all departments",
        "generated_sql": "SELECT DISTINCT department FROM employees",
        "status": "pending",
        "metadata": {"table": "employees"}
    }
    
    query = await create_query(db_session, **query_data)
    await db_session.commit()
    
    assert query.id is not None
    assert query.text == query_data["text"]
    assert query.generated_sql == query_data["generated_sql"]
    assert query.status == query_data["status"]
    assert query.metadata == query_data["metadata"]


@pytest.mark.asyncio
async def test_should_get_query_by_id(
    db_session: AsyncSession,
    sample_query: Dict
):
    """Test retrieving a query by ID."""
    query = await get_query_by_id(db_session, sample_query["id"])
    
    assert query is not None
    assert query.text == sample_query["text"]
    assert query.generated_sql == sample_query["generated_sql"]
    assert query.status == sample_query["status"]


@pytest.mark.asyncio
async def test_should_update_query_status(
    db_session: AsyncSession,
    sample_query: Dict
):
    """Test updating query status."""
    new_status = "failed"
    query = await update_query_status(
        db_session,
        sample_query["id"],
        new_status
    )
    await db_session.commit()
    
    assert query.status == new_status
    
    # Verify in database
    updated_query = await get_query_by_id(db_session, sample_query["id"])
    assert updated_query.status == new_status


@pytest.mark.asyncio
async def test_should_delete_query(
    db_session: AsyncSession,
    sample_query: Dict
):
    """Test query deletion."""
    await delete_query(db_session, sample_query["id"])
    await db_session.commit()
    
    # Verify deletion
    deleted_query = await get_query_by_id(db_session, sample_query["id"])
    assert deleted_query is None


@pytest.mark.asyncio
async def test_should_list_queries(
    db_session: AsyncSession,
    sample_query: Dict
):
    """Test listing queries with filters."""
    # Create additional queries
    queries_data = [
        {
            "text": "Count employees by department",
            "generated_sql": "SELECT department, COUNT(*) FROM employees GROUP BY department",
            "status": "completed",
            "metadata": {"operation": "count", "table": "employees"}
        },
        {
            "text": "Find highest paid employee",
            "generated_sql": "SELECT * FROM employees ORDER BY salary DESC LIMIT 1",
            "status": "failed",
            "metadata": {"operation": "max", "table": "employees"}
        }
    ]
    
    for query_data in queries_data:
        await create_query(db_session, **query_data)
    await db_session.commit()
    
    # Test listing all queries
    all_queries = await list_queries(db_session)
    assert len(all_queries) == 3  # Including sample_query
    
    # Test filtering by status
    completed_queries = await list_queries(
        db_session,
        filters={"status": "completed"}
    )
    assert len(completed_queries) == 2
    
    # Test filtering by metadata
    hr_queries = await list_queries(
        db_session,
        filters={"metadata": {"department": "HR"}}
    )
    assert len(hr_queries) == 1


@pytest.mark.asyncio
async def test_should_handle_concurrent_operations(
    db_session: AsyncSession,
    sample_query: Dict
):
    """Test handling of concurrent database operations."""
    async def update_status(session: AsyncSession, query_id: int, status: str):
        await update_query_status(session, query_id, status)
        await session.commit()
    
    # Create multiple concurrent update operations
    statuses = ["running", "completed", "failed"]
    tasks = [
        update_status(db_session, sample_query["id"], status)
        for status in statuses
    ]
    
    # Run updates concurrently
    await asyncio.gather(*tasks)
    
    # Verify final state
    final_query = await get_query_by_id(db_session, sample_query["id"])
    assert final_query.status in statuses


@pytest.mark.asyncio
async def test_should_handle_large_result_sets(db_session: AsyncSession):
    """Test handling of large result sets."""
    # Create multiple queries
    queries = []
    for i in range(100):
        query_data = {
            "text": f"Query {i}",
            "generated_sql": f"SELECT * FROM table_{i}",
            "status": "completed",
            "metadata": {"index": i}
        }
        query = await create_query(db_session, **query_data)
        queries.append(query)
    await db_session.commit()
    
    # Test pagination
    page_size = 10
    for page in range(10):
        offset = page * page_size
        results = await list_queries(
            db_session,
            limit=page_size,
            offset=offset
        )
        assert len(results) == page_size
        assert all(q.metadata["index"] >= offset for q in results)
        assert all(q.metadata["index"] < offset + page_size for q in results)
