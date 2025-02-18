"""Check database using psycopg2 with explicit output."""
import psycopg2
import traceback
import os

# Database URL
DB_URL = "postgres://uem4h7dfn2ghbi:p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d9ia9eei6rkq90"

def write_output(message):
    """Write output to both console and file."""
    print(message)
    with open("db_check_output.txt", "a") as f:
        f.write(message + "\n")

try:
    write_output("Starting database check...")
    
    # Connect to the database
    write_output("Connecting to database...")
    conn = psycopg2.connect(DB_URL)
    write_output("Connected successfully!")
    
    # Create a cursor
    cur = conn.cursor()
    
    # Check schema
    write_output("\nChecking schema 'ttt'...")
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ttt';")
    schema = cur.fetchone()
    write_output(f"Schema check result: {schema}")
    
    if schema:
        # List tables
        write_output("\nListing tables in schema 'ttt'...")
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'ttt'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        write_output(f"Found tables: {tables}")
        
        for table in tables:
            table_name = table[0]
            write_output(f"\nChecking table: {table_name}")
            
            # Get column info
            cur.execute(f"""
                SELECT column_name, data_type, character_maximum_length
                FROM information_schema.columns
                WHERE table_schema = 'ttt'
                AND table_name = '{table_name}'
                ORDER BY ordinal_position;
            """)
            columns = cur.fetchall()
            write_output(f"Columns: {columns}")
            
            # Get row count
            cur.execute(f"SELECT COUNT(*) FROM ttt.{table_name};")
            count = cur.fetchone()[0]
            write_output(f"Row count: {count}")
            
            # Get sample data
            if count > 0:
                cur.execute(f"SELECT * FROM ttt.{table_name} LIMIT 1;")
                sample = cur.fetchone()
                write_output(f"Sample row: {sample}")
    
except Exception as e:
    write_output(f"\nError occurred:")
    write_output(f"Error type: {type(e).__name__}")
    write_output(f"Error message: {str(e)}")
    write_output("\nTraceback:")
    write_output(traceback.format_exc())
    
finally:
    write_output("\nClosing connection...")
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
    write_output("Connection closed.")
    
write_output("\nCheck complete. Results written to db_check_output.txt")
