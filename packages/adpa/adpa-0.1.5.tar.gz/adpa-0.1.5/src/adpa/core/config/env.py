"""
Environment configuration utilities.
"""
from typing import Dict, Any, Optional
from pathlib import Path
import os
import json
from dotenv import load_dotenv, set_key, find_dotenv

def load_env_config(env_file: Optional[Path] = None) -> Dict[str, Any]:
    """Load environment configuration.
    
    Args:
        env_file: Optional path to .env file
        
    Returns:
        Dictionary of environment variables
        
    Raises:
        FileNotFoundError: If env_file not found
    """
    # Find .env file
    if env_file is None:
        env_file = find_dotenv(usecwd=True)
        if not env_file:
            env_file = Path(".env")
    
    # Load environment variables
    if env_file.exists():
        load_dotenv(env_file)
    
    # Get all ADPA_ prefixed variables
    config = {}
    for key, value in os.environ.items():
        if key.startswith("ADPA_"):
            # Convert value types
            if value.lower() in {"true", "false"}:
                value = value.lower() == "true"
            elif value.isdigit():
                value = int(value)
            elif value.replace(".", "", 1).isdigit():
                value = float(value)
            elif value.startswith("[") or value.startswith("{"):
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    pass
            config[key] = value
    
    return config

def save_env_config(
    config: Dict[str, Any],
    env_file: Optional[Path] = None,
    overwrite: bool = False
) -> None:
    """Save environment configuration.
    
    Args:
        config: Configuration dictionary
        env_file: Optional path to .env file
        overwrite: Whether to overwrite existing values
        
    Raises:
        ValueError: If config contains invalid values
    """
    # Find .env file
    if env_file is None:
        env_file = find_dotenv(usecwd=True)
        if not env_file:
            env_file = Path(".env")
    
    # Create .env file if it doesn't exist
    if not env_file.exists():
        env_file.touch()
    
    # Load existing config
    existing_config = load_env_config(env_file)
    
    # Update configuration
    for key, value in config.items():
        if not key.startswith("ADPA_"):
            key = f"ADPA_{key}"
        
        # Skip if value exists and not overwriting
        if key in existing_config and not overwrite:
            continue
        
        # Convert value to string
        if isinstance(value, (list, dict)):
            value = json.dumps(value)
        elif isinstance(value, bool):
            value = str(value).lower()
        else:
            value = str(value)
        
        # Save to .env file
        set_key(str(env_file), key, value)

def update_env_config(
    key: str,
    value: Any,
    env_file: Optional[Path] = None
) -> None:
    """Update single environment variable.
    
    Args:
        key: Variable name
        value: Variable value
        env_file: Optional path to .env file
        
    Raises:
        ValueError: If key or value is invalid
    """
    save_env_config({key: value}, env_file, overwrite=True)
