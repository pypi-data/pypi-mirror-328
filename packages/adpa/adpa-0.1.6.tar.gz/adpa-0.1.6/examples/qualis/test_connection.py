"""Test PostgreSQL connection and schema."""
import psycopg2
import os
import sys
from datetime import datetime

def log(message):
    """Write message to both console and file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    
    # Write to console
    print(full_message, flush=True)
    sys.stdout.flush()
    
    # Write to file
    with open("connection_test.log", "a", encoding="utf-8") as f:
        f.write(full_message + "\n")
        f.flush()
        os.fsync(f.fileno())

# Database configuration
db_config = {
    "dbname": "d9ia9eei6rkq90",
    "user": "uem4h7dfn2ghbi",
    "password": "p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb",
    "host": "c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
    "port": "5432"
}

try:
    # Start test
    log("Starting connection test...")
    
    # Try connection
    log("Attempting to connect to database...")
    conn = psycopg2.connect(**db_config)
    log("Successfully connected to database!")
    
    # Create cursor
    cur = conn.cursor()
    
    # Test basic query
    log("Testing basic query...")
    cur.execute("SELECT current_database(), current_user, version();")
    db, user, version = cur.fetchone()
    log(f"Database: {db}")
    log(f"User: {user}")
    log(f"Version: {version}")
    
    # Check schema
    log("\nChecking schema 'ttt'...")
    cur.execute("""
        SELECT schema_name, schema_owner 
        FROM information_schema.schemata 
        WHERE schema_name = 'ttt';
    """)
    schema = cur.fetchone()
    if schema:
        log(f"Found schema 'ttt' (owner: {schema[1]})")
        
        # List tables
        log("\nListing tables in schema 'ttt'...")
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'ttt'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        if tables:
            log(f"Found {len(tables)} tables:")
            for table in tables:
                table_name = table[0]
                log(f"\nTable: {table_name}")
                
                # Get column info
                cur.execute("""
                    SELECT column_name, data_type, is_nullable
                    FROM information_schema.columns
                    WHERE table_schema = 'ttt'
                    AND table_name = %s
                    ORDER BY ordinal_position;
                """, (table_name,))
                columns = cur.fetchall()
                log("Columns:")
                for col in columns:
                    log(f"  - {col[0]} ({col[1]}) {'NULL' if col[2]=='YES' else 'NOT NULL'}")
                
                # Get row count
                cur.execute(f"SELECT COUNT(*) FROM ttt.{table_name};")
                count = cur.fetchone()[0]
                log(f"Row count: {count}")
        else:
            log("No tables found in schema 'ttt'")
    else:
        log("Schema 'ttt' not found")

except psycopg2.Error as e:
    log(f"\nDatabase error occurred:")
    log(f"Error: {str(e)}")
    log(f"pgerror: {e.pgerror if hasattr(e, 'pgerror') else 'N/A'}")
    log(f"pgcode: {e.pgcode if hasattr(e, 'pgcode') else 'N/A'}")
    
except Exception as e:
    log(f"\nUnexpected error occurred:")
    log(f"Error type: {type(e).__name__}")
    log(f"Error message: {str(e)}")
    
finally:
    log("\nCleaning up...")
    if 'cur' in locals():
        cur.close()
        log("Cursor closed")
    if 'conn' in locals():
        conn.close()
        log("Connection closed")
    
log("\nTest complete. Check connection_test.log for details.")
