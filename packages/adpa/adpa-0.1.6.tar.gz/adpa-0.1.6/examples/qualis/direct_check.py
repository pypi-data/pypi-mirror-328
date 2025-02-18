"""Direct SQL check of schema ttt."""
import psycopg2

# Database connection parameters
conn = psycopg2.connect(
    host="c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
    port="5432",
    database="d9ia9eei6rkq90",
    user="uem4h7dfn2ghbi",
    password="p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb"
)

cur = conn.cursor()

# Simple direct queries
print("=== Database Connection Test ===")
cur.execute("SELECT current_database(), current_user;")
db_info = cur.fetchone()
print(f"Connected to database: {db_info[0]}")
print(f"Connected as user: {db_info[1]}")

print("\n=== Schema Check ===")
cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ttt';")
if cur.fetchone():
    print("Schema 'ttt' exists")
else:
    print("Schema 'ttt' does not exist")

print("\n=== Tables in Schema 'ttt' ===")
cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'ttt';
""")
tables = cur.fetchall()
if tables:
    for table in tables:
        print(f"Found table: {table[0]}")
else:
    print("No tables found in schema 'ttt'")

cur.close()
conn.close()
