"""Enhanced monitoring system for ADPA framework."""
from typing import Dict, List, Any, Optional, Callable
import psutil
import numpy as np
from datetime import datetime, timedelta
import logging
import json
from pathlib import Path
import requests
from dataclasses import dataclass
import torch
from prometheus_client import start_http_server, Gauge, Counter, Histogram
import mlflow
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import smtplib
from email.mime.text import MIMEText
import threading
import queue
import time

from pydantic import BaseModel, Field, validator

logger = logging.getLogger(__name__)


class MonitoringConfig(BaseModel):
    """Configuration for monitoring system."""
    
    prometheus_port: int = Field(
        default=8000,
        description="Port for Prometheus metrics server"
    )
    alert_threshold: float = Field(
        default=0.95,
        ge=0.0,
        le=1.0,
        description="Default threshold for alerts"
    )
    check_interval: int = Field(
        default=60,
        ge=1,
        description="Interval in seconds between metric checks"
    )
    retention_days: int = Field(
        default=30,
        ge=1,
        description="Number of days to retain metrics"
    )
    slack_token: Optional[str] = Field(
        default=None,
        description="Slack API token for alerts"
    )
    email_config: Optional[Dict[str, str]] = Field(
        default=None,
        description="Email configuration for alerts"
    )
    mlflow_tracking_uri: Optional[str] = Field(
        default=None,
        description="MLflow tracking URI"
    )

    class Config:
        """Pydantic model configuration."""
        validate_assignment = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class MonitoringSystem:
    """Comprehensive monitoring system."""

    def __init__(self, config: MonitoringConfig):
        """Initialize monitoring system.
        
        Args:
            config: Monitoring configuration
        """
        self.config = config
        self._setup_metrics()
        self._setup_alerting()
        self._setup_storage()
        
        # Start Prometheus server
        start_http_server(config.prometheus_port)
        
        # Initialize monitoring thread
        self._stop_event = threading.Event()
        self._metrics_queue = queue.Queue()
        self._start_monitoring_thread()

    def _setup_metrics(self):
        """Setup monitoring metrics."""
        # System metrics
        self.cpu_usage = Gauge("cpu_usage", "CPU usage percentage")
        self.memory_usage = Gauge("memory_usage", "Memory usage percentage")
        self.gpu_usage = Gauge("gpu_usage", "GPU usage percentage")
        self.disk_usage = Gauge("disk_usage", "Disk usage percentage")
        
        # Training metrics
        self.training_loss = Histogram(
            "training_loss",
            "Training loss values",
            buckets=np.logspace(-3, 2, 50)
        )
        self.validation_metrics = Gauge(
            "validation_metrics",
            "Validation metrics",
            ["metric_name"]
        )
        self.batch_processing_time = Histogram(
            "batch_processing_time",
            "Time to process a batch",
            buckets=np.logspace(-3, 2, 50)
        )
        
        # Model metrics
        self.prediction_latency = Histogram(
            "prediction_latency",
            "Model prediction latency",
            buckets=np.logspace(-3, 2, 50)
        )
        self.model_accuracy = Gauge("model_accuracy", "Model accuracy")
        self.model_drift = Gauge("model_drift", "Model drift score")
        
        # Error metrics
        self.error_count = Counter(
            "error_count",
            "Number of errors",
            ["error_type"]
        )
        self.error_rate = Gauge("error_rate", "Error rate")

    def _setup_alerting(self):
        """Setup alerting system."""
        self.alert_handlers = {
            "slack": self._send_slack_alert,
            "email": self._send_email_alert,
            "mlflow": self._log_mlflow_alert
        }
        
        # Alert thresholds
        self.thresholds = {
            "cpu_usage": 90.0,
            "memory_usage": 90.0,
            "gpu_usage": 90.0,
            "disk_usage": 90.0,
            "error_rate": 0.05,
            "model_drift": 0.1
        }

    def _setup_storage(self):
        """Setup metric storage."""
        self.metrics_history = {
            "system": [],
            "training": [],
            "model": [],
            "errors": []
        }
        
        # Cleanup old metrics periodically
        self._start_cleanup_thread()

    def record_metric(
        self,
        category: str,
        name: str,
        value: float,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Record a metric value.
        
        Args:
            category: Metric category
            name: Metric name
            value: Metric value
            metadata: Optional metadata
        """
        timestamp = datetime.now()
        metric = {
            "timestamp": timestamp,
            "name": name,
            "value": value,
            "metadata": metadata or {}
        }
        
        # Store metric
        self.metrics_history[category].append(metric)
        
        # Update Prometheus metric
        if hasattr(self, name):
            getattr(self, name).set(value)
        
        # Check for alerts
        self._check_alerts(category, name, value, metadata)
        
        # Queue for async processing
        self._metrics_queue.put(metric)

    def record_training_metrics(
        self,
        metrics: Dict[str, float],
        step: int
    ):
        """Record training metrics.
        
        Args:
            metrics: Dictionary of metrics
            step: Training step
        """
        for name, value in metrics.items():
            self.record_metric(
                "training",
                name,
                value,
                {"step": step}
            )
            
            # Update MLflow if configured
            if self.config.mlflow_tracking_uri:
                mlflow.log_metric(name, value, step=step)

    def record_prediction_metrics(
        self,
        latency: float,
        accuracy: float,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Record prediction metrics.
        
        Args:
            latency: Prediction latency
            accuracy: Prediction accuracy
            metadata: Optional metadata
        """
        self.prediction_latency.observe(latency)
        self.model_accuracy.set(accuracy)
        
        self.record_metric(
            "model",
            "prediction_metrics",
            accuracy,
            {
                "latency": latency,
                **(metadata or {})
            }
        )

    def record_error(
        self,
        error_type: str,
        error_msg: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Record an error.
        
        Args:
            error_type: Type of error
            error_msg: Error message
            metadata: Optional metadata
        """
        self.error_count.labels(error_type).inc()
        
        self.record_metric(
            "errors",
            "error",
            1.0,
            {
                "type": error_type,
                "message": error_msg,
                **(metadata or {})
            }
        )

    def get_metrics_summary(
        self,
        category: str,
        time_range: timedelta
    ) -> Dict[str, Any]:
        """Get summary of metrics.
        
        Args:
            category: Metric category
            time_range: Time range to summarize
            
        Returns:
            Metrics summary
        """
        start_time = datetime.now() - time_range
        metrics = [
            m for m in self.metrics_history[category]
            if m["timestamp"] >= start_time
        ]
        
        summary = {
            "count": len(metrics),
            "metrics": {}
        }
        
        # Group by metric name
        for metric in metrics:
            name = metric["name"]
            if name not in summary["metrics"]:
                summary["metrics"][name] = []
            summary["metrics"][name].append(metric["value"])
        
        # Calculate statistics
        for name, values in summary["metrics"].items():
            summary["metrics"][name] = {
                "mean": np.mean(values),
                "std": np.std(values),
                "min": np.min(values),
                "max": np.max(values),
                "last": values[-1]
            }
        
        return summary

    def _start_monitoring_thread(self):
        """Start background monitoring thread."""
        def monitor_loop():
            while not self._stop_event.is_set():
                try:
                    # System metrics
                    self.cpu_usage.set(psutil.cpu_percent())
                    self.memory_usage.set(psutil.virtual_memory().percent)
                    self.disk_usage.set(psutil.disk_usage("/").percent)
                    
                    # GPU metrics if available
                    if torch.cuda.is_available():
                        gpu_usage = torch.cuda.memory_allocated() / torch.cuda.max_memory_allocated()
                        self.gpu_usage.set(gpu_usage * 100)
                    
                    time.sleep(self.config.check_interval)
                except Exception as e:
                    logger.error(f"Monitoring error: {e}")

        threading.Thread(target=monitor_loop, daemon=True).start()

    def _start_cleanup_thread(self):
        """Start metrics cleanup thread."""
        def cleanup_loop():
            while not self._stop_event.is_set():
                try:
                    cutoff = datetime.now() - timedelta(days=self.config.retention_days)
                    
                    # Clean up old metrics
                    for category in self.metrics_history:
                        self.metrics_history[category] = [
                            m for m in self.metrics_history[category]
                            if m["timestamp"] >= cutoff
                        ]
                    
                    time.sleep(86400)  # Daily cleanup
                except Exception as e:
                    logger.error(f"Cleanup error: {e}")

        threading.Thread(target=cleanup_loop, daemon=True).start()

    def _check_alerts(
        self,
        category: str,
        name: str,
        value: float,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Check if metric should trigger alert."""
        if name in self.thresholds:
            threshold = self.thresholds[name]
            if value > threshold:
                alert = {
                    "timestamp": datetime.now(),
                    "category": category,
                    "name": name,
                    "value": value,
                    "threshold": threshold,
                    "metadata": metadata
                }
                
                # Send alerts
                for handler in self.alert_handlers.values():
                    try:
                        handler(alert)
                    except Exception as e:
                        logger.error(f"Alert handler error: {e}")

    def _send_slack_alert(self, alert: Dict[str, Any]):
        """Send alert to Slack."""
        if not self.config.slack_token:
            return
        
        client = WebClient(token=self.config.slack_token)
        message = self._format_alert_message(alert)
        
        try:
            client.chat_postMessage(
                channel="#monitoring-alerts",
                text=message
            )
        except SlackApiError as e:
            logger.error(f"Slack alert error: {e}")

    def _send_email_alert(self, alert: Dict[str, Any]):
        """Send alert via email."""
        if not self.config.email_config:
            return
        
        message = self._format_alert_message(alert)
        msg = MIMEText(message)
        msg["Subject"] = f"ADPA Alert: {alert['name']}"
        msg["From"] = self.config.email_config["from"]
        msg["To"] = self.config.email_config["to"]
        
        try:
            with smtplib.SMTP(
                self.config.email_config["smtp_server"],
                self.config.email_config["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    self.config.email_config["username"],
                    self.config.email_config["password"]
                )
                server.send_message(msg)
        except Exception as e:
            logger.error(f"Email alert error: {e}")

    def _log_mlflow_alert(self, alert: Dict[str, Any]):
        """Log alert to MLflow."""
        if not self.config.mlflow_tracking_uri:
            return
        
        mlflow.log_metric(
            f"alert_{alert['name']}",
            alert['value']
        )
        mlflow.log_dict(
            alert,
            f"alerts/{alert['timestamp'].strftime('%Y%m%d_%H%M%S')}.json"
        )

    def _format_alert_message(self, alert: Dict[str, Any]) -> str:
        """Format alert message."""
        return (
            f"⚠️ Alert: {alert['name']}\n"
            f"Value: {alert['value']:.2f} (threshold: {alert['threshold']:.2f})\n"
            f"Category: {alert['category']}\n"
            f"Time: {alert['timestamp']}\n"
            f"Metadata: {json.dumps(alert['metadata'], indent=2)}"
        )

    def close(self):
        """Clean up monitoring resources."""
        self._stop_event.set()
        # Wait for threads to finish
        time.sleep(1)
