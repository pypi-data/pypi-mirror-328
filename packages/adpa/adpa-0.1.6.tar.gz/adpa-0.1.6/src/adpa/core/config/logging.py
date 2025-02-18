"""Logging configuration for ADPA."""
from __future__ import annotations

import logging.config
import os
from pathlib import Path
from typing import Any, Dict

import yaml


def setup_logging(
    default_path: str = "logging.yaml",
    default_level: int = logging.INFO,
    env_key: str = "LOG_CFG",
) -> None:
    """Set up logging configuration.

    Args:
        default_path: Path to logging configuration file
        default_level: Default logging level
        env_key: Environment variable key for logging config
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value

    if os.path.exists(path):
        with open(path, "rt", encoding="utf-8") as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(f"Error in Logging Configuration: {e}")
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)


def get_default_config() -> Dict[str, Any]:
    """Get default logging configuration.

    Returns:
        Default logging configuration
    """
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            },
            "detailed": {
                "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "standard",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "detailed",
                "filename": "adpa.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf8",
            },
            "error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "detailed",
                "filename": "adpa_error.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf8",
            },
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console", "file", "error_file"],
                "level": "INFO",
                "propagate": True,
            },
            "adpa": {
                "handlers": ["console", "file", "error_file"],
                "level": "DEBUG",
                "propagate": False,
            },
            "adpa.text2sql": {
                "handlers": ["console", "file", "error_file"],
                "level": "DEBUG",
                "propagate": False,
            },
            "adpa.agents": {
                "handlers": ["console", "file", "error_file"],
                "level": "DEBUG",
                "propagate": False,
            },
            "adpa.database": {
                "handlers": ["console", "file", "error_file"],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }
