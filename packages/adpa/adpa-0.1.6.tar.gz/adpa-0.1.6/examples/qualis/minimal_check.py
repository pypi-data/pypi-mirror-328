"""Minimal database check."""
import sys
import psycopg2

# Print directly to stderr for immediate output
sys.stderr.write("Starting minimal check...\n")
sys.stderr.flush()

try:
    # Connect with connection string
    sys.stderr.write("Connecting to database...\n")
    sys.stderr.flush()
    
    conn = psycopg2.connect(
        "dbname=d9ia9eei6rkq90 user=uem4h7dfn2ghbi password=p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb host=c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com port=5432"
    )
    
    sys.stderr.write("Connected!\n")
    sys.stderr.flush()
    
    with conn.cursor() as cur:
        # Basic version check
        cur.execute('SELECT version();')
        ver = cur.fetchone()
        sys.stderr.write(f"Version: {ver}\n")
        sys.stderr.flush()
        
        # Schema check
        cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ttt';")
        schema = cur.fetchone()
        sys.stderr.write(f"Schema check result: {schema}\n")
        sys.stderr.flush()

except Exception as e:
    sys.stderr.write(f"Error: {str(e)}\n")
    sys.stderr.write(f"Error type: {type(e).__name__}\n")
    sys.stderr.flush()
    raise

finally:
    sys.stderr.write("Check complete.\n")
    sys.stderr.flush()
