# -*- coding: utf-8 -*-
"""Database configuration for Robot Framework tests."""
import os

def get_connection_params():
    """Get database connection parameters."""
    return {
        'dbapiModuleName': 'psycopg2',
        'dbName': os.getenv('POSTGRES_DATABASE', 'adpa_test'),
        'dbUsername': os.getenv('POSTGRES_USER', 'adpa_test'),
        'dbPassword': os.getenv('POSTGRES_PASSWORD', 'test_password'),
        'dbHost': os.getenv('POSTGRES_HOST', 'localhost'),
        'dbPort': int(os.getenv('POSTGRES_PORT', '5432')),
    }
