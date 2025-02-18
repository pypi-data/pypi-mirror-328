"""Test database connection."""
import psycopg2

# Database connection parameters
DB_PARAMS = {
    'dbname': 'd9ia9eei6rkq90',
    'user': 'uem4h7dfn2ghbi',
    'password': 'p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb',
    'host': 'c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com',
    'port': '5432'
}

def write_log(message):
    """Write message to file and print to console."""
    with open('db_test_output.txt', 'a') as f:
        f.write(message + '\n')
    print(message)

def main():
    """Test database connection."""
    write_log("Connecting to database...")
    
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        write_log("Connection successful!")
        
        with conn.cursor() as cur:
            # Test simple query
            cur.execute("SELECT current_database(), current_user, version()")
            db, user, version = cur.fetchone()
            write_log(f"Connected to database: {db}")
            write_log(f"Current user: {user}")
            write_log(f"PostgreSQL version: {version}")
    
    except Exception as e:
        write_log(f"Error: {str(e)}")
        write_log(f"Error type: {type(e)}")
    finally:
        if 'conn' in locals():
            conn.close()
            write_log("Database connection closed")

if __name__ == "__main__":
    # Clear the log file
    with open('db_test_output.txt', 'w') as f:
        f.write('')
    main()
