# Database Agent

The Database Agent is a specialized agent designed to handle all PostgreSQL database operations in ADPA. It provides a clean and organized interface for common database tasks, from basic queries to maintenance operations.

## Features

- Execute raw SQL queries
- Table management (create, drop, backup, restore)
- Database optimization
- Performance monitoring
- Table information and statistics

## Usage

### Basic Usage

```python
from adpa.agents.database_agent import DatabaseAgent

# Create agent instance
db_agent = DatabaseAgent()

# Execute a simple query
results = db_agent.execute_query(
    "SELECT * FROM users WHERE age > :min_age",
    {"min_age": 18}
)

# Get table information
table_info = db_agent.get_table_info("users")
```

### Table Management

```python
# Backup a table
db_agent.backup_table("users", "users_backup_20250107")

# Restore from backup
db_agent.restore_table("users_backup_20250107", "users")

# Create all tables
db_agent.create_tables()

# Drop all tables
db_agent.drop_tables()
```

### Optimization and Maintenance

```python
# Optimize a specific table
db_agent.optimize_table("users")

# Vacuum analyze the entire database
db_agent.vacuum_analyze()

# Get table size information
size_info = db_agent.get_table_size("users")

# Monitor slow queries
slow_queries = db_agent.get_slow_queries(min_duration=1000)  # milliseconds
```

## CLI Commands

The database agent functionality is exposed through a convenient CLI interface for easy development and maintenance tasks.

### Basic Commands

```bash
# Initialize database
python scripts/manage_db.py init

# Reset database (with backup)
python scripts/manage_db.py reset --backup

# Get table information
python scripts/manage_db.py info users

# Get table size
python scripts/manage_db.py size users
```

### Backup and Restore

```bash
# Create backup
python scripts/manage_db.py backup users users_backup_20250107

# Restore from backup
python scripts/manage_db.py restore users_backup_20250107 users
```

### Maintenance

```bash
# Optimize specific table
python scripts/manage_db.py optimize users

# Optimize entire database
python scripts/manage_db.py optimize

# View slow queries
python scripts/manage_db.py slow-queries --min-duration 2000
```

### Custom Queries

```bash
# Execute custom query with parameters
python scripts/manage_db.py query "SELECT * FROM users WHERE id = :user_id" --params '{"user_id": 1}'
```

## Configuration

The database agent uses the configuration from your `.env` file. Make sure you have the following variables set:

```env
POSTGRES_HOST=your_host
POSTGRES_PORT=5432
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DATABASE=your_database
```

## Best Practices

1. **Backup Before Changes**: Always create backups before making significant changes to the database structure or data.

2. **Regular Maintenance**: Run optimization tasks regularly to maintain database performance:
   ```bash
   python scripts/manage_db.py optimize
   ```

3. **Monitor Performance**: Regularly check for slow queries to identify potential performance issues:
   ```bash
   python scripts/manage_db.py slow-queries
   ```

4. **Use Parameterized Queries**: Always use parameterized queries to prevent SQL injection:
   ```python
   db_agent.execute_query(
       "SELECT * FROM users WHERE username = :username",
       {"username": user_input}
   )
   ```

## Error Handling

The database agent includes comprehensive error handling. All methods will raise exceptions with descriptive error messages if something goes wrong. It's recommended to wrap database operations in try-except blocks:

```python
try:
    db_agent.execute_query("SELECT * FROM users")
except Exception as e:
    logger.error(f"Database operation failed: {str(e)}")
    # Handle error appropriately
```
