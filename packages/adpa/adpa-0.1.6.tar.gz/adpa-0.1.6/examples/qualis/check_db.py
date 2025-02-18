"""Check database connectivity and schema."""
import psycopg2
import sys
from psycopg2 import Error

def main():
    """Main function to check database."""
    try:
        # Print attempt
        print("Attempting to connect to database...", flush=True)
        sys.stdout.flush()
        
        # Connect to database
        conn = psycopg2.connect(
            host="c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
            port="5432",
            database="d9ia9eei6rkq90",
            user="uem4h7dfn2ghbi",
            password="p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb"
        )
        
        # Create cursor
        cur = conn.cursor()
        
        # Test connection
        print("Testing connection...", flush=True)
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"PostgreSQL version: {version[0]}", flush=True)
        
        # Check schema
        print("\nChecking schema 'ttt'...", flush=True)
        cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ttt';")
        schema = cur.fetchone()
        if schema:
            print("Schema 'ttt' exists", flush=True)
        else:
            print("Schema 'ttt' does not exist", flush=True)
            return
        
        # List tables
        print("\nListing tables in schema 'ttt'...", flush=True)
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'ttt'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        if tables:
            for table in tables:
                print(f"Table found: {table[0]}", flush=True)
                
                # Get row count
                cur.execute(f"SELECT COUNT(*) FROM ttt.{table[0]};")
                count = cur.fetchone()[0]
                print(f"Row count: {count}", flush=True)
                
                # Show first row
                if count > 0:
                    cur.execute(f"SELECT * FROM ttt.{table[0]} LIMIT 1;")
                    row = cur.fetchone()
                    print(f"Sample row: {row}", flush=True)
        else:
            print("No tables found in schema 'ttt'", flush=True)
        
    except Error as e:
        print(f"Database error occurred:", flush=True)
        print(f"Error: {e}", flush=True)
        print(f"Details: {e.args[0]}", flush=True)
        print(f"pgerror: {e.pgerror if hasattr(e, 'pgerror') else 'N/A'}", flush=True)
        print(f"pgcode: {e.pgcode if hasattr(e, 'pgcode') else 'N/A'}", flush=True)
        
    except Exception as e:
        print(f"An error occurred:", flush=True)
        print(f"Error type: {type(e).__name__}", flush=True)
        print(f"Error message: {str(e)}", flush=True)
        
    finally:
        print("\nClosing connection...", flush=True)
        try:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
            print("Connection closed successfully", flush=True)
        except Exception as e:
            print(f"Error closing connection: {e}", flush=True)

if __name__ == "__main__":
    main()
