"""Test SQL query generation functionality."""
import pytest
from adpa.training.data_generation import DataGenerator, GenerationConfig
from adpa.training.text2sql.schema_extractor import SchemaExtractor
import sqlparse
import sqlite3
import tempfile
import os

# Test schemas
SIMPLE_SCHEMA = {
    "tables": [
        {
            "name": "users",
            "columns": [
                {"name": "id", "type": "INTEGER", "primary_key": True},
                {"name": "name", "type": "TEXT", "nullable": False},
                {"name": "email", "type": "TEXT", "unique": True}
            ]
        },
        {
            "name": "orders",
            "columns": [
                {"name": "id", "type": "INTEGER", "primary_key": True},
                {"name": "user_id", "type": "INTEGER", "foreign_key": "users.id"},
                {"name": "amount", "type": "DECIMAL(10,2)"},
                {"name": "status", "type": "TEXT"}
            ]
        }
    ],
    "relationships": [
        {
            "from_table": "orders",
            "to_table": "users",
            "from_columns": ["user_id"],
            "to_columns": ["id"]
        }
    ]
}

@pytest.fixture
def generator():
    """Create data generator instance."""
    return DataGenerator(model_name="gpt2-medium", use_gpu=False)

@pytest.fixture
def test_db():
    """Create test database."""
    db_file = tempfile.NamedTemporaryFile(delete=False)
    conn = sqlite3.connect(db_file.name)
    
    # Create tables
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    """)
    
    conn.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            amount DECIMAL(10,2),
            status TEXT
        )
    """)
    
    # Insert test data
    conn.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        [
            ("John Doe", "john@example.com"),
            ("Jane Smith", "jane@example.com")
        ]
    )
    
    conn.executemany(
        "INSERT INTO orders (user_id, amount, status) VALUES (?, ?, ?)",
        [
            (1, 100.50, "completed"),
            (1, 75.25, "pending"),
            (2, 200.00, "completed")
        ]
    )
    
    conn.commit()
    conn.close()
    
    yield db_file.name
    os.unlink(db_file.name)

class TestSQLGeneration:
    """Test SQL query generation."""

    def test_simple_queries(self, generator):
        """Test generation of simple SELECT queries."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        assert len(queries) == 5
        for query in queries:
            # Validate query structure
            assert "SELECT" in query["sql"].upper()
            assert sqlparse.parse(query["sql"])
            assert query["complexity"] in ["simple", "medium", "complex"]

    def test_join_queries(self, generator):
        """Test generation of JOIN queries."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        join_queries = [q for q in queries if "JOIN" in q["sql"].upper()]
        assert len(join_queries) > 0
        
        for query in join_queries:
            # Validate join conditions
            assert "orders" in query["sql"]
            assert "users" in query["sql"]
            assert "user_id" in query["sql"]

    def test_aggregate_queries(self, generator):
        """Test generation of aggregate queries."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        agg_queries = [
            q for q in queries
            if any(fn in q["sql"].upper() for fn in ["COUNT", "SUM", "AVG"])
        ]
        assert len(agg_queries) > 0

    def test_query_execution(self, generator, test_db):
        """Test that generated queries are executable."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        conn = sqlite3.connect(test_db)
        for query in queries:
            try:
                conn.execute(query["sql"])
            except sqlite3.Error as e:
                pytest.fail(f"Query execution failed: {e}\nQuery: {query['sql']}")
        conn.close()

    def test_schema_extraction(self, test_db):
        """Test schema extraction from database."""
        extractor = SchemaExtractor(f"sqlite:///{test_db}")
        schema = extractor.extract_schema()
        
        # Validate extracted schema
        assert len(schema["tables"]) == 2
        assert schema["tables"][0]["name"] == "users"
        assert schema["tables"][1]["name"] == "orders"
        
        # Validate relationships
        assert len(schema["relationships"]) == 1
        rel = schema["relationships"][0]
        assert rel["from_table"] == "orders"
        assert rel["to_table"] == "users"

    @pytest.mark.parametrize("complexity", ["simple", "medium", "complex"])
    def test_query_complexity(self, generator, complexity):
        """Test generation of queries with different complexity levels."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        complexity_queries = [q for q in queries if q["complexity"] == complexity]
        assert len(complexity_queries) > 0
        
        for query in complexity_queries:
            if complexity == "simple":
                assert "JOIN" not in query["sql"].upper()
                assert "GROUP BY" not in query["sql"].upper()
            elif complexity == "complex":
                assert any(
                    term in query["sql"].upper()
                    for term in ["JOIN", "GROUP BY", "HAVING", "EXISTS"]
                )

    def test_error_handling(self, generator):
        """Test handling of invalid schemas."""
        invalid_schema = {
            "tables": [
                {
                    "name": "invalid",
                    "columns": [
                        {"name": "id", "type": "INVALID_TYPE"}
                    ]
                }
            ]
        }
        
        with pytest.raises(ValueError):
            generator.generate_sql_queries(invalid_schema, GenerationConfig(num_samples=1))

    def test_query_validation(self, generator):
        """Test SQL query validation."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        for query in queries:
            # Parse and validate SQL
            parsed = sqlparse.parse(query["sql"])
            assert len(parsed) == 1
            assert parsed[0].get_type() == "SELECT"
            
            # Check for basic SQL injection patterns
            sql = query["sql"].upper()
            assert "DROP" not in sql
            assert "DELETE" not in sql
            assert "UPDATE" not in sql
            assert ";" not in sql  # No multiple statements

    def test_natural_language_mapping(self, generator):
        """Test natural language descriptions of queries."""
        config = GenerationConfig(num_samples=5)
        queries = generator.generate_sql_queries(SIMPLE_SCHEMA, config)
        
        for query in queries:
            assert "natural" in query
            assert len(query["natural"]) > 0
            assert isinstance(query["natural"], str)
            
            # Verify natural language matches SQL
            if "JOIN" in query["sql"].upper():
                assert any(
                    term in query["natural"].lower()
                    for term in ["join", "combine", "related"]
                )
            if "GROUP BY" in query["sql"].upper():
                assert any(
                    term in query["natural"].lower()
                    for term in ["group", "aggregate", "summarize"]
                )
