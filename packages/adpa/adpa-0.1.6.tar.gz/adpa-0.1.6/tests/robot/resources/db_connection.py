# -*- coding: utf-8 -*-
"""Database connection helper for Robot Framework tests."""
import os
import psycopg2
from robot.libraries.BuiltIn import BuiltIn

def setup_database_connection():
    """Connect to PostgreSQL database using environment variables."""
    try:
        # Get environment variables with defaults
        db_name = os.getenv('POSTGRES_DATABASE', 'adpa_test')
        user = os.getenv('POSTGRES_USER', 'adpa_test')
        password = os.getenv('POSTGRES_PASSWORD', 'test_password')
        host = os.getenv('POSTGRES_HOST', 'localhost')

        # Print debug information
        print(f"Database connection parameters:")
        print(f"Database: {db_name}")
        print(f"User: {user}")
        print(f"Host: {host}")
        print(f"Port: 5432")

        # Get DatabaseLibrary instance
        db = BuiltIn().get_library_instance('DatabaseLibrary')
        
        # Connect using DatabaseLibrary with hardcoded port
        db.connect_to_database(
            dbapiModuleName='psycopg2',
            dbName=db_name,
            dbUsername=user,
            dbPassword=password,
            dbHost=host,
            dbPort=5432  # Using direct integer value
        )
        print("Successfully connected to database")
        return True
    except Exception as e:
        print(f"Failed to connect to database: {str(e)}")
        return False
