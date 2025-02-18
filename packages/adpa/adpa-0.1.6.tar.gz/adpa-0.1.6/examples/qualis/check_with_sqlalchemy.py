"""Check database using SQLAlchemy."""
from sqlalchemy import create_engine, text
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('db_check.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Database URL
DB_URL = "postgresql://uem4h7dfn2ghbi:p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d9ia9eei6rkq90"

try:
    logger.info("Creating database engine...")
    engine = create_engine(DB_URL, echo=True)
    
    logger.info("Testing connection...")
    with engine.connect() as conn:
        # Check database connection
        result = conn.execute(text("SELECT version();"))
        version = result.scalar()
        logger.info(f"Connected to PostgreSQL version: {version}")
        
        # Check schema
        logger.info("Checking schema 'ttt'...")
        result = conn.execute(text(
            "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ttt';"
        ))
        schema = result.scalar()
        if schema:
            logger.info(f"Schema 'ttt' exists")
            
            # List tables
            logger.info("Getting tables...")
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'ttt'
                ORDER BY table_name;
            """))
            tables = result.fetchall()
            
            if tables:
                logger.info(f"Found {len(tables)} tables:")
                for table in tables:
                    table_name = table[0]
                    logger.info(f"\nChecking table: {table_name}")
                    
                    # Get column info
                    result = conn.execute(text(f"""
                        SELECT column_name, data_type, character_maximum_length
                        FROM information_schema.columns
                        WHERE table_schema = 'ttt'
                        AND table_name = :table_name
                        ORDER BY ordinal_position;
                    """), {"table_name": table_name})
                    columns = result.fetchall()
                    logger.info(f"Columns: {columns}")
                    
                    # Get row count
                    result = conn.execute(text(f"SELECT COUNT(*) FROM ttt.{table_name};"))
                    count = result.scalar()
                    logger.info(f"Row count: {count}")
                    
                    # Get sample data
                    if count > 0:
                        result = conn.execute(text(f"SELECT * FROM ttt.{table_name} LIMIT 1;"))
                        sample = result.fetchone()
                        logger.info(f"Sample row: {sample}")
            else:
                logger.info("No tables found in schema 'ttt'")
        else:
            logger.info("Schema 'ttt' does not exist")
            
except Exception as e:
    logger.error(f"An error occurred: {str(e)}", exc_info=True)
    
logger.info("Database check complete. Check db_check.log for details.")
