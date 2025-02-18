"""Example script for extracting database schema."""
import logging
from pathlib import Path
from adpa.training.text2sql.schema_extractor import SchemaExtractor

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Example database connection strings
    databases = {
        "sqlite": "sqlite:///example.db",
        "postgres": "postgresql://user:pass@localhost:5432/dbname",
        "mysql": "mysql://user:pass@localhost:3306/dbname"
    }

    # Extract schema from SQLite database
    extractor = SchemaExtractor(databases["sqlite"])
    
    # Save in different formats
    output_dir = Path("extracted_schemas")
    output_dir.mkdir(exist_ok=True)
    
    # JSON format
    extractor.save_schema(
        output_dir / "schema.json",
        format_type="json"
    )
    
    # SQL format
    extractor.save_schema(
        output_dir / "schema.sql",
        format_type="sql"
    )
    
    # Natural language format
    extractor.save_schema(
        output_dir / "schema.txt",
        format_type="natural"
    )
    
    # Print schema context
    logger.info("\nNatural Language Schema Description:")
    print(extractor.generate_schema_context("natural"))
    
    logger.info("\nSQL Schema:")
    print(extractor.generate_schema_context("sql"))

if __name__ == "__main__":
    main()
