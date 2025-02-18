"""Script to verify imported data in the qualification management system.

This script checks the data in all tables and shows sample records to verify
the import was successful.
"""
from typing import Dict, List, Tuple, Optional
import psycopg2
from psycopg2.extensions import connection, cursor
from tabulate import tabulate
import os

# Database connection parameters from environment variables
DB_CONFIG: Dict[str, str] = {
    "host": os.environ.get("DB_HOST", "c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com"),
    "port": os.environ.get("DB_PORT", "5432"),
    "database": os.environ.get("DB_NAME", "d9ia9eei6rkq90"),
    "user": os.environ.get("DB_USER", "uem4h7dfn2ghbi"),
    "password": os.environ.get("DB_PASSWORD", "p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb")
}


def get_db_connection() -> connection:
    """Create and return a database connection."""
    return psycopg2.connect(**DB_CONFIG)


def show_table_info(cur: cursor, table_name: str) -> None:
    """Display table information."""
    print(f"\n=== {table_name} Table Information ===")
    
    # Get column information
    cur.execute("""
        SELECT column_name, data_type, character_maximum_length
        FROM information_schema.tables t
        JOIN information_schema.columns c 
            ON c.table_name = t.table_name 
            AND c.table_schema = t.table_schema
        WHERE t.table_schema = 'ttt'
        AND t.table_name = %s
        ORDER BY ordinal_position;
    """, (table_name,))
    columns = cur.fetchall()
    
    print("\nColumns:")
    for col in columns:
        col_type = f"{col[1]}" + (f"({col[2]})" if col[2] else "")
        print(f"  - {col[0]}: {col_type}")


def show_person_data(cur: cursor) -> None:
    """Display sample person records."""
    show_table_info(cur, "ttz_person")
    
    cur.execute("""
        SELECT person_id, first_name, last_name, email, birth_date,
               created_at, updated_at
        FROM ttt.ttz_person
        ORDER BY person_id
        LIMIT 5;
    """)
    records = cur.fetchall()
    headers = ["ID", "First Name", "Last Name", "Email", "Birth Date", 
              "Created At", "Updated At"]
    print("\nSample Records:")
    print(tabulate(records, headers=headers, tablefmt="grid"))


def show_qualification_data(cur: cursor) -> None:
    """Display sample qualification records."""
    show_table_info(cur, "ttz_qualification")
    
    cur.execute("""
        SELECT qualification_id, name, description, level, 
               valid_from, valid_until, created_at, updated_at
        FROM ttt.ttz_qualification
        ORDER BY qualification_id
        LIMIT 5;
    """)
    records = cur.fetchall()
    headers = ["ID", "Name", "Description", "Level", "Valid From", 
              "Valid Until", "Created At", "Updated At"]
    print("\nSample Records:")
    print(tabulate(records, headers=headers, tablefmt="grid"))


def show_person_qualification_data(cur: cursor) -> None:
    """Display sample person-qualification mappings."""
    show_table_info(cur, "ttz_person_qualification")
    
    cur.execute("""
        SELECT 
            pq.person_qualification_id,
            p.first_name || ' ' || p.last_name as person_name,
            q.name as qualification_name,
            pq.acquired_date,
            pq.expiry_date,
            pq.status,
            pq.created_at,
            pq.updated_at
        FROM ttt.ttz_person_qualification pq
        JOIN ttt.ttz_person p ON p.person_id = pq.person_id
        JOIN ttt.ttz_qualification q ON q.qualification_id = pq.qualification_id
        ORDER BY pq.person_qualification_id
        LIMIT 5;
    """)
    records = cur.fetchall()
    headers = ["ID", "Person", "Qualification", "Acquired", "Expires", 
              "Status", "Created At", "Updated At"]
    print("\nSample Records:")
    print(tabulate(records, headers=headers, tablefmt="grid"))


def show_statistics(cur: cursor) -> None:
    """Display statistics about the data."""
    print("\n=== Database Statistics ===")
    
    # Person statistics
    cur.execute("""
        SELECT 
            COUNT(*) as total_persons,
            COUNT(DISTINCT email) as unique_emails,
            MIN(birth_date) as earliest_birth,
            MAX(birth_date) as latest_birth,
            COUNT(DISTINCT first_name) as unique_first_names,
            COUNT(DISTINCT last_name) as unique_last_names
        FROM ttt.ttz_person;
    """)
    person_stats = cur.fetchone()
    
    # Qualification statistics
    cur.execute("""
        SELECT 
            COUNT(*) as total_quals,
            COUNT(DISTINCT name) as unique_names,
            MIN(level) as min_level,
            MAX(level) as max_level,
            COUNT(DISTINCT description) as unique_descriptions
        FROM ttt.ttz_qualification;
    """)
    qual_stats = cur.fetchone()
    
    # Person-Qualification statistics
    cur.execute("""
        SELECT 
            COUNT(*) as total_mappings,
            COUNT(DISTINCT person_id) as persons_with_quals,
            COUNT(DISTINCT qualification_id) as quals_assigned,
            COUNT(DISTINCT status) as status_types,
            MIN(acquired_date) as earliest_acquired,
            MAX(expiry_date) as latest_expiry
        FROM ttt.ttz_person_qualification;
    """)
    pq_stats = cur.fetchone()
    
    print("\nPerson Table Statistics:")
    print(f"  - Total Persons: {person_stats[0]}")
    print(f"  - Unique Emails: {person_stats[1]}")
    print(f"  - Birth Date Range: {person_stats[2]} to {person_stats[3]}")
    print(f"  - Unique First Names: {person_stats[4]}")
    print(f"  - Unique Last Names: {person_stats[5]}")
    
    print("\nQualification Table Statistics:")
    print(f"  - Total Qualifications: {qual_stats[0]}")
    print(f"  - Unique Names: {qual_stats[1]}")
    print(f"  - Level Range: {qual_stats[2]} to {qual_stats[3]}")
    print(f"  - Unique Descriptions: {qual_stats[4]}")
    
    print("\nPerson-Qualification Mapping Statistics:")
    print(f"  - Total Mappings: {pq_stats[0]}")
    print(f"  - Persons with Qualifications: {pq_stats[1]}")
    print(f"  - Qualifications Assigned: {pq_stats[2]}")
    print(f"  - Different Status Types: {pq_stats[3]}")
    print(f"  - Date Range: {pq_stats[4]} to {pq_stats[5]}")
    
    # Status distribution
    cur.execute("""
        SELECT status, COUNT(*) as count
        FROM ttt.ttz_person_qualification
        GROUP BY status
        ORDER BY count DESC;
    """)
    status_dist = cur.fetchall()
    print("\nQualification Status Distribution:")
    for status, count in status_dist:
        print(f"  - {status}: {count}")


def main() -> None:
    """Main function to verify imported data."""
    conn: Optional[connection] = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            print("=== Data Verification Report ===")
            show_person_data(cur)
            show_qualification_data(cur)
            show_person_qualification_data(cur)
            show_statistics(cur)
            
    except Exception as e:
        print(f"Error verifying data: {str(e)}")
        raise
        
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
