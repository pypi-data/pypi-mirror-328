"""Database utilities for the Text-to-SQL Streamlit app."""
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
import logging

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from models import DatabaseConfig, QueryMetadata

# Configure logging
logger = logging.getLogger(__name__)


class DatabaseManager:
    """Manages database connections and query execution."""
    
    def __init__(self, config: DatabaseConfig) -> None:
        """Initialize database manager.
        
        Args:
            config: Database configuration
        """
        self._config = config
        self._engine = create_engine(config.uri)
        logger.info("Database manager initialized with URI: %s", config.uri)
    
    def execute_query(self, query: str) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
        """Execute SQL query and return results as DataFrame.
        
        Args:
            query: SQL query to execute
            
        Returns:
            Tuple of (DataFrame with results, error message if any)
        """
        try:
            with self._engine.connect() as conn:
                df = pd.read_sql_query(text(query), conn)
                logger.debug("Query executed successfully: %s", query)
                return df, None
        except SQLAlchemyError as e:
            error_msg = f"Database error: {str(e)}"
            logger.error(error_msg)
            return None, error_msg
    
    def get_schema_info(self) -> Dict[str, List[Dict[str, str]]]:
        """Get database schema information.
        
        Returns:
            Dictionary with table names as keys and column information as values
        """
        schema_info = {}
        try:
            with self._engine.connect() as conn:
                # Get all tables
                tables_query = """
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """
                tables = pd.read_sql_query(text(tables_query), conn)
                
                # Get column information for each table
                for table in tables["table_name"]:
                    columns_query = f"""
                        SELECT 
                            column_name,
                            data_type,
                            is_nullable,
                            column_default
                        FROM information_schema.columns
                        WHERE table_name = '{table}'
                    """
                    columns = pd.read_sql_query(text(columns_query), conn)
                    schema_info[table] = columns.to_dict("records")
                
                logger.debug("Schema info retrieved successfully")
                return schema_info
        except SQLAlchemyError as e:
            logger.error("Error getting schema info: %s", e)
            return {}
    
    def get_sample_data(
        self, table_name: str, limit: int = 5
    ) -> Optional[pd.DataFrame]:
        """Get sample data from a table.
        
        Args:
            table_name: Name of the table
            limit: Maximum number of rows to return
            
        Returns:
            DataFrame with sample data or None if error
        """
        try:
            with self._engine.connect() as conn:
                query = f"SELECT * FROM {table_name} LIMIT {limit}"
                df = pd.read_sql_query(text(query), conn)
                logger.debug("Sample data retrieved for table: %s", table_name)
                return df
        except SQLAlchemyError as e:
            logger.error("Error getting sample data: %s", e)
            return None
    
    def validate_query(self, query: str) -> Tuple[bool, Optional[str]]:
        """Validate SQL query without executing it.
        
        Args:
            query: SQL query to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            with self._engine.connect() as conn:
                # Try to compile the query without executing
                compiled_query = text(query).compile(
                    dialect=self._engine.dialect,
                    compile_kwargs={"literal_binds": True}
                )
                logger.debug("Query validated successfully: %s", query)
                return True, None
        except SQLAlchemyError as e:
            error_msg = f"Query validation error: {str(e)}"
            logger.error(error_msg)
            return False, error_msg
    
    def get_query_metadata(self, query: str) -> QueryMetadata:
        """Get metadata about the query.
        
        Args:
            query: SQL query to analyze
            
        Returns:
            QueryMetadata object with query information
        """
        try:
            # Basic query type detection
            query_lower = query.lower()
            query_type = self._detect_query_type(query_lower)
            
            # Extract table names
            tables_referenced = self._extract_table_names(query_lower)
            
            # Create metadata object
            metadata = QueryMetadata(
                tables_referenced=tables_referenced,
                query_type=query_type,
                estimated_rows=None,  # Could be implemented with EXPLAIN
                execution_plan=None  # Could be implemented with EXPLAIN
            )
            
            logger.debug("Query metadata generated: %s", metadata)
            return metadata
        except Exception as e:
            logger.error("Error getting query metadata: %s", e)
            return QueryMetadata(
                tables_referenced=[],
                query_type="unknown"
            )
    
    def _detect_query_type(self, query: str) -> str:
        """Detect the type of SQL query.
        
        Args:
            query: SQL query in lowercase
            
        Returns:
            Query type as string
        """
        if query.startswith("select"):
            return "select"
        elif query.startswith("insert"):
            return "insert"
        elif query.startswith("update"):
            return "update"
        elif query.startswith("delete"):
            return "delete"
        return "unknown"
    
    def _extract_table_names(self, query: str) -> List[str]:
        """Extract table names from SQL query.
        
        Args:
            query: SQL query in lowercase
            
        Returns:
            List of table names
        """
        tables = []
        from_idx = query.find("from")
        if from_idx != -1:
            tables_part = query[from_idx:].split("where")[0]
            tables = tables_part.replace("from", "").strip().split(",")
            tables = [t.strip() for t in tables]
        return tables
