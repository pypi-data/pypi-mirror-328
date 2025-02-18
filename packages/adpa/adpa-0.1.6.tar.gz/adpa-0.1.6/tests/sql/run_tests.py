"""Run all SQL tests and generate reports."""
import os
import time
import pytest
import asyncio
from typing import Dict, Any, List
from pathlib import Path
from test_reporting import TestReport
from test_performance import PerformanceMetrics
from test_load import LoadTestMetrics


class TestRunner:
    """Test runner with reporting."""

    def __init__(self):
        """Initialize test runner."""
        self.report = TestReport()
        self.test_dir = Path(__file__).parent
        self.results: Dict[str, Any] = {}

    async def run_all_tests(self) -> None:
        """Run all test suites."""
        # Run unit tests
        await self.run_unit_tests()
        
        # Run performance tests
        await self.run_performance_tests()
        
        # Run load tests
        await self.run_load_tests()
        
        # Generate report
        self.generate_report()

    async def run_unit_tests(self) -> None:
        """Run unit tests with pytest."""
        print("\nRunning unit tests...")
        
        # Collect test results using pytest
        result = pytest.main([
            str(self.test_dir / "test_generator.py"),
            str(self.test_dir / "test_validation.py"),
            str(self.test_dir / "test_error_recovery.py"),
            "-v"
        ])
        
        self.results["unit_tests"] = {
            "exit_code": result,
            "passed": result == 0
        }

    async def run_performance_tests(self) -> None:
        """Run performance tests."""
        print("\nRunning performance tests...")
        metrics = PerformanceMetrics()
        
        # Run performance tests
        test_files = [
            "test_generator.py",
            "test_validation.py",
            "test_middleware.py"
        ]
        
        for test_file in test_files:
            start_time = time.time()
            result = pytest.main([str(self.test_dir / test_file), "-v"])
            duration = time.time() - start_time
            
            # Record metrics
            self.report.add_performance_data(test_file, duration)
            
            if result != 0:
                self.report.add_error_data(f"PerformanceError_{test_file}")

    async def run_load_tests(self) -> None:
        """Run load tests."""
        print("\nRunning load tests...")
        metrics = LoadTestMetrics()
        
        # Define load test scenarios
        scenarios = [
            {"name": "normal_load", "users": 10, "requests": 10},
            {"name": "heavy_load", "users": 50, "requests": 20},
            {"name": "spike_load", "users": 100, "requests": 5}
        ]
        
        for scenario in scenarios:
            metrics.start()
            
            # Run load test scenario
            result = pytest.main([
                str(self.test_dir / "test_load.py"),
                "-v",
                f"--users={scenario['users']}",
                f"--requests={scenario['requests']}"
            ])
            
            metrics.stop()
            
            # Record metrics
            stats = metrics.get_stats()
            self.report.add_load_data(scenario["name"], {
                "response_time": stats["response_time"]["mean"],
                "throughput": stats["requests_per_second"]
            })
            
            if result != 0:
                self.report.add_error_data(f"LoadError_{scenario['name']}")

    def generate_report(self) -> str:
        """Generate comprehensive test report.
        
        Returns:
            Path to generated report
        """
        print("\nGenerating test report...")
        
        # Generate report with all collected data
        report_path = self.report.generate_report("SQL Functionality Test Report")
        
        # Save raw data
        self.report.save_data()
        
        print(f"\nTest report generated: {report_path}")
        return report_path


def main() -> None:
    """Main entry point."""
    # Set up asyncio event loop
    loop = asyncio.get_event_loop()
    
    # Create and run test runner
    runner = TestRunner()
    loop.run_until_complete(runner.run_all_tests())
    
    # Close event loop
    loop.close()


if __name__ == "__main__":
    main()
