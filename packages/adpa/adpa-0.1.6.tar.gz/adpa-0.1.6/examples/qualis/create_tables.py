"""Database creation script for qualification management system.

This script creates the necessary database schema and tables for managing
qualifications, persons, and their relationships. It also imports initial data
from Excel files.

Typical usage:
    python create_tables.py

Tables created:
    - ttt.ttz_person: Stores person information
    - ttt.ttz_qualification: Stores qualification definitions
    - ttt.ttz_person_qualification: Maps persons to their qualifications
"""
from typing import Dict, Optional
import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection, cursor
import os
from datetime import datetime


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


def create_schema(cur: cursor) -> None:
    """Create the ttt schema if it doesn't exist.
    
    Args:
        cur: Database cursor for executing commands
        
    Raises:
        psycopg2.Error: If schema creation fails
    """
    cur.execute("CREATE SCHEMA IF NOT EXISTS ttt;")


def create_tables(cur: cursor) -> None:
    """Create the required tables with prefix ttz_.
    
    Args:
        cur: Database cursor for executing commands
        
    Raises:
        psycopg2.Error: If table creation fails
    """
    # Create person table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ttt.ttz_person (
            person_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(255) UNIQUE,
            birth_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create qualification table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ttt.ttz_qualification (
            qualification_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            level INTEGER,
            valid_from DATE,
            valid_until DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create person_qualification table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ttt.ttz_person_qualification (
            person_qualification_id SERIAL PRIMARY KEY,
            person_id INTEGER REFERENCES ttt.ttz_person(person_id),
            qualification_id INTEGER REFERENCES ttt.ttz_qualification(qualification_id),
            acquired_date DATE,
            expiry_date DATE,
            status VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(person_id, qualification_id)
        );
    """)


def import_excel_data(cur: cursor) -> None:
    """Import data from Excel files into the database.
    
    Args:
        cur: Database cursor for executing commands
        
    Raises:
        FileNotFoundError: If Excel files are not found
        pd.errors.EmptyDataError: If Excel files are empty
        psycopg2.Error: If data import fails
    """
    # Import person data
    df_person = pd.read_excel("person.xlsx")
    for _, row in df_person.iterrows():
        cur.execute("""
            INSERT INTO ttt.ttz_person (first_name, last_name, email, birth_date)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (email) DO UPDATE 
            SET first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name,
                birth_date = EXCLUDED.birth_date,
                updated_at = CURRENT_TIMESTAMP;
        """, (row["first_name"], row["last_name"], row["email"], row["birth_date"]))
    
    # Import qualification data
    df_qual = pd.read_excel("qualification.xlsx")
    for _, row in df_qual.iterrows():
        cur.execute("""
            INSERT INTO ttt.ttz_qualification (name, description, level, valid_from, valid_until)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (qualification_id) DO UPDATE 
            SET name = EXCLUDED.name,
                description = EXCLUDED.description,
                level = EXCLUDED.level,
                valid_from = EXCLUDED.valid_from,
                valid_until = EXCLUDED.valid_until,
                updated_at = CURRENT_TIMESTAMP;
        """, (row["name"], row["description"], row["level"], 
              row["valid_from"], row["valid_until"]))
    
    # Import person_qualification data
    df_pq = pd.read_excel("person_qualification.xlsx")
    for _, row in df_pq.iterrows():
        cur.execute("""
            INSERT INTO ttt.ttz_person_qualification 
            (person_id, qualification_id, acquired_date, expiry_date, status)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (person_id, qualification_id) DO UPDATE 
            SET acquired_date = EXCLUDED.acquired_date,
                expiry_date = EXCLUDED.expiry_date,
                status = EXCLUDED.status,
                updated_at = CURRENT_TIMESTAMP;
        """, (row["person_id"], row["qualification_id"], 
              row["acquired_date"], row["expiry_date"], row["status"]))


def main() -> None:
    """Main function to set up the database schema and import data."""
    conn: Optional[connection] = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            print("Creating schema...")
            create_schema(cur)
            
            print("Creating tables...")
            create_tables(cur)
            
            print("Importing data...")
            import_excel_data(cur)
            
            conn.commit()
            print("Database setup completed successfully!")
            
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {str(e)}")
        raise
    
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
