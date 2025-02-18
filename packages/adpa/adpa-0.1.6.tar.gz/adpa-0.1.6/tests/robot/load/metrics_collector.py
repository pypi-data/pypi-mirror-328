"""Metrics collection and analysis for load tests."""
import psutil
import time
import json
import logging
import numpy as np
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

class MetricsCollector:
    """Collects and analyzes system metrics during load tests."""

    def __init__(self, test_id: str, output_dir: str = "results/load"):
        """Initialize metrics collector."""
        self.test_id = test_id
        self.output_dir = Path(output_dir) / test_id
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.metrics: Dict[str, List[Any]] = {
            'timestamp': [],
            'cpu_percent': [],
            'memory_percent': [],
            'disk_io': [],
            'network_io': [],
            'response_times': [],
            'errors': [],
            'active_users': []
        }
        self.start_time = None
        self.running = False
        self.logger = logging.getLogger(__name__)

    def start(self):
        """Start metrics collection."""
        self.start_time = time.time()
        self.running = True
        self._collect_metrics()

    def stop(self):
        """Stop metrics collection."""
        self.running = False
        self._save_metrics()
        self._generate_report()

    def _collect_metrics(self):
        """Collect system metrics."""
        while self.running:
            try:
                current_time = time.time()
                self.metrics['timestamp'].append(current_time)
                
                # CPU metrics
                self.metrics['cpu_percent'].append(psutil.cpu_percent(interval=1))
                
                # Memory metrics
                memory = psutil.virtual_memory()
                self.metrics['memory_percent'].append(memory.percent)
                
                # Disk I/O metrics
                disk_io = psutil.disk_io_counters()
                self.metrics['disk_io'].append({
                    'read_bytes': disk_io.read_bytes,
                    'write_bytes': disk_io.write_bytes
                })
                
                # Network I/O metrics
                net_io = psutil.net_io_counters()
                self.metrics['network_io'].append({
                    'bytes_sent': net_io.bytes_sent,
                    'bytes_recv': net_io.bytes_recv
                })
                
                time.sleep(1)  # Collect metrics every second
                
            except Exception as e:
                self.logger.error(f"Error collecting metrics: {str(e)}")

    def add_response_time(self, response_time: float):
        """Add response time measurement."""
        self.metrics['response_times'].append(response_time)

    def add_error(self, error: str):
        """Add error occurrence."""
        self.metrics['errors'].append({
            'timestamp': time.time(),
            'error': error
        })

    def update_active_users(self, count: int):
        """Update active user count."""
        self.metrics['active_users'].append({
            'timestamp': time.time(),
            'count': count
        })

    def _save_metrics(self):
        """Save collected metrics to file."""
        metrics_file = self.output_dir / 'metrics.json'
        with open(metrics_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)

    def _generate_report(self):
        """Generate performance report."""
        report = self._analyze_metrics()
        self._create_visualizations()
        self._save_report(report)

    def _analyze_metrics(self) -> Dict[str, Any]:
        """Analyze collected metrics."""
        response_times = np.array(self.metrics['response_times'])
        cpu_usage = np.array(self.metrics['cpu_percent'])
        memory_usage = np.array(self.metrics['memory_percent'])

        return {
            'test_id': self.test_id,
            'duration': time.time() - self.start_time,
            'response_time': {
                'avg': np.mean(response_times),
                'p50': np.percentile(response_times, 50),
                'p90': np.percentile(response_times, 90),
                'p95': np.percentile(response_times, 95),
                'p99': np.percentile(response_times, 99)
            },
            'resource_usage': {
                'cpu': {
                    'avg': np.mean(cpu_usage),
                    'max': np.max(cpu_usage)
                },
                'memory': {
                    'avg': np.mean(memory_usage),
                    'max': np.max(memory_usage)
                }
            },
            'errors': {
                'count': len(self.metrics['errors']),
                'rate': len(self.metrics['errors']) / len(response_times) if response_times.size > 0 else 0
            }
        }

    def _create_visualizations(self):
        """Create performance visualizations."""
        # Response Time Distribution
        plt.figure(figsize=(10, 6))
        plt.hist(self.metrics['response_times'], bins=50)
        plt.title('Response Time Distribution')
        plt.xlabel('Response Time (ms)')
        plt.ylabel('Count')
        plt.savefig(self.output_dir / 'response_times.png')
        plt.close()

        # Resource Usage Over Time
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        # CPU Usage
        ax1.plot(self.metrics['timestamp'], self.metrics['cpu_percent'])
        ax1.set_title('CPU Usage Over Time')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('CPU %')
        
        # Memory Usage
        ax2.plot(self.metrics['timestamp'], self.metrics['memory_percent'])
        ax2.set_title('Memory Usage Over Time')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Memory %')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'resource_usage.png')
        plt.close()

        # Active Users Over Time
        if self.metrics['active_users']:
            df = pd.DataFrame(self.metrics['active_users'])
            plt.figure(figsize=(10, 6))
            plt.plot(df['timestamp'], df['count'])
            plt.title('Active Users Over Time')
            plt.xlabel('Time')
            plt.ylabel('Users')
            plt.savefig(self.output_dir / 'active_users.png')
            plt.close()

    def _save_report(self, report: Dict[str, Any]):
        """Save performance report."""
        report_file = self.output_dir / 'report.json'
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        # Generate HTML report
        html_report = self._generate_html_report(report)
        with open(self.output_dir / 'report.html', 'w') as f:
            f.write(html_report)

    def _generate_html_report(self, report: Dict[str, Any]) -> str:
        """Generate HTML report from metrics."""
        template = """
        <html>
        <head>
            <title>Load Test Report - {test_id}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .metric {{ margin: 20px 0; padding: 10px; border: 1px solid #ddd; }}
                .chart {{ margin: 20px 0; }}
                .error {{ color: red; }}
            </style>
        </head>
        <body>
            <h1>Load Test Report - {test_id}</h1>
            <div class="metric">
                <h2>Test Summary</h2>
                <p>Duration: {duration:.2f} seconds</p>
                <p>Total Requests: {total_requests}</p>
                <p>Error Rate: {error_rate:.2%}</p>
            </div>
            <div class="metric">
                <h2>Response Times</h2>
                <p>Average: {avg_rt:.2f} ms</p>
                <p>P50: {p50_rt:.2f} ms</p>
                <p>P90: {p90_rt:.2f} ms</p>
                <p>P95: {p95_rt:.2f} ms</p>
                <p>P99: {p99_rt:.2f} ms</p>
            </div>
            <div class="metric">
                <h2>Resource Usage</h2>
                <p>Average CPU: {avg_cpu:.2f}%</p>
                <p>Max CPU: {max_cpu:.2f}%</p>
                <p>Average Memory: {avg_mem:.2f}%</p>
                <p>Max Memory: {max_mem:.2f}%</p>
            </div>
            <div class="chart">
                <h2>Charts</h2>
                <img src="response_times.png" alt="Response Time Distribution">
                <img src="resource_usage.png" alt="Resource Usage">
                <img src="active_users.png" alt="Active Users">
            </div>
        </body>
        </html>
        """
        
        return template.format(
            test_id=report['test_id'],
            duration=report['duration'],
            total_requests=len(self.metrics['response_times']),
            error_rate=report['errors']['rate'],
            avg_rt=report['response_time']['avg'],
            p50_rt=report['response_time']['p50'],
            p90_rt=report['response_time']['p90'],
            p95_rt=report['response_time']['p95'],
            p99_rt=report['response_time']['p99'],
            avg_cpu=report['resource_usage']['cpu']['avg'],
            max_cpu=report['resource_usage']['cpu']['max'],
            avg_mem=report['resource_usage']['memory']['avg'],
            max_mem=report['resource_usage']['memory']['max']
        )

def main():
    """Example usage of MetricsCollector."""
    collector = MetricsCollector('example_test')
    collector.start()
    
    # Simulate some metrics
    for _ in range(100):
        collector.add_response_time(random.random() * 1000)
        collector.update_active_users(random.randint(1, 100))
        time.sleep(0.1)
    
    collector.stop()

if __name__ == '__main__':
    import random
    main()
