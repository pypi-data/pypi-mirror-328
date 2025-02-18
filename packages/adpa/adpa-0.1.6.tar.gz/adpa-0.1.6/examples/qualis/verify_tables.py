"""Database verification script for qualification management system.

This script verifies the database schema and tables created for the qualification
management system. It provides detailed information about table structure and
content.

Typical usage:
    python verify_tables.py
"""
from typing import Dict, List, Tuple, Optional
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection, cursor


# Database connection parameters
DB_CONFIG: Dict[str, str] = {
    "host": "c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
    "port": "5432",
    "database": "d9ia9eei6rkq90",
    "user": "uem4h7dfn2ghbi",
    "password": "p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb"
}


def get_db_connection() -> connection:
    """Create and return a database connection.
    
    Returns:
        psycopg2.extensions.connection: Database connection object
        
    Raises:
        psycopg2.Error: If connection fails
    """
    return psycopg2.connect(**DB_CONFIG)


def get_tables(cur: cursor) -> List[Tuple[str]]:
    """Get list of tables in the ttt schema.
    
    Args:
        cur: Database cursor for executing commands
        
    Returns:
        List[Tuple[str]]: List of table names
        
    Raises:
        psycopg2.Error: If query fails
    """
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'ttt' 
        AND table_name LIKE 'ttz_%'
        ORDER BY table_name;
    """)
    return cur.fetchall()


def get_column_info(cur: cursor, table_name: str) -> List[Tuple[str, str, Optional[int]]]:
    """Get column information for a specific table.
    
    Args:
        cur: Database cursor for executing commands
        table_name: Name of the table to get column information for
        
    Returns:
        List[Tuple[str, str, Optional[int]]]: List of (column_name, data_type, max_length)
        
    Raises:
        psycopg2.Error: If query fails
    """
    cur.execute("""
        SELECT column_name, data_type, character_maximum_length
        FROM information_schema.columns
        WHERE table_schema = 'ttt'
        AND table_name = %s
        ORDER BY ordinal_position;
    """, (table_name,))
    return cur.fetchall()


def get_row_count(cur: cursor, table_name: str) -> int:
    """Get the number of rows in a table.
    
    Args:
        cur: Database cursor for executing commands
        table_name: Name of the table to count rows for
        
    Returns:
        int: Number of rows in the table
        
    Raises:
        psycopg2.Error: If query fails
    """
    cur.execute(f"SELECT COUNT(*) FROM ttt.{table_name};")
    return cur.fetchone()[0]


def print_table_info(cur: cursor, table_name: str) -> None:
    """Print detailed information about a table.
    
    Args:
        cur: Database cursor for executing commands
        table_name: Name of the table to print information for
        
    Raises:
        psycopg2.Error: If queries fail
    """
    print(f"\nTable: {table_name}")
    
    # Print column information
    columns = get_column_info(cur, table_name)
    print("  Columns:")
    for col_name, data_type, max_length in columns:
        type_info = f"{data_type}" + (f"({max_length})" if max_length else "")
        print(f"    - {col_name}: {type_info}")
    
    # Print row count
    count = get_row_count(cur, table_name)
    print(f"  Row count: {count}")


def verify_tables() -> None:
    """Verify and print information about all tables in the ttt schema."""
    conn: Optional[connection] = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            tables = get_tables(cur)
            
            if not tables:
                print("No tables found in schema 'ttt'")
                return
                
            print("Tables in schema 'ttt':")
            for (table_name,) in tables:
                print_table_info(cur, table_name)
                
    except Exception as e:
        print(f"Error verifying tables: {str(e)}")
        raise
        
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    verify_tables()
