"""Performance benchmarks for SQL functionality."""
import pytest
import time
import statistics
from typing import List, Dict, Any
from sqlalchemy import create_engine, text
from adpa.sql.generator import SQLGenerator, SQLGenerationConfig
from adpa.sql.validation import SQLValidator
from adpa.sql.middleware import SQLMiddleware


class PerformanceMetrics:
    """Collection of performance metrics."""

    def __init__(self) -> None:
        """Initialize metrics."""
        self.timings: List[float] = []
        self.memory_usage: List[float] = []
        self.cpu_usage: List[float] = []

    def add_timing(self, duration: float) -> None:
        """Add timing measurement."""
        self.timings.append(duration)

    def add_memory(self, usage: float) -> None:
        """Add memory usage measurement."""
        self.memory_usage.append(usage)

    def add_cpu(self, usage: float) -> None:
        """Add CPU usage measurement."""
        self.cpu_usage.append(usage)

    def get_stats(self) -> Dict[str, Any]:
        """Get statistical summary."""
        return {
            "timing": {
                "mean": statistics.mean(self.timings),
                "median": statistics.median(self.timings),
                "std_dev": statistics.stdev(self.timings) if len(self.timings) > 1 else 0,
                "min": min(self.timings),
                "max": max(self.timings)
            },
            "memory": {
                "mean": statistics.mean(self.memory_usage),
                "max": max(self.memory_usage)
            },
            "cpu": {
                "mean": statistics.mean(self.cpu_usage),
                "max": max(self.cpu_usage)
            }
        }


@pytest.fixture
def performance_metrics():
    """Create performance metrics collector."""
    return PerformanceMetrics()


@pytest.fixture
def benchmark_db():
    """Create benchmark database."""
    engine = create_engine("sqlite:///:memory:")
    
    # Create test tables
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                created_at TIMESTAMP
            )
        """))
        conn.execute(text("""
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                amount DECIMAL,
                status TEXT,
                created_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """))
        
        # Insert test data
        for i in range(1000):
            conn.execute(text(
                "INSERT INTO users (name, email, created_at) "
                "VALUES (:name, :email, CURRENT_TIMESTAMP)"
            ), {"name": f"User {i}", "email": f"user{i}@test.com"})
            
            # Create multiple orders per user
            for j in range(5):
                conn.execute(text(
                    "INSERT INTO orders (user_id, amount, status, created_at) "
                    "VALUES (:user_id, :amount, :status, CURRENT_TIMESTAMP)"
                ), {
                    "user_id": i + 1,
                    "amount": 100 * (j + 1),
                    "status": "completed"
                })
        
        conn.commit()
    
    return engine


def measure_performance(func):
    """Decorator to measure function performance."""
    def wrapper(*args, **kwargs):
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss / 1024 / 1024  # MB
        start_time = time.time()
        start_cpu = process.cpu_percent()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_memory = process.memory_info().rss / 1024 / 1024
        end_cpu = process.cpu_percent()
        
        metrics = kwargs.get("metrics")
        if metrics:
            metrics.add_timing(end_time - start_time)
            metrics.add_memory(end_memory - start_memory)
            metrics.add_cpu(end_cpu - start_cpu)
        
        return result
    return wrapper


@measure_performance
def test_should_benchmark_simple_query_generation(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark simple query generation."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    for _ in range(100):
        result = generator.generate_query("Show all users")
        assert result["success"]


@measure_performance
def test_should_benchmark_complex_query_generation(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark complex query generation."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    for _ in range(100):
        result = generator.generate_query(
            "Show me all users who have made more than 3 orders "
            "with total amount greater than 1000 in the last month"
        )
        assert result["success"]


@measure_performance
def test_should_benchmark_validation(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark query validation."""
    validator = SQLValidator(benchmark_db)
    
    queries = [
        "SELECT * FROM users LIMIT 10",
        "SELECT u.*, COUNT(o.id) FROM users u JOIN orders o ON u.id = o.user_id "
        "GROUP BY u.id HAVING COUNT(o.id) > 3",
        "SELECT * FROM users WHERE id IN (SELECT user_id FROM orders "
        "GROUP BY user_id HAVING SUM(amount) > 1000)"
    ]
    
    for query in queries:
        for _ in range(100):
            result = validator.validate_query(query)
            assert result.valid


@measure_performance
def test_should_benchmark_concurrent_requests(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark concurrent request handling."""
    import asyncio
    import httpx
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    
    app = FastAPI()
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    validator = SQLValidator(benchmark_db)
    
    app.add_middleware(
        SQLMiddleware,
        generator=generator,
        validator=validator
    )
    
    @app.post("/query")
    async def query(request_data: dict):
        return {"status": "success"}
    
    client = TestClient(app)
    
    async def make_requests():
        async with httpx.AsyncClient(app=app) as ac:
            tasks = []
            for _ in range(10):
                task = ac.post(
                    "/query",
                    json={"query": "Show active users"}
                )
                tasks.append(task)
            return await asyncio.gather(*tasks)
    
    for _ in range(10):
        responses = asyncio.run(make_requests())
        assert all(r.status_code == 200 for r in responses)


def test_should_report_performance_metrics(performance_metrics) -> None:
    """Test performance metrics reporting."""
    stats = performance_metrics.get_stats()
    
    # Timing checks
    assert stats["timing"]["mean"] < 0.1  # 100ms max average
    assert stats["timing"]["max"] < 0.5   # 500ms max spike
    
    # Memory checks
    assert stats["memory"]["mean"] < 100  # 100MB average
    assert stats["memory"]["max"] < 200   # 200MB max
    
    # CPU checks
    assert stats["cpu"]["mean"] < 50      # 50% average CPU
    assert stats["cpu"]["max"] < 80       # 80% max CPU


def print_benchmark_results(performance_metrics) -> None:
    """Print formatted benchmark results."""
    stats = performance_metrics.get_stats()
    
    print("\nPerformance Benchmark Results")
    print("============================")
    
    print("\nTiming Statistics (seconds):")
    print(f"  Mean:    {stats['timing']['mean']:.4f}")
    print(f"  Median:  {stats['timing']['median']:.4f}")
    print(f"  Std Dev: {stats['timing']['std_dev']:.4f}")
    print(f"  Min:     {stats['timing']['min']:.4f}")
    print(f"  Max:     {stats['timing']['max']:.4f}")
    
    print("\nMemory Usage (MB):")
    print(f"  Mean:    {stats['memory']['mean']:.2f}")
    print(f"  Max:     {stats['memory']['max']:.2f}")
    
    print("\nCPU Usage (%):")
    print(f"  Mean:    {stats['cpu']['mean']:.2f}")
    print(f"  Max:     {stats['cpu']['max']:.2f}")


@measure_performance
def test_should_benchmark_memory_intensive_queries(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark memory-intensive queries."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    # Queries that typically require significant memory
    queries = [
        "Show all user activity for the past year",
        "Calculate moving averages for all products",
        "Generate complete audit trail",
        "Show full order history with all details",
        "Create detailed sales report with all metrics"
    ]
    
    for query in queries:
        result = generator.generate_query(query)
        assert result["success"]


@measure_performance
def test_should_benchmark_cpu_intensive_queries(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark CPU-intensive queries."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    # Queries that typically require significant CPU
    queries = [
        "Calculate correlation between all metrics",
        "Generate predictive analysis for all products",
        "Perform complex statistical analysis",
        "Calculate percentiles for all numeric columns",
        "Generate optimization recommendations"
    ]
    
    for query in queries:
        result = generator.generate_query(query)
        assert result["success"]


@measure_performance
def test_should_benchmark_io_intensive_queries(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark I/O-intensive queries."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    # Queries that typically require significant I/O
    queries = [
        "Export all historical data",
        "Import and process large dataset",
        "Generate complete system backup",
        "Perform full data validation",
        "Rebuild all indexes"
    ]
    
    for query in queries:
        result = generator.generate_query(query)
        assert result["success"]


@measure_performance
def test_should_benchmark_query_optimization(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark query optimization process."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    # Queries that need optimization
    queries = [
        "Find users with complex conditions",
        "Calculate metrics with multiple joins",
        "Generate report with subqueries",
        "Analyze data with window functions",
        "Process hierarchical data"
    ]
    
    for query in queries:
        result = generator.generate_query(query)
        assert result["success"]
        assert "optimization" in result["phases"]


@measure_performance
def test_should_benchmark_parallel_processing(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark parallel query processing."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    async def process_queries():
        queries = [
            "Process batch 1",
            "Process batch 2",
            "Process batch 3",
            "Process batch 4",
            "Process batch 5"
        ]
        
        tasks = [
            asyncio.create_task(
                asyncio.to_thread(generator.generate_query, query)
            )
            for query in queries
        ]
        
        results = await asyncio.gather(*tasks)
        return results
    
    results = asyncio.run(process_queries())
    assert all(r["success"] for r in results)


@measure_performance
def test_should_benchmark_incremental_processing(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark incremental query processing."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    base_query = "Show user activity"
    conditions = [
        "from last week",
        "with high priority",
        "in specific region",
        "with certain status",
        "meeting criteria"
    ]
    
    query = base_query
    for condition in conditions:
        query += " " + condition
        result = generator.generate_query(query)
        assert result["success"]


@measure_performance
def test_should_benchmark_streaming_queries(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark streaming query processing."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    async def stream_queries():
        for i in range(100):
            query = f"Process stream batch {i}"
            result = await asyncio.to_thread(generator.generate_query, query)
            assert result["success"]
            await asyncio.sleep(0.01)  # Simulate streaming delay
    
    asyncio.run(stream_queries())


@measure_performance
def test_should_benchmark_cache_effectiveness(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark query cache effectiveness."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    # First run - should populate cache
    for i in range(5):
        query = f"Cached query {i}"
        result = generator.generate_query(query)
        assert result["success"]
    
    # Second run - should use cache
    start_time = time.time()
    for i in range(5):
        query = f"Cached query {i}"
        result = generator.generate_query(query)
        assert result["success"]
    cached_time = time.time() - start_time
    
    # Verify cache effectiveness
    assert cached_time < 0.1  # Should be very fast


@measure_performance
def test_should_benchmark_resource_cleanup(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark resource cleanup after queries."""
    import gc
    import psutil
    
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    process = psutil.Process()
    
    initial_memory = process.memory_info().rss
    
    # Run memory-intensive queries
    for i in range(10):
        query = f"Large query {i}"
        result = generator.generate_query(query)
        assert result["success"]
    
    # Force cleanup
    gc.collect()
    
    # Check memory usage
    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory
    assert memory_increase < 10 * 1024 * 1024  # Less than 10MB increase


@measure_performance
def test_should_benchmark_error_handling_performance(
    benchmark_db,
    performance_metrics
) -> None:
    """Benchmark performance of error handling."""
    generator = SQLGenerator(SQLGenerationConfig(), benchmark_db)
    
    def generate_with_error():
        try:
            generator.generate_query("Invalid query that will fail")
        except Exception:
            pass  # Expected to fail
    
    # Measure error handling time
    start_time = time.time()
    for _ in range(100):
        generate_with_error()
    error_handling_time = time.time() - start_time
    
    assert error_handling_time < 1.0  # Should handle errors quickly


if __name__ == "__main__":
    metrics = PerformanceMetrics()
    
    # Run benchmarks
    test_should_benchmark_simple_query_generation(metrics=metrics)
    test_should_benchmark_complex_query_generation(metrics=metrics)
    test_should_benchmark_validation(metrics=metrics)
    test_should_benchmark_concurrent_requests(metrics=metrics)
    test_should_benchmark_memory_intensive_queries(benchmark_db(), metrics)
    test_should_benchmark_cpu_intensive_queries(benchmark_db(), metrics)
    test_should_benchmark_io_intensive_queries(benchmark_db(), metrics)
    test_should_benchmark_query_optimization(benchmark_db(), metrics)
    test_should_benchmark_parallel_processing(benchmark_db(), metrics)
    test_should_benchmark_incremental_processing(benchmark_db(), metrics)
    test_should_benchmark_streaming_queries(benchmark_db(), metrics)
    test_should_benchmark_cache_effectiveness(benchmark_db(), metrics)
    test_should_benchmark_resource_cleanup(benchmark_db(), metrics)
    test_should_benchmark_error_handling_performance(benchmark_db(), metrics)
    
    print_benchmark_results(metrics)
