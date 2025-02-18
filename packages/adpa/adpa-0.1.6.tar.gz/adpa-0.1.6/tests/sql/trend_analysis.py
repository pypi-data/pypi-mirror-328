"""Trend analysis for SQL functionality tests."""
import json
import datetime
from typing import Dict, List, Any, Optional, Tuple
import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import seaborn as sns


class TrendAnalyzer:
    """Analyze trends in test results."""

    def __init__(self, data_dir: str = "test_reports"):
        """Initialize trend analyzer.
        
        Args:
            data_dir: Directory containing test data
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # Initialize data storage
        self.performance_data: Dict[str, List[float]] = {}
        self.error_data: Dict[str, List[int]] = {}
        self.load_data: Dict[str, List[Dict[str, float]]] = {}
        self.test_runs: List[Dict[str, Any]] = []

    def load_historical_data(self) -> None:
        """Load historical test data."""
        for data_file in sorted(self.data_dir.glob("test_data_*.json")):
            with open(data_file) as f:
                data = json.load(f)
                self._process_data(data)

    def _process_data(self, data: Dict[str, Any]) -> None:
        """Process and store test data.
        
        Args:
            data: Test data to process
        """
        # Store performance data
        for test_name, duration in data.get("performance", {}).items():
            if test_name not in self.performance_data:
                self.performance_data[test_name] = []
            self.performance_data[test_name].append(duration)
        
        # Store error data
        for error_type, count in data.get("errors", {}).items():
            if error_type not in self.error_data:
                self.error_data[error_type] = []
            self.error_data[error_type].append(count)
        
        # Store load test data
        for test_name, metrics in data.get("load", {}).items():
            if test_name not in self.load_data:
                self.load_data[test_name] = []
            self.load_data[test_name].append(metrics)
        
        # Store test run
        self.test_runs.append({
            "timestamp": datetime.datetime.fromisoformat(data["timestamp"]),
            "data": data
        })

    def analyze_performance_trends(self) -> Dict[str, Any]:
        """Analyze performance trends.
        
        Returns:
            Dictionary containing trend analysis results
        """
        results = {}
        
        for test_name, durations in self.performance_data.items():
            if len(durations) < 2:
                continue
            
            # Convert to pandas Series
            series = pd.Series(durations)
            
            # Calculate basic statistics
            stats_data = {
                "mean": series.mean(),
                "std": series.std(),
                "min": series.min(),
                "max": series.max(),
                "p95": series.quantile(0.95)
            }
            
            # Perform trend analysis
            x = np.arange(len(series)).reshape(-1, 1)
            y = series.values
            
            # Linear regression
            model = LinearRegression()
            model.fit(x, y)
            trend = {
                "slope": model.coef_[0],
                "intercept": model.intercept_,
                "r2_score": model.score(x, y)
            }
            
            # Detect anomalies (points > 2 std from mean)
            mean = series.mean()
            std = series.std()
            anomalies = series[abs(series - mean) > 2 * std]
            
            results[test_name] = {
                "statistics": stats_data,
                "trend": trend,
                "anomalies": {
                    "count": len(anomalies),
                    "indices": anomalies.index.tolist(),
                    "values": anomalies.values.tolist()
                }
            }
        
        return results

    def analyze_error_patterns(self) -> Dict[str, Any]:
        """Analyze error patterns.
        
        Returns:
            Dictionary containing error pattern analysis
        """
        results = {}
        
        for error_type, counts in self.error_data.items():
            if len(counts) < 2:
                continue
            
            series = pd.Series(counts)
            
            # Calculate error frequency
            frequency = {
                "total": series.sum(),
                "mean_per_run": series.mean(),
                "std_per_run": series.std()
            }
            
            # Analyze error patterns
            patterns = {
                "consecutive_errors": self._find_consecutive_errors(series),
                "error_clusters": self._find_error_clusters(series),
                "periodic_patterns": self._find_periodic_patterns(series)
            }
            
            results[error_type] = {
                "frequency": frequency,
                "patterns": patterns
            }
        
        return results

    def _find_consecutive_errors(self, series: pd.Series) -> List[Dict[str, Any]]:
        """Find consecutive error occurrences.
        
        Args:
            series: Error count series
            
        Returns:
            List of consecutive error patterns
        """
        consecutive = []
        current_streak = 0
        
        for i, value in enumerate(series):
            if value > 0:
                current_streak += 1
            else:
                if current_streak > 1:
                    consecutive.append({
                        "start": i - current_streak,
                        "length": current_streak
                    })
                current_streak = 0
        
        return consecutive

    def _find_error_clusters(self, series: pd.Series) -> List[Dict[str, Any]]:
        """Find clusters of errors.
        
        Args:
            series: Error count series
            
        Returns:
            List of error clusters
        """
        # Use rolling window to detect clusters
        window_size = 3
        rolling_sum = series.rolling(window=window_size).sum()
        
        clusters = []
        threshold = rolling_sum.mean() + rolling_sum.std()
        
        cluster_start = None
        for i, value in enumerate(rolling_sum):
            if value > threshold:
                if cluster_start is None:
                    cluster_start = i
            elif cluster_start is not None:
                clusters.append({
                    "start": cluster_start,
                    "end": i,
                    "sum": float(series[cluster_start:i].sum())
                })
                cluster_start = None
        
        return clusters

    def _find_periodic_patterns(self, series: pd.Series) -> Dict[str, Any]:
        """Find periodic patterns in errors.
        
        Args:
            series: Error count series
            
        Returns:
            Dictionary containing periodic pattern analysis
        """
        if len(series) < 4:
            return {}
        
        # Perform seasonal decomposition
        try:
            decomposition = seasonal_decompose(
                series,
                period=min(len(series) // 2, 7),
                model="additive"
            )
            
            return {
                "seasonal": decomposition.seasonal.tolist(),
                "trend": decomposition.trend.tolist(),
                "resid": decomposition.resid.tolist()
            }
        except:
            return {}

    def analyze_load_test_trends(self) -> Dict[str, Any]:
        """Analyze load test trends.
        
        Returns:
            Dictionary containing load test trend analysis
        """
        results = {}
        
        for test_name, metrics_list in self.load_data.items():
            if len(metrics_list) < 2:
                continue
            
            # Convert to DataFrame
            df = pd.DataFrame(metrics_list)
            
            # Analyze each metric
            metric_trends = {}
            for column in df.columns:
                series = df[column]
                
                # Calculate statistics
                stats_data = {
                    "mean": series.mean(),
                    "std": series.std(),
                    "min": series.min(),
                    "max": series.max(),
                    "p95": series.quantile(0.95)
                }
                
                # Calculate trend
                x = np.arange(len(series)).reshape(-1, 1)
                y = series.values
                
                model = LinearRegression()
                model.fit(x, y)
                
                trend = {
                    "slope": float(model.coef_[0]),
                    "intercept": float(model.intercept_),
                    "r2_score": float(model.score(x, y))
                }
                
                metric_trends[column] = {
                    "statistics": stats_data,
                    "trend": trend
                }
            
            results[test_name] = metric_trends
        
        return results

    def generate_trend_report(self, output_dir: Optional[str] = None) -> str:
        """Generate trend analysis report.
        
        Args:
            output_dir: Optional directory to save report
            
        Returns:
            Path to generated report
        """
        if output_dir is None:
            output_dir = self.data_dir
        else:
            output_dir = Path(output_dir)
            output_dir.mkdir(exist_ok=True)
        
        # Analyze trends
        performance_trends = self.analyze_performance_trends()
        error_patterns = self.analyze_error_patterns()
        load_trends = self.analyze_load_test_trends()
        
        # Create report
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "performance_trends": performance_trends,
            "error_patterns": error_patterns,
            "load_trends": load_trends
        }
        
        # Save report
        report_path = output_dir / f"trend_report_{int(datetime.datetime.now().timestamp())}.json"
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)
        
        return str(report_path)

    def plot_trends(self, output_dir: Optional[str] = None) -> List[str]:
        """Generate trend plots.
        
        Args:
            output_dir: Optional directory to save plots
            
        Returns:
            List of paths to generated plots
        """
        if output_dir is None:
            output_dir = self.data_dir
        else:
            output_dir = Path(output_dir)
            output_dir.mkdir(exist_ok=True)
        
        plot_paths = []
        
        # Performance trends
        plt.figure(figsize=(12, 6))
        for test_name, durations in self.performance_data.items():
            plt.plot(durations, label=test_name)
        plt.title("Performance Trends")
        plt.xlabel("Test Run")
        plt.ylabel("Duration (s)")
        plt.legend()
        
        path = output_dir / "performance_trends.png"
        plt.savefig(path)
        plt.close()
        plot_paths.append(str(path))
        
        # Error patterns
        plt.figure(figsize=(12, 6))
        for error_type, counts in self.error_data.items():
            plt.plot(counts, label=error_type)
        plt.title("Error Patterns")
        plt.xlabel("Test Run")
        plt.ylabel("Error Count")
        plt.legend()
        
        path = output_dir / "error_patterns.png"
        plt.savefig(path)
        plt.close()
        plot_paths.append(str(path))
        
        # Load test trends
        for test_name, metrics_list in self.load_data.items():
            plt.figure(figsize=(12, 6))
            df = pd.DataFrame(metrics_list)
            
            for column in df.columns:
                plt.plot(df[column], label=column)
            
            plt.title(f"Load Test Trends - {test_name}")
            plt.xlabel("Test Run")
            plt.ylabel("Value")
            plt.legend()
            
            path = output_dir / f"load_trends_{test_name}.png"
            plt.savefig(path)
            plt.close()
            plot_paths.append(str(path))
        
        return plot_paths


if __name__ == "__main__":
    # Create and run trend analyzer
    analyzer = TrendAnalyzer()
    analyzer.load_historical_data()
    
    # Generate report and plots
    report_path = analyzer.generate_trend_report()
    plot_paths = analyzer.plot_trends()
    
    print(f"Report generated: {report_path}")
    print("Plots generated:")
    for path in plot_paths:
        print(f"- {path}")
