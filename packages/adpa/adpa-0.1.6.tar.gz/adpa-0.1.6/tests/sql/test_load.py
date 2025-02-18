"""Load testing for SQL functionality."""
import pytest
import asyncio
import time
import statistics
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any
from fastapi import FastAPI
from fastapi.testclient import TestClient
from adpa.sql.generator import SQLGenerator, SQLGenerationConfig
from adpa.sql.validation import SQLValidator
from adpa.sql.middleware import SQLMiddleware


@pytest.fixture
def app():
    """Create test FastAPI application."""
    app = FastAPI()
    engine = create_engine("sqlite:///:memory:")
    generator = SQLGenerator(SQLGenerationConfig(), engine)
    validator = SQLValidator(engine)
    
    app.add_middleware(
        SQLMiddleware,
        generator=generator,
        validator=validator
    )
    
    @app.post("/query")
    async def query(request_data: dict):
        return {"status": "success"}
    
    return app


class LoadTestMetrics:
    """Load test metrics collector."""

    def __init__(self):
        """Initialize metrics."""
        self.response_times: List[float] = []
        self.error_count: int = 0
        self.success_count: int = 0
        self.start_time: float = 0
        self.end_time: float = 0

    def start(self):
        """Start load test."""
        self.start_time = time.time()

    def stop(self):
        """Stop load test."""
        self.end_time = time.time()

    def add_response(self, duration: float, success: bool):
        """Add response measurement."""
        self.response_times.append(duration)
        if success:
            self.success_count += 1
        else:
            self.error_count += 1

    def get_stats(self) -> Dict[str, Any]:
        """Get statistical summary."""
        total_time = self.end_time - self.start_time
        total_requests = self.success_count + self.error_count
        
        return {
            "total_time": total_time,
            "total_requests": total_requests,
            "requests_per_second": total_requests / total_time,
            "success_rate": self.success_count / total_requests * 100,
            "error_rate": self.error_count / total_requests * 100,
            "response_time": {
                "mean": statistics.mean(self.response_times),
                "median": statistics.median(self.response_times),
                "p95": statistics.quantiles(self.response_times, n=20)[18],
                "p99": statistics.quantiles(self.response_times, n=100)[98],
                "min": min(self.response_times),
                "max": max(self.response_times)
            }
        }


async def run_load_test(
    client: TestClient,
    total_users: int,
    requests_per_user: int,
    metrics: LoadTestMetrics
) -> None:
    """Run load test with specified parameters."""
    async def user_session(user_id: int):
        """Simulate single user session."""
        queries = [
            "Show all users",
            "Show active orders",
            "Show total sales by month",
            "Show top customers",
            "Show product inventory"
        ]
        
        for i in range(requests_per_user):
            query = queries[i % len(queries)]
            start_time = time.time()
            try:
                response = client.post(
                    "/query",
                    json={"query": query, "user_id": user_id}
                )
                success = response.status_code == 200
            except Exception:
                success = False
            
            duration = time.time() - start_time
            metrics.add_response(duration, success)
            
            # Simulate think time
            await asyncio.sleep(0.1)

    metrics.start()
    tasks = [user_session(i) for i in range(total_users)]
    await asyncio.gather(*tasks)
    metrics.stop()


def test_should_handle_normal_load(app):
    """Test system under normal load."""
    client = TestClient(app)
    metrics = LoadTestMetrics()
    
    asyncio.run(run_load_test(
        client=client,
        total_users=10,
        requests_per_user=10,
        metrics=metrics
    ))
    
    stats = metrics.get_stats()
    assert stats["success_rate"] > 95
    assert stats["response_time"]["p95"] < 0.5  # 500ms


def test_should_handle_heavy_load(app):
    """Test system under heavy load."""
    client = TestClient(app)
    metrics = LoadTestMetrics()
    
    asyncio.run(run_load_test(
        client=client,
        total_users=50,
        requests_per_user=20,
        metrics=metrics
    ))
    
    stats = metrics.get_stats()
    assert stats["success_rate"] > 90
    assert stats["response_time"]["p99"] < 1.0  # 1s


def test_should_handle_spike_load(app):
    """Test system under spike load."""
    client = TestClient(app)
    metrics = LoadTestMetrics()
    
    # First normal load
    asyncio.run(run_load_test(
        client=client,
        total_users=10,
        requests_per_user=5,
        metrics=metrics
    ))
    
    # Then spike
    asyncio.run(run_load_test(
        client=client,
        total_users=100,
        requests_per_user=5,
        metrics=metrics
    ))
    
    stats = metrics.get_stats()
    assert stats["success_rate"] > 85


def test_should_handle_sustained_load(app):
    """Test system under sustained load."""
    client = TestClient(app)
    metrics = LoadTestMetrics()
    
    for _ in range(5):
        asyncio.run(run_load_test(
            client=client,
            total_users=20,
            requests_per_user=10,
            metrics=metrics
        ))
        time.sleep(1)  # Brief pause between waves
    
    stats = metrics.get_stats()
    assert stats["success_rate"] > 90


def test_should_handle_concurrent_complex_queries(app):
    """Test system with concurrent complex queries."""
    client = TestClient(app)
    metrics = LoadTestMetrics()
    
    complex_queries = [
        "Show users who made more than 5 orders last month",
        "Calculate average order value by product category",
        "Show top selling products by region",
        "Find customers with abandoned carts",
        "Generate sales report with year-over-year comparison"
    ]
    
    async def run_complex_queries():
        tasks = []
        for query in complex_queries:
            task = client.post("/query", json={"query": query})
            tasks.append(task)
        return await asyncio.gather(*tasks)
    
    metrics.start()
    responses = asyncio.run(run_complex_queries())
    metrics.stop()
    
    assert all(r.status_code == 200 for r in responses)
    stats = metrics.get_stats()
    assert stats["response_time"]["max"] < 2.0  # 2s


def test_should_handle_mixed_query_types(app):
    """Test system with mix of simple and complex queries."""
    client = TestClient(app)
    metrics = LoadTestMetrics()
    
    async def mixed_query_session():
        queries = [
            "Show all users",  # Simple
            "Show users with high-value orders",  # Complex
            "List products",  # Simple
            "Show sales trends by category",  # Complex
            "Count active users"  # Simple
        ]
        
        for query in queries:
            start_time = time.time()
            response = client.post("/query", json={"query": query})
            duration = time.time() - start_time
            metrics.add_response(duration, response.status_code == 200)
    
    metrics.start()
    asyncio.run(mixed_query_session())
    metrics.stop()
    
    stats = metrics.get_stats()
    assert stats["success_rate"] == 100


def print_load_test_results(metrics: LoadTestMetrics) -> None:
    """Print formatted load test results."""
    stats = metrics.get_stats()
    
    print("\nLoad Test Results")
    print("================")
    
    print(f"\nTotal Time: {stats['total_time']:.2f} seconds")
    print(f"Total Requests: {stats['total_requests']}")
    print(f"Requests/Second: {stats['requests_per_second']:.2f}")
    print(f"Success Rate: {stats['success_rate']:.2f}%")
    print(f"Error Rate: {stats['error_rate']:.2f}%")
    
    print("\nResponse Time Statistics (seconds):")
    print(f"  Mean:   {stats['response_time']['mean']:.4f}")
    print(f"  Median: {stats['response_time']['median']:.4f}")
    print(f"  P95:    {stats['response_time']['p95']:.4f}")
    print(f"  P99:    {stats['response_time']['p99']:.4f}")
    print(f"  Min:    {stats['response_time']['min']:.4f}")
    print(f"  Max:    {stats['response_time']['max']:.4f}")


if __name__ == "__main__":
    # Run load tests
    app = FastAPI()
    metrics = LoadTestMetrics()
    
    test_should_handle_normal_load(app)
    test_should_handle_heavy_load(app)
    test_should_handle_spike_load(app)
    test_should_handle_sustained_load(app)
    test_should_handle_concurrent_complex_queries(app)
    test_should_handle_mixed_query_types(app)
    
    print_load_test_results(metrics)
