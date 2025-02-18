"""
Text2SQL Streamlit Application
"""
import streamlit as st
from typing import Optional, Dict, List
import json
from pathlib import Path
from datetime import datetime

from adpa.text2sql.types import (
    QueryResult, QueryContext, QueryMetrics,
    GeneratorConfig, SchemaConfig
)
from adpa.text2sql.models import (
    Column, Table, Index, Schema,
    DatabaseConfig, ValidationResult
)
from adpa.text2sql.generator import SQLGenerator
from adpa.text2sql.validation import SQLValidator
from adpa.text2sql.utils import (
    analyze_query_complexity,
    extract_table_references,
    suggest_indexes,
    suggest_joins
)

def initialize_app() -> None:
    """Initialize the Streamlit application."""
    st.set_page_config(
        page_title="Text2SQL Assistant",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    if "history" not in st.session_state:
        st.session_state.history = []
    if "config" not in st.session_state:
        st.session_state.config = load_default_config()

def render_sidebar() -> None:
    """Render the sidebar with settings and history."""
    with st.sidebar:
        st.title("Settings")
        
        # Configuration
        st.subheader("Configuration")
        db_url = st.text_input("Database URL", st.session_state.config.get("db_url", ""))
        schema_path = st.text_input("Schema Path", st.session_state.config.get("schema_path", ""))
        
        if st.button("Save Settings"):
            st.session_state.config.update({
                "db_url": db_url,
                "schema_path": schema_path
            })
            st.success("Settings saved!")
        
        # History
        st.subheader("Query History")
        for query in st.session_state.history:
            with st.expander(f"{query['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}"):
                st.text("Query:")
                st.code(query["natural_query"])
                st.text("SQL:")
                st.code(query["sql"])

def load_default_config() -> Dict:
    """Load default configuration."""
    return {
        "db_url": "sqlite:///database.db",
        "schema_path": "schema.json",
        "max_history": 50,
        "show_metrics": True
    }

def main() -> None:
    """Main application function."""
    initialize_app()
    
    st.title("Text2SQL Assistant")
    st.write("Convert natural language queries to SQL")
    
    # Query input
    query = st.text_area("Enter your query:", height=100)
    
    if st.button("Generate SQL"):
        if not query:
            st.error("Please enter a query!")
            return
        
        try:
            # Initialize components
            generator = SQLGenerator(
                config=GeneratorConfig(
                    database_url=st.session_state.config["db_url"],
                    schema_path=st.session_state.config["schema_path"]
                )
            )
            validator = SQLValidator()
            
            # Generate SQL
            result = generator.generate(query)
            
            # Validate
            validation = validator.validate_query(result.sql)
            if not validation.is_valid:
                st.error(f"Generated SQL is invalid: {validation.errors}")
                return
            
            # Display results
            st.subheader("Generated SQL")
            st.code(result.sql, language="sql")
            
            # Show metrics if enabled
            if st.session_state.config["show_metrics"]:
                st.subheader("Query Metrics")
                metrics = result.metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Complexity", metrics.complexity)
                with col2:
                    st.metric("Tables", len(metrics.tables))
                with col3:
                    st.metric("Generation Time", f"{metrics.generation_time:.2f}s")
            
            # Add to history
            st.session_state.history.insert(0, {
                "timestamp": datetime.now(),
                "natural_query": query,
                "sql": result.sql,
                "metrics": result.metrics
            })
            
            # Limit history size
            if len(st.session_state.history) > st.session_state.config["max_history"]:
                st.session_state.history.pop()
            
        except Exception as e:
            st.error(f"Error generating SQL: {str(e)}")
    
    # Render sidebar
    render_sidebar()

if __name__ == "__main__":
    main()
