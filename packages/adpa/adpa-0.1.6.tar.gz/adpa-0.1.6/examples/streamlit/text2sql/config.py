"""Configuration for the Text-to-SQL Streamlit app."""
import os
from pathlib import Path
import logging

from dotenv import load_dotenv

from models import DatabaseConfig, AppConfig

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
env_path = Path(__file__).parents[3] / ".env"
logger.debug(f"Looking for .env file at: {env_path}")
if env_path.exists():
    logger.info(f"Loading environment variables from {env_path}")
    load_dotenv(env_path)
else:
    logger.warning(f".env file not found at {env_path}")

# Create database configuration
DB_CONFIG = DatabaseConfig(
    host=os.getenv("POSTGRES_HOST", "c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com"),
    port=int(os.getenv("POSTGRES_PORT", "5432")),
    user=os.getenv("POSTGRES_USER", "uem4h7dfn2ghbi"),
    password=os.getenv("POSTGRES_PASSWORD", "p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb"),
    database=os.getenv("POSTGRES_DATABASE", "d9ia9eei6rkq90"),
    uri=os.getenv(
        "POSTGRES_URI",
        "postgresql://uem4h7dfn2ghbi:p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb@"
        "c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d9ia9eei6rkq90"
    )
)

# Create app configuration
APP_CONFIG = AppConfig(
    title="ADPA Text-to-SQL Explorer",
    icon="🔍",
    theme_color="#1E88E5",
    max_history_size=100,
    example_queries=[
        "Show all users who joined last month",
        "Find the total number of orders per customer",
        "List products with price greater than $100",
        "Show active users with their latest order date",
        "Calculate average order value by month"
    ],
    schema_info={
        "users": [
            "id (integer, primary key)",
            "username (varchar)",
            "email (varchar)",
            "created_at (timestamp)",
            "status (varchar)",
            "last_login (timestamp)"
        ],
        "orders": [
            "id (integer, primary key)",
            "user_id (integer, foreign key)",
            "total_amount (decimal)",
            "status (varchar)",
            "created_at (timestamp)"
        ],
        "products": [
            "id (integer, primary key)",
            "name (varchar)",
            "description (text)",
            "price (decimal)",
            "category (varchar)",
            "stock_level (integer)"
        ]
    }
)
