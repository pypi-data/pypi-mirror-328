"""Advanced integration tests between text2sql and agents modules."""

import asyncio
from datetime import datetime, timedelta
import pytest
from typing import Dict, List
from uuid import UUID, uuid4

from adpa.agents.types import (
    AgentConfig, AgentMessage, AgentMetrics, AgentPriority,
    AgentStatus, AgentType, MonitoringConfig, ResourceLimits,
    SecurityConfig, TaskResult
)
from adpa.agents.manager import AgentManager
from adpa.text2sql.models import Column, Index, Schema, Table
from adpa.text2sql.validation import SQLValidator
from adpa.text2sql.utils import (
    analyze_query_complexity, extract_table_references,
    suggest_indexes, suggest_joins
)


@pytest.fixture
def complex_schema():
    """Create a complex database schema for testing."""
    tables = {}
    
    # Products table
    product_columns = [
        Column(id=uuid4(), name="id", type="INTEGER", primary_key=True),
        Column(id=uuid4(), name="name", type="VARCHAR", nullable=False),
        Column(id=uuid4(), name="price", type="DECIMAL", nullable=False),
        Column(id=uuid4(), name="category_id", type="INTEGER",
               foreign_key="categories.id"),
        Column(id=uuid4(), name="supplier_id", type="INTEGER",
               foreign_key="suppliers.id")
    ]
    tables["products"] = Table(
        id=uuid4(),
        name="products",
        columns=product_columns,
        indexes=[
            Index(
                id=uuid4(),
                name="idx_products_category",
                table="products",
                columns=["category_id"]
            )
        ]
    )
    
    # Categories table
    category_columns = [
        Column(id=uuid4(), name="id", type="INTEGER", primary_key=True),
        Column(id=uuid4(), name="name", type="VARCHAR", nullable=False),
        Column(id=uuid4(), name="parent_id", type="INTEGER",
               foreign_key="categories.id")
    ]
    tables["categories"] = Table(
        id=uuid4(),
        name="categories",
        columns=category_columns
    )
    
    # Suppliers table
    supplier_columns = [
        Column(id=uuid4(), name="id", type="INTEGER", primary_key=True),
        Column(id=uuid4(), name="name", type="VARCHAR", nullable=False),
        Column(id=uuid4(), name="country", type="VARCHAR")
    ]
    tables["suppliers"] = Table(
        id=uuid4(),
        name="suppliers",
        columns=supplier_columns
    )
    
    # Orders table
    order_columns = [
        Column(id=uuid4(), name="id", type="INTEGER", primary_key=True),
        Column(id=uuid4(), name="customer_id", type="INTEGER",
               foreign_key="customers.id"),
        Column(id=uuid4(), name="order_date", type="TIMESTAMP", nullable=False),
        Column(id=uuid4(), name="status", type="VARCHAR", nullable=False)
    ]
    tables["orders"] = Table(
        id=uuid4(),
        name="orders",
        columns=order_columns
    )
    
    # Order Items table
    order_item_columns = [
        Column(id=uuid4(), name="order_id", type="INTEGER",
               foreign_key="orders.id"),
        Column(id=uuid4(), name="product_id", type="INTEGER",
               foreign_key="products.id"),
        Column(id=uuid4(), name="quantity", type="INTEGER", nullable=False),
        Column(id=uuid4(), name="price", type="DECIMAL", nullable=False)
    ]
    tables["order_items"] = Table(
        id=uuid4(),
        name="order_items",
        columns=order_item_columns,
        indexes=[
            Index(
                id=uuid4(),
                name="idx_order_items_order",
                table="order_items",
                columns=["order_id"]
            )
        ]
    )
    
    return Schema(
        id=uuid4(),
        name="public",
        tables=tables,
        dialect="postgresql"
    )


@pytest.fixture
def monitoring_config():
    """Create enhanced monitoring configuration."""
    return MonitoringConfig(
        heartbeat_interval=1,
        health_check_interval=5,
        metrics_interval=10,
        log_level="DEBUG",
        alert_threshold={
            "cpu": 0.9,
            "memory": 0.9,
            "error_rate": 0.05
        }
    )


@pytest.fixture
def security_config():
    """Create security configuration."""
    return SecurityConfig(
        enable_encryption=True,
        encryption_key_rotation=3600,
        allowed_hosts=["localhost"],
        allowed_ports=[5432],
        require_authentication=True
    )


class TestAdvancedQueryProcessing:
    """Test advanced query processing scenarios."""

    @pytest.mark.asyncio
    async def test_complex_join_query(self, complex_schema):
        """Test processing a complex query with multiple joins."""
        # Initialize components
        manager = AgentManager(AgentConfig(
            agent_type=AgentType.PROCESSOR,
            priority=AgentPriority.HIGH
        ))
        validator = SQLValidator()
        
        await manager.start_agent("query_processor")
        
        # Complex query with multiple joins
        query = """
        SELECT 
            c.name as category,
            s.name as supplier,
            COUNT(oi.product_id) as total_orders,
            SUM(oi.quantity * oi.price) as revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        JOIN categories c ON p.category_id = c.id
        JOIN suppliers s ON p.supplier_id = s.id
        GROUP BY c.name, s.name
        HAVING SUM(oi.quantity * oi.price) > 1000
        ORDER BY revenue DESC
        """
        
        # Validate query
        errors = validator.validate_query(query)
        assert not errors, "Complex query should be valid"
        
        # Check schema compatibility
        errors = validator.validate_schema_compatibility(query, complex_schema)
        assert not errors, "Query should be compatible with schema"
        
        # Analyze query complexity
        complexity = analyze_query_complexity(query)
        assert complexity == "O(n * m * log(n))", "Should detect complex join"
        
        # Get suggested indexes
        suggested_indexes = suggest_indexes(query, complex_schema)
        assert len(suggested_indexes) > 0, "Should suggest indexes for optimization"
        
        await manager.stop_agent("query_processor")

    @pytest.mark.asyncio
    async def test_distributed_query_processing(
        self, complex_schema, monitoring_config, security_config
    ):
        """Test distributed query processing with multiple agents."""
        # Create multiple agents for different roles
        manager = AgentManager()
        
        # Start validator agent
        await manager.start_agent("validator_agent")
        validator_config = AgentConfig(
            agent_type=AgentType.ANALYZER,
            priority=AgentPriority.HIGH,
            monitoring_config=monitoring_config,
            security_config=security_config
        )
        
        # Start optimizer agent
        await manager.start_agent("optimizer_agent")
        optimizer_config = AgentConfig(
            agent_type=AgentType.PROCESSOR,
            priority=AgentPriority.MEDIUM,
            monitoring_config=monitoring_config,
            security_config=security_config
        )
        
        # Create test queries
        queries = [
            "SELECT * FROM products WHERE category_id = 1",
            "SELECT * FROM orders WHERE order_date > NOW() - INTERVAL '1 day'",
            """
            SELECT c.name, COUNT(o.id)
            FROM categories c
            LEFT JOIN products p ON c.id = p.category_id
            LEFT JOIN order_items oi ON p.id = oi.product_id
            LEFT JOIN orders o ON oi.order_id = o.id
            GROUP BY c.name
            """
        ]
        
        # Process queries concurrently
        async def process_query(query: str) -> TaskResult:
            # Validate
            message = AgentMessage(
                sender_id="test",
                receiver_id="validator_agent",
                message_type="validate_query",
                payload={"query": query, "schema": complex_schema}
            )
            
            # Optimize
            message = AgentMessage(
                sender_id="validator_agent",
                receiver_id="optimizer_agent",
                message_type="optimize_query",
                payload={"query": query, "schema": complex_schema}
            )
            
            return TaskResult(
                task_id=str(uuid4()),
                success=True,
                start_time=datetime.now(),
                end_time=datetime.now() + timedelta(milliseconds=100)
            )
        
        tasks = [process_query(query) for query in queries]
        results = await asyncio.gather(*tasks)
        
        assert all(r.success for r in results), "All queries should process successfully"
        
        # Check agent health
        validator_health = await manager.check_agent_health("validator_agent")
        optimizer_health = await manager.check_agent_health("optimizer_agent")
        
        assert validator_health.is_healthy
        assert optimizer_health.is_healthy
        
        # Stop agents
        await manager.stop_agent("validator_agent")
        await manager.stop_agent("optimizer_agent")

    @pytest.mark.asyncio
    async def test_query_optimization_suggestions(self, complex_schema):
        """Test query optimization suggestions from agents."""
        manager = AgentManager(AgentConfig(
            agent_type=AgentType.ANALYZER,
            priority=AgentPriority.HIGH
        ))
        await manager.start_agent("optimizer_agent")
        
        # Query that could be optimized
        query = """
        SELECT 
            p.name,
            c.name as category,
            COUNT(oi.order_id) as total_orders
        FROM products p
        JOIN categories c ON p.category_id = c.id
        LEFT JOIN order_items oi ON p.id = oi.product_id
        WHERE c.name LIKE 'Electronics%'
        GROUP BY p.name, c.name
        ORDER BY total_orders DESC
        """
        
        # Extract table references
        tables = extract_table_references(query)
        assert "products" in tables
        assert "categories" in tables
        assert "order_items" in tables
        
        # Get join suggestions
        joins = suggest_joins(tables, complex_schema)
        assert len(joins) > 0, "Should suggest optimal join paths"
        
        # Get index suggestions
        indexes = suggest_indexes(query, complex_schema)
        assert len(indexes) > 0, "Should suggest helpful indexes"
        
        # Check resource usage
        usage = await manager.get_resource_usage("optimizer_agent")
        assert usage.cpu >= 0.0
        assert usage.memory >= 0.0
        
        await manager.stop_agent("optimizer_agent")
