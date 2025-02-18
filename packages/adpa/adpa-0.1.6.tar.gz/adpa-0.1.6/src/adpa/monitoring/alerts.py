"""Alert handling for monitoring system."""
from typing import Dict, Any, Optional, Protocol
import logging
from datetime import datetime
import json

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import smtplib
from email.mime.text import MIMEText
import mlflow

from adpa.monitoring.types import Alert, AlertConfig

logger = logging.getLogger(__name__)


class AlertHandler(Protocol):
    """Alert handler protocol."""
    
    def send_alert(self, alert: Alert) -> None:
        """Send alert."""
        ...


class SlackAlertHandler:
    """Slack alert handler."""
    
    def __init__(self, token: str, channel: str = "#monitoring-alerts"):
        """Initialize handler.
        
        Args:
            token: Slack API token
            channel: Target channel
        """
        self.client = WebClient(token=token)
        self.channel = channel

    def send_alert(self, alert: Alert) -> None:
        """Send alert to Slack.
        
        Args:
            alert: Alert to send
        """
        message = self._format_message(alert)
        
        try:
            self.client.chat_postMessage(
                channel=self.channel,
                text=message
            )
        except SlackApiError as e:
            logger.error(f"Slack alert error: {e}")

    def _format_message(self, alert: Alert) -> str:
        """Format alert message."""
        return (
            f"⚠️ Alert: {alert.name}\n"
            f"Value: {alert.value:.2f} (threshold: {alert.threshold:.2f})\n"
            f"Category: {alert.category}\n"
            f"Time: {alert.timestamp}\n"
            f"Metadata: {json.dumps(alert.metadata, indent=2)}"
        )


class EmailAlertHandler:
    """Email alert handler."""
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        username: str,
        password: str,
        from_addr: str,
        to_addr: str
    ):
        """Initialize handler.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            username: SMTP username
            password: SMTP password
            from_addr: Sender address
            to_addr: Recipient address
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.from_addr = from_addr
        self.to_addr = to_addr

    def send_alert(self, alert: Alert) -> None:
        """Send alert via email.
        
        Args:
            alert: Alert to send
        """
        message = self._format_message(alert)
        msg = MIMEText(message)
        msg["Subject"] = f"ADPA Alert: {alert.name}"
        msg["From"] = self.from_addr
        msg["To"] = self.to_addr
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
        except Exception as e:
            logger.error(f"Email alert error: {e}")

    def _format_message(self, alert: Alert) -> str:
        """Format alert message."""
        return (
            f"Alert: {alert.name}\n\n"
            f"Value: {alert.value:.2f}\n"
            f"Threshold: {alert.threshold:.2f}\n"
            f"Category: {alert.category}\n"
            f"Time: {alert.timestamp}\n\n"
            f"Metadata:\n{json.dumps(alert.metadata, indent=2)}"
        )


class MLflowAlertHandler:
    """MLflow alert handler."""
    
    def __init__(self, tracking_uri: Optional[str] = None):
        """Initialize handler.
        
        Args:
            tracking_uri: Optional MLflow tracking URI
        """
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)

    def send_alert(self, alert: Alert) -> None:
        """Log alert to MLflow.
        
        Args:
            alert: Alert to log
        """
        try:
            # Log alert value
            mlflow.log_metric(
                f"alert_{alert.name}",
                alert.value
            )
            
            # Log alert details
            mlflow.log_dict(
                alert.dict(),
                f"alerts/{alert.timestamp.strftime('%Y%m%d_%H%M%S')}.json"
            )
        except Exception as e:
            logger.error(f"MLflow alert error: {e}")


class AlertManager:
    """Alert manager."""
    
    def __init__(self, config: AlertConfig):
        """Initialize manager.
        
        Args:
            config: Alert configuration
        """
        self.config = config
        self.handlers: Dict[str, AlertHandler] = {}

    def add_handler(self, name: str, handler: AlertHandler) -> None:
        """Add alert handler.
        
        Args:
            name: Handler name
            handler: Alert handler
        """
        self.handlers[name] = handler

    def remove_handler(self, name: str) -> None:
        """Remove alert handler.
        
        Args:
            name: Handler name
        """
        self.handlers.pop(name, None)

    def check_alert(
        self,
        name: str,
        value: float,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """Check if value should trigger alert.
        
        Args:
            name: Metric name
            value: Metric value
            metadata: Optional metadata
        """
        if name in self.config.thresholds:
            threshold = self.config.thresholds[name]
            if value > threshold:
                alert = Alert(
                    name=name,
                    value=value,
                    threshold=threshold,
                    category="metric",
                    metadata=metadata or {}
                )
                self.send_alert(alert)

    def send_alert(self, alert: Alert) -> None:
        """Send alert to all handlers.
        
        Args:
            alert: Alert to send
        """
        for name, handler in self.handlers.items():
            if name in self.config.channels:
                try:
                    handler.send_alert(alert)
                except Exception as e:
                    logger.error(f"Alert handler error ({name}): {e}")
