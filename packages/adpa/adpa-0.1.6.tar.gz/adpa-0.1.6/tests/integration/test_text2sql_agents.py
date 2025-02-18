"""Integration tests between text2sql and agents modules."""

import asyncio
from datetime import datetime
import pytest
from uuid import UUID, uuid4

from adpa.agents.types import (
    AgentConfig, AgentMessage, AgentPriority, AgentStatus,
    AgentType, ResourceLimits
)
from adpa.agents.manager import AgentManager
from adpa.text2sql.models import Column, Schema, Table, QueryTemplate
from adpa.text2sql.validation import SQLValidator
from adpa.text2sql.context import QueryContext


@pytest.fixture
def sample_schema():
    """Create a sample database schema."""
    # Create users table
    user_columns = [
        Column(
            id=uuid4(),
            name="id",
            type="INTEGER",
            primary_key=True
        ),
        Column(
            id=uuid4(),
            name="username",
            type="VARCHAR",
            nullable=False,
            unique=True
        ),
        Column(
            id=uuid4(),
            name="email",
            type="VARCHAR",
            nullable=False
        )
    ]
    users_table = Table(
        id=uuid4(),
        name="users",
        columns=user_columns
    )

    # Create orders table
    order_columns = [
        Column(
            id=uuid4(),
            name="id",
            type="INTEGER",
            primary_key=True
        ),
        Column(
            id=uuid4(),
            name="user_id",
            type="INTEGER",
            foreign_key="users.id"
        ),
        Column(
            id=uuid4(),
            name="total",
            type="DECIMAL"
        ),
        Column(
            id=uuid4(),
            name="created_at",
            type="TIMESTAMP",
            nullable=False
        )
    ]
    orders_table = Table(
        id=uuid4(),
        name="orders",
        columns=order_columns
    )

    return Schema(
        id=uuid4(),
        name="public",
        tables={
            "users": users_table,
            "orders": orders_table
        }
    )


@pytest.fixture
def query_processor_config():
    """Create configuration for query processor agent."""
    return AgentConfig(
        agent_type=AgentType.PROCESSOR,
        priority=AgentPriority.HIGH,
        resource_limits=ResourceLimits(
            max_memory="1G",
            max_cpu=1.0,
            max_tasks=10
        )
    )


@pytest.fixture
def query_validator():
    """Create SQL validator instance."""
    return SQLValidator()


class TestQueryProcessing:
    """Test query processing with agents."""

    @pytest.mark.asyncio
    async def test_process_valid_query(
        self, sample_schema, query_processor_config, query_validator
    ):
        """Test processing a valid SQL query through an agent."""
        # Initialize agent manager
        manager = AgentManager(query_processor_config)
        await manager.start_agent("query_processor")

        # Create query context
        context = QueryContext(schema=sample_schema)
        
        # Create query message
        query = "SELECT u.username, COUNT(o.id) as order_count " \
               "FROM users u JOIN orders o ON u.id = o.user_id " \
               "GROUP BY u.username"
        
        message = AgentMessage(
            sender_id="test",
            receiver_id="query_processor",
            message_type="process_query",
            payload={
                "query": query,
                "context": context,
                "validate": True
            }
        )

        # Validate query
        errors = query_validator.validate_query(query)
        assert not errors, "Query should be valid"

        # Check schema compatibility
        errors = query_validator.validate_schema_compatibility(
            query, sample_schema
        )
        assert not errors, "Query should be compatible with schema"

        # Check agent health
        health = await manager.check_agent_health("query_processor")
        assert health.is_healthy
        assert health.status == AgentStatus.RUNNING

        # Stop agent
        await manager.stop_agent("query_processor")

    @pytest.mark.asyncio
    async def test_process_invalid_query(
        self, sample_schema, query_processor_config, query_validator
    ):
        """Test processing an invalid SQL query through an agent."""
        # Initialize agent manager
        manager = AgentManager(query_processor_config)
        await manager.start_agent("query_processor")

        # Create query context
        context = QueryContext(schema=sample_schema)
        
        # Create query with SQL injection attempt
        query = "SELECT * FROM users; DROP TABLE users;"
        
        message = AgentMessage(
            sender_id="test",
            receiver_id="query_processor",
            message_type="process_query",
            payload={
                "query": query,
                "context": context,
                "validate": True
            }
        )

        # Validate query
        errors = query_validator.validate_query(query)
        assert errors, "Query should be invalid"
        assert "dangerous SQL pattern" in errors[0].message

        # Check agent health after processing invalid query
        health = await manager.check_agent_health("query_processor")
        assert health.is_healthy
        assert health.error_count == 0  # Error was caught by validation

        # Stop agent
        await manager.stop_agent("query_processor")

    @pytest.mark.asyncio
    async def test_concurrent_query_processing(
        self, sample_schema, query_processor_config, query_validator
    ):
        """Test processing multiple queries concurrently."""
        # Initialize agent manager
        manager = AgentManager(query_processor_config)
        await manager.start_agent("query_processor")

        # Create query context
        context = QueryContext(schema=sample_schema)
        
        # Create multiple queries
        queries = [
            "SELECT * FROM users WHERE id = 1",
            "SELECT * FROM orders WHERE user_id = 1",
            "SELECT u.username FROM users u JOIN orders o ON u.id = o.user_id"
        ]
        
        messages = [
            AgentMessage(
                sender_id="test",
                receiver_id="query_processor",
                message_type="process_query",
                payload={
                    "query": query,
                    "context": context,
                    "validate": True
                }
            )
            for query in queries
        ]

        # Validate all queries concurrently
        tasks = [
            query_validator.validate_query(query)
            for query in queries
        ]
        results = await asyncio.gather(*[
            asyncio.create_task(asyncio.sleep(0.1))  # Simulate processing
            for _ in tasks
        ])

        # Check agent resource usage
        usage = await manager.get_resource_usage("query_processor")
        assert usage.cpu >= 0.0
        assert usage.memory >= 0.0

        # Stop agent
        await manager.stop_agent("query_processor")

    @pytest.mark.asyncio
    async def test_query_template_processing(
        self, sample_schema, query_processor_config, query_validator
    ):
        """Test processing queries using templates."""
        # Initialize agent manager
        manager = AgentManager(query_processor_config)
        await manager.start_agent("query_processor")

        # Create query template
        template = QueryTemplate(
            id=uuid4(),
            name="user_orders",
            template="SELECT u.username, COUNT(o.id) as order_count " \
                    "FROM users u JOIN orders o ON u.id = o.user_id " \
                    "WHERE u.id = {user_id} " \
                    "GROUP BY u.username"
        )

        # Create query context
        context = QueryContext(schema=sample_schema)
        
        # Render and validate template
        query = template.render(user_id=1)
        errors = query_validator.validate_query(query)
        assert not errors, "Rendered query should be valid"

        # Check schema compatibility
        errors = query_validator.validate_schema_compatibility(
            query, sample_schema
        )
        assert not errors, "Rendered query should be compatible with schema"

        # Stop agent
        await manager.stop_agent("query_processor")
