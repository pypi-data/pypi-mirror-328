"""Streamlit app for Text-to-SQL exploration."""
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

import streamlit as st
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("text2sql_app.log")
    ]
)
logger = logging.getLogger(__name__)

# Add project root to Python path
project_root = Path(__file__).parents[3]
sys.path.insert(0, str(project_root))
logger.debug(f"Python path: {sys.path}")

try:
    from config import DB_CONFIG, APP_CONFIG
    from database import DatabaseManager
    from models import (
        QueryResult, QueryMetadata, Text2SQLConfig,
        TableSchema, TableColumn
    )
    from adpa.text2sql.hybrid.coordinator import Text2SQLCoordinator
except Exception as e:
    logger.error(f"Error importing modules: {e}")
    raise

# Initialize session state
if "query_history" not in st.session_state:
    st.session_state.query_history = []


def initialize_text2sql() -> Text2SQLCoordinator:
    """Initialize Text2SQL coordinator with configuration.
    
    Returns:
        Configured Text2SQL coordinator
    """
    config = Text2SQLConfig(
        connection_params={"url": DB_CONFIG.uri},
        enable_security=True,
        enable_monitoring=True,
        optimization_level=2,
        timeout_seconds=30
    )
    return Text2SQLCoordinator(config.dict())


def add_to_history(
    query: str,
    sql: str,
    success: bool,
    timestamp: datetime,
    metadata: Optional[QueryMetadata] = None,
    error_message: Optional[str] = None,
    confidence: float = 0.0,
    processing_time: float = 0.0
) -> None:
    """Add query to history with timestamp.
    
    Args:
        query: Natural language query
        sql: Generated SQL query
        success: Whether the query was successful
        timestamp: Query timestamp
        metadata: Query metadata
        error_message: Error message if query failed
        confidence: Query confidence score
        processing_time: Query processing time
    """
    st.session_state.query_history.append(
        QueryResult(
            natural_query=query,
            sql_query=sql,
            success=success,
            timestamp=timestamp,
            confidence=confidence,
            processing_time=processing_time,
            error_message=error_message,
            metadata=metadata
        )
    )
    if len(st.session_state.query_history) > APP_CONFIG.max_history_size:
        st.session_state.query_history.pop(0)


def display_schema_info() -> None:
    """Display database schema information."""
    st.sidebar.markdown("### Database Schema")
    for table, columns in APP_CONFIG.schema_info.items():
        with st.sidebar.expander(f"📋 {table}"):
            for column in columns:
                st.write(f"- {column}")


def display_query_history() -> None:
    """Display query history in sidebar."""
    st.sidebar.markdown("### Query History")
    for entry in reversed(st.session_state.query_history[-5:]):
        with st.sidebar.expander(
            f"🕒 {entry.timestamp.strftime('%H:%M:%S')} "
            f"({'✅' if entry.success else '❌'})"
        ):
            st.write("Natural Query:")
            st.write(f"_{entry.natural_query}_")
            st.write("SQL Query:")
            st.code(entry.sql_query, language="sql")
            if entry.metadata:
                st.write("Tables Referenced:")
                st.write(", ".join(entry.metadata.tables_referenced))


def display_example_queries() -> None:
    """Display example queries that users can try."""
    st.sidebar.markdown("### Example Queries")
    for query in APP_CONFIG.example_queries:
        if st.sidebar.button(f"🔍 {query}"):
            st.session_state.natural_query = query
            st.experimental_rerun()


def process_query(
    text2sql: Text2SQLCoordinator,
    db: DatabaseManager,
    query: str
) -> Optional[Dict[str, Any]]:
    """Process natural language query and return results.
    
    Args:
        text2sql: Text2SQL coordinator
        db: Database manager
        query: Natural language query
        
    Returns:
        Dictionary with query results and metadata
    """
    try:
        # Convert natural language to SQL
        logger.info(f"Converting query: {query}")
        result = text2sql.convert_to_sql(query)
        
        # Validate SQL query
        logger.debug(f"Validating SQL: {result.sql}")
        is_valid, error = db.validate_query(result.sql)
        if not is_valid:
            error_msg = f"Invalid SQL query: {error}"
            logger.error(error_msg)
            st.error(error_msg)
            return None
        
        # Execute query and get results
        logger.debug("Executing query")
        df, error = db.execute_query(result.sql)
        if error:
            error_msg = f"Error executing query: {error}"
            logger.error(error_msg)
            st.error(error_msg)
            return None
        
        # Get query metadata
        logger.debug("Getting query metadata")
        metadata = db.get_query_metadata(result.sql)
        
        return {
            "sql": result.sql,
            "confidence": result.confidence,
            "processing_time": result.processing_time,
            "results": df,
            "metadata": metadata
        }
    except Exception as e:
        logger.error(f"Error processing query: {e}", exc_info=True)
        st.error(f"An error occurred: {str(e)}")
        return None


def main() -> None:
    """Main Streamlit app."""
    try:
        logger.info("Starting Streamlit app")
        st.set_page_config(
            page_title=APP_CONFIG.title,
            page_icon=APP_CONFIG.icon,
            layout="wide"
        )
        
        # Initialize components
        logger.debug("Initializing Text2SQL coordinator")
        text2sql = initialize_text2sql()
        
        logger.debug("Initializing DatabaseManager")
        db = DatabaseManager(DB_CONFIG)
        
        # Title and description
        st.title(f"{APP_CONFIG.icon} {APP_CONFIG.title}")
        st.markdown("""
            Convert natural language questions into SQL queries and explore your database.
            Type your question below or try one of the example queries from the sidebar.
        """)
        
        # Sidebar components
        logger.debug("Setting up sidebar components")
        display_schema_info()
        display_example_queries()
        display_query_history()
        
        # Main query input
        query = st.text_area(
            "Enter your question:",
            value=st.session_state.get("natural_query", ""),
            height=100,
            placeholder="e.g., Show all users who joined last month"
        )
        
        # Process query when submitted
        if st.button("🔍 Convert to SQL", type="primary"):
            if not query:
                st.warning("Please enter a question first.")
                return
            
            logger.info(f"Processing query: {query}")
            with st.spinner("Processing query..."):
                result = process_query(text2sql, db, query)
                
                if result:
                    logger.debug("Query processed successfully")
                    # Display SQL query
                    st.markdown("### Generated SQL")
                    st.code(result["sql"], language="sql")
                    
                    # Display confidence and timing
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Confidence", f"{result['confidence']:.2%}")
                    col2.metric("Processing Time", f"{result['processing_time']:.3f}s")
                    col3.metric(
                        "Tables Referenced",
                        len(result["metadata"].tables_referenced)
                    )
                    
                    # Display results
                    st.markdown("### Query Results")
                    st.dataframe(
                        result["results"],
                        use_container_width=True,
                        hide_index=True
                    )
                    
                    # Add to history
                    add_to_history(
                        query=query,
                        sql=result["sql"],
                        success=True,
                        timestamp=datetime.now(),
                        metadata=result["metadata"],
                        confidence=result["confidence"],
                        processing_time=result["processing_time"]
                    )
                    
                    # Clear input after successful query
                    st.session_state.natural_query = ""
                    
                else:
                    logger.error("Query processing failed")
                    # Add failed query to history
                    add_to_history(
                        query=query,
                        sql="Query failed",
                        success=False,
                        timestamp=datetime.now(),
                        error_message="Query processing failed"
                    )
    except Exception as e:
        logger.error(f"Error in main app: {e}", exc_info=True)
        st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        logger.info("Starting application")
        main()
    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)
        st.error("An unexpected error occurred. Please check the logs for details.")
