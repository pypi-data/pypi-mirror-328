"""Script to check schema ttt and its tables."""
import psycopg2
from tabulate import tabulate
import sys

# Database connection parameters
DB_CONFIG = {
    "host": "c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
    "port": "5432",
    "database": "d9ia9eei6rkq90",
    "user": "uem4h7dfn2ghbi",
    "password": "p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb"
}

def check_connection():
    """Test database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✓ Successfully connected to database")
        return conn
    except psycopg2.Error as e:
        print(f"✗ Failed to connect to database:")
        print(f"  Error: {e}")
        sys.exit(1)

def check_schema(cur):
    """Check if schema exists."""
    try:
        cur.execute("""
            SELECT schema_name, schema_owner 
            FROM information_schema.schemata 
            WHERE schema_name = 'ttt';
        """)
        schema = cur.fetchone()
        if schema:
            print(f"✓ Schema 'ttt' exists (owner: {schema[1]})")
            return True
        else:
            print("✗ Schema 'ttt' does not exist!")
            return False
    except psycopg2.Error as e:
        print(f"✗ Error checking schema:")
        print(f"  Error: {e}")
        return False

def get_tables(cur):
    """Get list of tables in schema."""
    try:
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'ttt'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        if tables:
            print(f"\n✓ Found {len(tables)} tables in schema 'ttt':")
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("\n✗ No tables found in schema 'ttt'")
        return tables
    except psycopg2.Error as e:
        print(f"\n✗ Error getting tables:")
        print(f"  Error: {e}")
        return []

def check_table(cur, table_name):
    """Check table structure and content."""
    print(f"\n=== Checking table: {table_name} ===")
    
    try:
        # Get column information
        cur.execute("""
            SELECT column_name, data_type, character_maximum_length, is_nullable
            FROM information_schema.columns
            WHERE table_schema = 'ttt'
            AND table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))
        columns = cur.fetchall()
        
        print("\nColumns:")
        for col in columns:
            type_info = f"{col[1]}" + (f"({col[2]})" if col[2] else "")
            nullable = "NULL" if col[3] == 'YES' else "NOT NULL"
            print(f"  - {col[0]}: {type_info} {nullable}")
        
        # Get constraints
        cur.execute("""
            SELECT c.conname as constraint_name,
                   c.contype as constraint_type,
                   pg_get_constraintdef(c.oid) as definition
            FROM pg_constraint c
            JOIN pg_namespace n ON n.oid = c.connamespace
            WHERE n.nspname = 'ttt'
            AND c.conrelid::regclass::text = 'ttt.%s';
        """, (table_name,))
        constraints = cur.fetchall()
        
        if constraints:
            print("\nConstraints:")
            for con in constraints:
                con_type = {
                    'p': 'PRIMARY KEY',
                    'f': 'FOREIGN KEY',
                    'u': 'UNIQUE',
                    'c': 'CHECK'
                }.get(con[1], 'OTHER')
                print(f"  - {con[0]} ({con_type}): {con[2]}")
        
        # Get row count
        cur.execute(f"SELECT COUNT(*) FROM ttt.{table_name};")
        count = cur.fetchone()[0]
        print(f"\nRow count: {count}")
        
        # Show sample data
        if count > 0:
            cur.execute(f"SELECT * FROM ttt.{table_name} LIMIT 3;")
            sample = cur.fetchall()
            headers = [col[0] for col in columns]
            print("\nSample data:")
            print(tabulate(sample, headers=headers, tablefmt="grid"))
            
        return True
        
    except psycopg2.Error as e:
        print(f"✗ Error checking table {table_name}:")
        print(f"  Error: {e}")
        return False

def main():
    """Main function to check schema and tables."""
    conn = None
    try:
        # Connect to database
        conn = check_connection()
        cur = conn.cursor()
        
        # Check schema
        if not check_schema(cur):
            return
        
        # Get and check tables
        tables = get_tables(cur)
        for table in tables:
            check_table(cur, table[0])
            
    except Exception as e:
        print(f"\n✗ Unexpected error:")
        print(f"  Error: {e}")
        
    finally:
        if conn:
            conn.close()
            print("\n✓ Database connection closed")

if __name__ == "__main__":
    main()
