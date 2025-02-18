"""Database storage management page for ADPA Framework."""
import streamlit as st
from typing import Dict, List, Optional
import yaml

from adpa.core.database import DatabaseManager
from adpa.core.types import DatabaseConfig, TableSchema
from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.database.models.database import DatabaseModel
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

def render_database_page():
    """Render the database storage page."""
    st.title("💾 Database Storage")
    
    # Initialize database manager
    db_manager = DatabaseManager()
    
    # Sidebar
    st.sidebar.markdown("### Database Actions")
    action = st.sidebar.selectbox(
        "Select Action",
        ["View Tables", "Create Table", "Manage Connections"]
    )
    
    if action == "View Tables":
        view_tables(db_manager)
    elif action == "Create Table":
        create_table(db_manager)
    else:
        manage_connections(db_manager)

def view_tables(db_manager: DatabaseManager):
    """View database tables."""
    st.subheader("Database Tables")
    
    # Connection selection
    connection = st.selectbox(
        "Select Connection",
        db_manager.list_connections()
    )
    
    try:
        tables = db_manager.list_tables(connection)
        
        if not tables:
            st.info("No tables found in this database.")
            return
        
        for table in tables:
            with st.expander(f"Table: {table.name}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Schema**: {table.schema}")
                    st.markdown(f"**Created**: {table.created_at}")
                    st.markdown(f"**Last Modified**: {table.last_modified}")
                
                with col2:
                    st.markdown(f"**Rows**: {table.row_count}")
                    st.markdown(f"**Size**: {table.size_mb:.2f} MB")
                    st.markdown(f"**Indexes**: {len(table.indexes)}")
                
                # Table preview
                if st.button(f"Preview {table.name}", key=f"preview_{table.name}"):
                    preview_data = db_manager.preview_table(connection, table.name)
                    st.dataframe(preview_data)
                
                # Table operations
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button(f"Export {table.name}", key=f"export_{table.name}"):
                        try:
                            file_path = db_manager.export_table(
                                connection,
                                table.name
                            )
                            st.success(f"Table exported to: {file_path}")
                        except Exception as e:
                            logger.error(f"Export failed: {str(e)}")
                            st.error(f"Export failed: {str(e)}")
                
                with col2:
                    if st.button(f"Delete {table.name}", key=f"delete_{table.name}"):
                        try:
                            db_manager.delete_table(connection, table.name)
                            st.success(f"Table '{table.name}' deleted successfully!")
                            st.rerun()
                        except Exception as e:
                            logger.error(f"Delete failed: {str(e)}")
                            st.error(f"Delete failed: {str(e)}")
                
    except Exception as e:
        logger.error(f"Failed to list tables: {str(e)}")
        st.error(f"Failed to list tables: {str(e)}")

def create_table(db_manager: DatabaseManager):
    """Create a new database table."""
    st.subheader("Create Table")
    
    # Connection selection
    connection = st.selectbox(
        "Select Connection",
        db_manager.list_connections()
    )
    
    # Table details
    name = st.text_input("Table Name")
    description = st.text_area("Description")
    
    # Column definition
    st.markdown("### Define Columns")
    
    columns = []
    num_columns = st.number_input(
        "Number of Columns",
        min_value=1,
        max_value=50,
        value=1
    )
    
    for i in range(num_columns):
        st.markdown(f"#### Column {i+1}")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            col_name = st.text_input("Name", key=f"col_name_{i}")
        
        with col2:
            col_type = st.selectbox(
                "Type",
                ["string", "integer", "float", "boolean", "datetime", "json"],
                key=f"col_type_{i}"
            )
        
        with col3:
            col_nullable = st.checkbox("Nullable", key=f"col_nullable_{i}")
        
        columns.append({
            "name": col_name,
            "type": col_type,
            "nullable": col_nullable
        })
    
    # Indexes
    st.markdown("### Define Indexes")
    
    indexes = []
    num_indexes = st.number_input(
        "Number of Indexes",
        min_value=0,
        max_value=10,
        value=0
    )
    
    for i in range(num_indexes):
        st.markdown(f"#### Index {i+1}")
        col1, col2 = st.columns(2)
        
        with col1:
            idx_name = st.text_input("Name", key=f"idx_name_{i}")
            idx_columns = st.multiselect(
                "Columns",
                [col["name"] for col in columns if col["name"]],
                key=f"idx_columns_{i}"
            )
        
        with col2:
            idx_type = st.selectbox(
                "Type",
                ["btree", "hash", "gin", "gist"],
                key=f"idx_type_{i}"
            )
            idx_unique = st.checkbox("Unique", key=f"idx_unique_{i}")
        
        if idx_name and idx_columns:
            indexes.append({
                "name": idx_name,
                "columns": idx_columns,
                "type": idx_type,
                "unique": idx_unique
            })
    
    if st.button("Create Table"):
        if not name:
            st.warning("Please enter a table name.")
            return
        
        if not any(col["name"] for col in columns):
            st.warning("Please define at least one column.")
            return
        
        try:
            schema = TableSchema(
                name=name,
                description=description,
                columns=columns,
                indexes=indexes
            )
            
            db_manager.create_table(connection, schema)
            st.success(f"Table '{name}' created successfully!")
            
        except Exception as e:
            logger.error(f"Failed to create table: {str(e)}")
            st.error(f"Failed to create table: {str(e)}")

def manage_connections(db_manager: DatabaseManager):
    """Manage database connections."""
    st.subheader("Manage Connections")
    
    # Add new connection
    st.markdown("### Add Connection")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Connection Name")
        host = st.text_input("Host")
        port = st.number_input("Port", min_value=1, max_value=65535)
    
    with col2:
        database = st.text_input("Database Name")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
    
    if st.button("Add Connection"):
        try:
            config = DatabaseConfig(
                name=name,
                host=host,
                port=port,
                database=database,
                username=username,
                password=password
            )
            
            db_manager.add_connection(config)
            st.success(f"Connection '{name}' added successfully!")
            
        except Exception as e:
            logger.error(f"Failed to add connection: {str(e)}")
            st.error(f"Failed to add connection: {str(e)}")
    
    # List connections
    st.markdown("### Existing Connections")
    connections = db_manager.list_connections()
    
    if not connections:
        st.info("No connections configured.")
        return
    
    for conn in connections:
        with st.expander(f"Connection: {conn.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Host**: {conn.host}")
                st.markdown(f"**Port**: {conn.port}")
                st.markdown(f"**Database**: {conn.database}")
            
            with col2:
                st.markdown(f"**Status**: {conn.status}")
                st.markdown(f"**Tables**: {len(conn.tables)}")
                st.markdown(f"**Size**: {conn.size_mb:.2f} MB")
            
            # Test connection
            if st.button(f"Test {conn.name}", key=f"test_{conn.name}"):
                try:
                    db_manager.test_connection(conn.name)
                    st.success("Connection test successful!")
                except Exception as e:
                    logger.error(f"Connection test failed: {str(e)}")
                    st.error(f"Connection test failed: {str(e)}")
            
            # Remove connection
            if st.button(f"Remove {conn.name}", key=f"remove_{conn.name}"):
                try:
                    db_manager.remove_connection(conn.name)
                    st.success(f"Connection '{conn.name}' removed successfully!")
                    st.rerun()
                except Exception as e:
                    logger.error(f"Failed to remove connection: {str(e)}")
                    st.error(f"Failed to remove connection: {str(e)}")

def main():
    """Main entry point for database storage page."""
    try:
        render_database_page()
    except Exception as e:
        st.error(f"Failed to render database storage page: {str(e)}")
        logger.error(f"Database storage page error: {str(e)}")

if __name__ == "__main__":
    main()
