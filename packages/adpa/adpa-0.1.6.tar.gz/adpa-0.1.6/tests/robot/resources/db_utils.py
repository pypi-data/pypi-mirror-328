"""Database utilities for Robot Framework tests."""
from robot.api.deco import keyword
from DatabaseLibrary import DatabaseLibrary

class DatabaseUtils:
    """Database utilities for Robot Framework tests."""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        """Initialize database utilities."""
        self.db = DatabaseLibrary()

    @keyword('Connect To Test Database')
    def connect_to_test_database(self):
        """Connect to test database."""
        try:
            self.db.connect_to_database(
                dbapiModuleName='psycopg2',
                dbName='adpa_test',
                dbUsername='adpa_test',
                dbPassword='test_password',
                dbHost='localhost',
                dbPort=5432
            )
            print("Successfully connected to database")
            return True
        except Exception as e:
            print(f"Failed to connect to database: {str(e)}")
            return False

    @keyword('Execute Test Query')
    def execute_test_query(self, query):
        """Execute a test query."""
        try:
            return self.db.execute_sql_string(query)
        except Exception as e:
            print(f"Failed to execute query: {str(e)}")
            return None
