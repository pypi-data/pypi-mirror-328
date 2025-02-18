from robot.api.deco import keyword
from DatabaseLibrary import DatabaseLibrary

class DatabaseHelper:
    """Helper class for database operations."""

    def __init__(self):
        """Initialize the database helper."""
        self.db = DatabaseLibrary()

    @keyword('Connect To Test Database')
    def connect_to_test_database(self):
        """Connect to test database with hardcoded values."""
        self.db.connect_to_database(
            'psycopg2',
            'adpa_test',
            'adpa_test',
            'test_password',
            'localhost',
            5432  # Using direct integer value
        )
