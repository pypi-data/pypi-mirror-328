import pytest
from sqlalchemy import create_engine, text
from adpa.agents.database_agent import DatabaseAgent
from adpa.database.models.base import Base

@pytest.fixture
def db_agent():
    agent = DatabaseAgent()
    # Use a test database URL
    agent.engine = create_engine("postgresql://adpa_test:test_password@localhost:5432/adpa_test")
    return agent

@pytest.fixture
def test_table(db_agent):
    # Create a test table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        value INTEGER
    );
    """
    with db_agent.engine.connect() as conn:
        conn.execute(text(create_table_sql))
        conn.commit()
    
    yield "test_table"
    
    # Cleanup
    with db_agent.engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS test_table;"))
        conn.commit()

def test_execute_query(db_agent, test_table):
    # Insert test data
    insert_sql = """
    INSERT INTO test_table (name, value) VALUES 
    ('test1', 100),
    ('test2', 200);
    """
    db_agent.execute_query(insert_sql)
    
    # Query the data
    result = db_agent.execute_query("SELECT * FROM test_table ORDER BY id;")
    
    assert len(result) == 2
    assert result[0]['name'] == 'test1'
    assert result[0]['value'] == 100

def test_get_table_info(db_agent, test_table):
    info = db_agent.get_table_info(test_table)
    
    expected_columns = {'id', 'name', 'value'}
    actual_columns = {col['column_name'] for col in info}
    
    assert expected_columns.issubset(actual_columns)

def test_backup_and_restore(db_agent, test_table):
    # Insert test data
    db_agent.execute_query(
        "INSERT INTO test_table (name, value) VALUES ('original', 100);"
    )
    
    # Backup the table
    backup_table = "test_table_backup"
    db_agent.backup_table(test_table, backup_table)
    
    # Modify original table
    db_agent.execute_query(
        "UPDATE test_table SET value = 200 WHERE name = 'original';"
    )
    
    # Restore from backup
    db_agent.restore_table(backup_table, test_table)
    
    # Verify restoration
    result = db_agent.execute_query(
        "SELECT * FROM test_table WHERE name = 'original';"
    )
    
    assert len(result) == 1
    assert result[0]['value'] == 100
    
    # Cleanup backup table
    db_agent.execute_query(f"DROP TABLE IF EXISTS {backup_table};")

def test_vacuum_analyze(db_agent, test_table):
    # Should not raise any exceptions
    db_agent.vacuum_analyze(test_table)
    db_agent.vacuum_analyze()  # Test without specific table

def test_get_table_size(db_agent, test_table):
    size_info = db_agent.get_table_size(test_table)
    
    assert 'total_size' in size_info
    assert 'table_size' in size_info
    assert 'index_size' in size_info

def test_optimize_table(db_agent, test_table):
    # Should not raise any exceptions
    db_agent.optimize_table(test_table)
