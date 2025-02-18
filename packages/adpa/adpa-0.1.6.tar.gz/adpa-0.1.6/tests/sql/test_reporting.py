"""Test reporting and visualization tools."""
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from jinja2 import Environment, FileSystemLoader


class TestReport:
    """Test report generator and visualizer."""

    def __init__(self, report_dir: str = "test_reports"):
        """Initialize test report generator.
        
        Args:
            report_dir: Directory to store reports
        """
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(exist_ok=True)
        self.performance_data: Dict[str, List[float]] = {}
        self.error_data: Dict[str, int] = {}
        self.load_data: Dict[str, List[Dict[str, float]]] = {}
        
        # Set up Jinja2 environment
        self.template_dir = Path(__file__).parent / "templates"
        self.template_dir.mkdir(exist_ok=True)
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        
        # Create default HTML template if it doesn't exist
        self._create_default_template()
        
        # Set up plotting style
        plt.style.use("seaborn")
        sns.set_palette("husl")

    def _create_default_template(self) -> None:
        """Create default HTML template for reports."""
        template_path = self.template_dir / "report_template.html"
        if not template_path.exists():
            template_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>{{ title }}</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; }
                    .metric { margin: 10px 0; }
                    .chart { margin: 20px 0; }
                    .success { color: green; }
                    .warning { color: orange; }
                    .error { color: red; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f5f5f5; }
                </style>
            </head>
            <body>
                <h1>{{ title }}</h1>
                <div class="section">
                    <h2>Test Summary</h2>
                    <div class="metric">Total Tests: {{ total_tests }}</div>
                    <div class="metric">Passed: <span class="success">{{ passed_tests }}</span></div>
                    <div class="metric">Failed: <span class="error">{{ failed_tests }}</span></div>
                    <div class="metric">Duration: {{ duration }} seconds</div>
                </div>
                
                <div class="section">
                    <h2>Performance Metrics</h2>
                    {% for metric in performance_metrics %}
                    <div class="metric">
                        <h3>{{ metric.name }}</h3>
                        <div>Average: {{ metric.average }}</div>
                        <div>P95: {{ metric.p95 }}</div>
                        <div>Max: {{ metric.max }}</div>
                    </div>
                    {% endfor %}
                </div>
                
                <div class="section">
                    <h2>Error Analysis</h2>
                    <table>
                        <tr>
                            <th>Error Type</th>
                            <th>Count</th>
                            <th>Impact</th>
                        </tr>
                        {% for error in errors %}
                        <tr>
                            <td>{{ error.type }}</td>
                            <td>{{ error.count }}</td>
                            <td class="{{ error.severity }}">{{ error.impact }}</td>
                        </tr>
                        {% endfor %}
                    </table>
                </div>
                
                <div class="section">
                    <h2>Charts</h2>
                    {% for chart in charts %}
                    <div class="chart">
                        <h3>{{ chart.title }}</h3>
                        <img src="{{ chart.path }}" alt="{{ chart.title }}">
                    </div>
                    {% endfor %}
                </div>
            </body>
            </html>
            """
            template_path.write_text(template_content)

    def add_performance_data(self, test_name: str, duration: float) -> None:
        """Add performance data point.
        
        Args:
            test_name: Name of the test
            duration: Execution time in seconds
        """
        if test_name not in self.performance_data:
            self.performance_data[test_name] = []
        self.performance_data[test_name].append(duration)

    def add_error_data(self, error_type: str) -> None:
        """Add error occurrence.
        
        Args:
            error_type: Type of error encountered
        """
        self.error_data[error_type] = self.error_data.get(error_type, 0) + 1

    def add_load_data(self, test_name: str, metrics: Dict[str, float]) -> None:
        """Add load test metrics.
        
        Args:
            test_name: Name of the load test
            metrics: Dictionary of metrics (e.g., response_time, throughput)
        """
        if test_name not in self.load_data:
            self.load_data[test_name] = []
        self.load_data[test_name].append(metrics)

    def plot_performance_distribution(self, output_path: Optional[str] = None) -> str:
        """Plot performance distribution for each test.
        
        Args:
            output_path: Optional path to save the plot
            
        Returns:
            Path to the saved plot
        """
        plt.figure(figsize=(12, 6))
        
        data = []
        for test_name, durations in self.performance_data.items():
            for duration in durations:
                data.append({"Test": test_name, "Duration": duration})
        
        df = pd.DataFrame(data)
        sns.boxplot(x="Test", y="Duration", data=df)
        plt.xticks(rotation=45)
        plt.title("Test Performance Distribution")
        
        if output_path is None:
            output_path = str(self.report_dir / "performance_distribution.png")
        plt.savefig(output_path, bbox_inches="tight")
        plt.close()
        
        return output_path

    def plot_error_distribution(self, output_path: Optional[str] = None) -> str:
        """Plot error distribution.
        
        Args:
            output_path: Optional path to save the plot
            
        Returns:
            Path to the saved plot
        """
        plt.figure(figsize=(10, 6))
        
        error_types = list(self.error_data.keys())
        error_counts = list(self.error_data.values())
        
        plt.bar(error_types, error_counts)
        plt.xticks(rotation=45)
        plt.title("Error Distribution")
        plt.ylabel("Count")
        
        if output_path is None:
            output_path = str(self.report_dir / "error_distribution.png")
        plt.savefig(output_path, bbox_inches="tight")
        plt.close()
        
        return output_path

    def plot_load_test_results(self, output_path: Optional[str] = None) -> str:
        """Plot load test results.
        
        Args:
            output_path: Optional path to save the plot
            
        Returns:
            Path to the saved plot
        """
        plt.figure(figsize=(12, 6))
        
        data = []
        for test_name, metrics_list in self.load_data.items():
            for i, metrics in enumerate(metrics_list):
                metrics["Test"] = test_name
                metrics["Sequence"] = i
                data.append(metrics)
        
        df = pd.DataFrame(data)
        
        plt.subplot(2, 1, 1)
        sns.lineplot(data=df, x="Sequence", y="response_time", hue="Test")
        plt.title("Response Time Over Time")
        
        plt.subplot(2, 1, 2)
        sns.lineplot(data=df, x="Sequence", y="throughput", hue="Test")
        plt.title("Throughput Over Time")
        
        if output_path is None:
            output_path = str(self.report_dir / "load_test_results.png")
        plt.savefig(output_path, bbox_inches="tight")
        plt.close()
        
        return output_path

    def generate_report(self, title: str = "Test Report") -> str:
        """Generate HTML test report.
        
        Args:
            title: Report title
            
        Returns:
            Path to the generated report
        """
        template = self.env.get_template("report_template.html")
        
        # Generate charts
        charts = [
            {
                "title": "Performance Distribution",
                "path": self.plot_performance_distribution()
            },
            {
                "title": "Error Distribution",
                "path": self.plot_error_distribution()
            },
            {
                "title": "Load Test Results",
                "path": self.plot_load_test_results()
            }
        ]
        
        # Calculate metrics
        total_tests = sum(len(durations) for durations in self.performance_data.values())
        failed_tests = sum(self.error_data.values())
        passed_tests = total_tests - failed_tests
        
        # Calculate performance metrics
        performance_metrics = []
        for test_name, durations in self.performance_data.items():
            df = pd.Series(durations)
            performance_metrics.append({
                "name": test_name,
                "average": f"{df.mean():.3f}s",
                "p95": f"{df.quantile(0.95):.3f}s",
                "max": f"{df.max():.3f}s"
            })
        
        # Prepare error analysis
        errors = []
        for error_type, count in self.error_data.items():
            severity = "warning" if count < 3 else "error"
            impact = "Low" if count < 3 else "High"
            errors.append({
                "type": error_type,
                "count": count,
                "severity": severity,
                "impact": impact
            })
        
        # Generate report
        context = {
            "title": title,
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "failed_tests": failed_tests,
            "duration": sum(sum(d) for d in self.performance_data.values()),
            "performance_metrics": performance_metrics,
            "errors": errors,
            "charts": charts
        }
        
        report_path = self.report_dir / f"report_{int(time.time())}.html"
        report_path.write_text(template.render(context))
        
        return str(report_path)

    def save_data(self) -> None:
        """Save test data to JSON file."""
        data = {
            "performance": self.performance_data,
            "errors": self.error_data,
            "load": self.load_data,
            "timestamp": datetime.now().isoformat()
        }
        
        data_path = self.report_dir / f"test_data_{int(time.time())}.json"
        with open(data_path, "w") as f:
            json.dump(data, f, indent=2)

    def load_data_from_file(self, file_path: str) -> None:
        """Load test data from JSON file.
        
        Args:
            file_path: Path to JSON data file
        """
        with open(file_path) as f:
            data = json.load(f)
        
        self.performance_data = data["performance"]
        self.error_data = data["errors"]
        self.load_data = data["load"]


if __name__ == "__main__":
    # Example usage
    report = TestReport()
    
    # Add some test data
    report.add_performance_data("test_simple_query", 0.1)
    report.add_performance_data("test_complex_query", 0.5)
    report.add_error_data("ConnectionError")
    report.add_error_data("TimeoutError")
    report.add_load_data("normal_load", {
        "response_time": 0.2,
        "throughput": 100
    })
    
    # Generate report
    report_path = report.generate_report("SQL Test Report")
    print(f"Report generated: {report_path}")
    
    # Save data
    report.save_data()
