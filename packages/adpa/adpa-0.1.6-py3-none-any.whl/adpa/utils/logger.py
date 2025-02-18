"""Logging configuration for the ADPA Framework."""

import logging
import os
from pathlib import Path
from typing import Optional
from pythonjsonlogger import jsonlogger
from datetime import datetime

from .file_utils import ensure_dir

class ADPALogger(logging.Logger):
    """Custom logger class for ADPA Framework."""
    
    def __init__(self, name: str, level: int = logging.NOTSET):
        super().__init__(name, level)
        self.metrics = {}

    def log_metric(self, name: str, value: float, tags: Optional[dict] = None) -> None:
        """Log a metric value with optional tags.
        
        Args:
            name: Metric name
            value: Metric value
            tags: Optional tags to associate with the metric
        """
        metric = {
            'timestamp': datetime.utcnow().isoformat(),
            'value': value,
            'tags': tags or {}
        }
        self.metrics[name] = metric
        self.info(f"Metric: {name}={value}", extra={'metric': metric})

def get_logger(
    name: str,
    log_dir: Optional[str] = None,
    log_level: Optional[str] = None,
    json_format: bool = True
) -> ADPALogger:
    """Get a configured logger instance.
    
    Args:
        name: Name for the logger
        log_dir: Directory for log files (default: project_root/logs)
        log_level: Log level (default: from env or INFO)
        json_format: Whether to use JSON format for file logs (default: True)
        
    Returns:
        ADPALogger: Configured logger instance
    """
    # Register custom logger class
    logging.setLoggerClass(ADPALogger)
    logger = logging.getLogger(name)
    
    # Only configure if handlers haven't been set up
    if not logger.handlers:
        # Set log level from environment or parameter or default to INFO
        level = (log_level or os.getenv("LOG_LEVEL", "INFO")).upper()
        logger.setLevel(level)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        
        # Create file handler
        if log_dir is None:
            from .file_utils import get_project_root
            log_dir = str(get_project_root() / 'logs')
        
        log_path = Path(log_dir) / f"{name}.log"
        ensure_dir(log_path)
        file_handler = logging.FileHandler(str(log_path))
        file_handler.setLevel(level)
        
        # Create formatters
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        if json_format:
            file_formatter = jsonlogger.JsonFormatter(
                "%(asctime)s %(name)s %(levelname)s %(message)s %(metric)s"
            )
        else:
            file_formatter = console_formatter
        
        # Set formatters
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)
        
        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
        # Log initial configuration
        logger.debug(
            "Logger configured",
            extra={
                'config': {
                    'name': name,
                    'level': level,
                    'log_dir': log_dir,
                    'json_format': json_format
                }
            }
        )
    
    return logger
