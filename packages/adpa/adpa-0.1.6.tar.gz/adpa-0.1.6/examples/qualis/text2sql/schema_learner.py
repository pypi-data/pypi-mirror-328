"""Schema learning component that automatically learns and adapts to database structure."""
from typing import Dict, List, Optional, Set, Tuple
import logging
from dataclasses import dataclass, field
import psycopg2
from psycopg2.extensions import connection
import json

@dataclass
class ColumnInfo:
    name: str
    data_type: str
    is_nullable: bool
    default_value: Optional[str]
    constraints: List[str] = field(default_factory=list)
    description: Optional[str] = None
    common_values: Set[str] = field(default_factory=set)
    value_patterns: List[str] = field(default_factory=list)

@dataclass
class TableInfo:
    name: str
    schema: str
    columns: Dict[str, ColumnInfo] = field(default_factory=dict)
    primary_key: List[str] = field(default_factory=list)
    foreign_keys: Dict[str, Tuple[str, str]] = field(default_factory=dict)
    indexes: List[str] = field(default_factory=list)
    description: Optional[str] = None
    sample_data: Dict[str, List[str]] = field(default_factory=dict)

class SchemaLearner:
    def __init__(self, connection_params: Dict[str, str]):
        """Initialize the schema learner with database connection parameters."""
        self.conn_params = connection_params
        self.tables: Dict[str, TableInfo] = {}
        self.relationships: Dict[str, List[Tuple[str, str, str]]] = {}
        self.common_queries: Dict[str, Dict[str, int]] = {}
        self.error_patterns: Dict[str, List[str]] = {}
        self.logger = logging.getLogger(__name__)

    def connect(self) -> connection:
        """Create a database connection."""
        return psycopg2.connect(**self.conn_params)

    def learn_schema(self) -> None:
        """Learn the complete database schema."""
        try:
            with self.connect() as conn:
                self._learn_tables(conn)
                self._learn_relationships(conn)
                self._learn_common_patterns(conn)
                self._analyze_sample_data(conn)
        except Exception as e:
            self.logger.error(f"Error learning schema: {str(e)}")
            raise

    def _learn_tables(self, conn: connection) -> None:
        """Learn table structures and their columns."""
        with conn.cursor() as cur:
            # Get all tables in the schema
            cur.execute("""
                SELECT table_schema, table_name, obj_description(
                    (quote_ident(table_schema) || '.' || quote_ident(table_name))::regclass, 
                    'pg_class'
                ) as description
                FROM information_schema.tables 
                WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
                AND table_type = 'BASE TABLE'
            """)
            
            for schema, table, description in cur.fetchall():
                table_info = TableInfo(name=table, schema=schema, description=description)
                
                # Get column information
                cur.execute("""
                    SELECT column_name, data_type, is_nullable, column_default,
                           col_description(
                               (quote_ident(table_schema) || '.' || quote_ident(table_name))::regclass,
                               ordinal_position
                           ) as description
                    FROM information_schema.columns
                    WHERE table_schema = %s AND table_name = %s
                    ORDER BY ordinal_position
                """, (schema, table))
                
                for col_name, data_type, nullable, default, col_desc in cur.fetchall():
                    table_info.columns[col_name] = ColumnInfo(
                        name=col_name,
                        data_type=data_type,
                        is_nullable=nullable == 'YES',
                        default_value=default,
                        description=col_desc
                    )
                
                self.tables[f"{schema}.{table}"] = table_info

    def _learn_relationships(self, conn: connection) -> None:
        """Learn relationships between tables."""
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    tc.table_schema, 
                    tc.table_name, 
                    kcu.column_name,
                    ccu.table_schema AS foreign_table_schema,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY'
            """)
            
            for row in cur.fetchall():
                (schema, table, column, 
                 foreign_schema, foreign_table, foreign_column) = row
                
                source = f"{schema}.{table}"
                target = f"{foreign_schema}.{foreign_table}"
                
                if source not in self.relationships:
                    self.relationships[source] = []
                
                self.relationships[source].append(
                    (column, target, foreign_column)
                )

    def _learn_common_patterns(self, conn: connection) -> None:
        """Learn common query patterns from query history."""
        with conn.cursor() as cur:
            # This would typically read from a query_history table
            # For now, we'll initialize with some common patterns
            self.common_queries = {
                "list_all": {"SELECT * FROM {table}": 1},
                "find_by_id": {"SELECT * FROM {table} WHERE {pk} = %s": 1},
                "count_all": {"SELECT COUNT(*) FROM {table}": 1},
                "group_by": {"SELECT {column}, COUNT(*) FROM {table} GROUP BY {column}": 1}
            }

    def _analyze_sample_data(self, conn: connection) -> None:
        """Analyze sample data to learn patterns and common values."""
        with conn.cursor() as cur:
            for table_key, table_info in self.tables.items():
                schema, table = table_key.split('.')
                
                # Get sample data for each column
                for column_name, column_info in table_info.columns.items():
                    try:
                        cur.execute(f"""
                            SELECT DISTINCT {column_name}
                            FROM {schema}.{table}
                            WHERE {column_name} IS NOT NULL
                            LIMIT 100
                        """)
                        
                        values = [str(row[0]) for row in cur.fetchall()]
                        column_info.common_values.update(values)
                        
                        # Learn patterns for string columns
                        if column_info.data_type.startswith('character'):
                            self._learn_string_patterns(values, column_info)
                            
                    except Exception as e:
                        self.logger.warning(
                            f"Error analyzing column {column_name} in {table_key}: {str(e)}"
                        )

    def _learn_string_patterns(self, values: List[str], column_info: ColumnInfo) -> None:
        """Learn patterns from string values."""
        patterns = set()
        for value in values:
            pattern = self._get_string_pattern(value)
            patterns.add(pattern)
        column_info.value_patterns.extend(patterns)

    @staticmethod
    def _get_string_pattern(value: str) -> str:
        """Convert a string value to a pattern."""
        if value.isdigit():
            return "\\d+"
        elif value.isalpha():
            return "[A-Za-z]+"
        elif '@' in value and '.' in value:
            return "email"
        elif '-' in value or '/' in value:
            return "date-like"
        return "mixed"

    def learn_from_query(self, text_input: str, sql_query: str, success: bool) -> None:
        """Learn from successful and failed queries."""
        if success:
            # Store successful query pattern
            pattern_key = self._get_query_pattern(sql_query)
            if pattern_key not in self.common_queries:
                self.common_queries[pattern_key] = {}
            if sql_query not in self.common_queries[pattern_key]:
                self.common_queries[pattern_key][sql_query] = 0
            self.common_queries[pattern_key][sql_query] += 1
        else:
            # Store error pattern
            error_key = self._get_error_pattern(text_input)
            if error_key not in self.error_patterns:
                self.error_patterns[error_key] = []
            self.error_patterns[error_key].append(sql_query)

    def _get_query_pattern(self, sql_query: str) -> str:
        """Extract a pattern from a SQL query."""
        # TODO: Implement more sophisticated pattern extraction
        words = sql_query.lower().split()
        if "select" in words and "where" in words:
            return "select_where"
        elif "select" in words and "join" in words:
            return "select_join"
        return "other"

    def _get_error_pattern(self, text_input: str) -> str:
        """Extract a pattern from failed text input."""
        # TODO: Implement more sophisticated error pattern extraction
        words = text_input.lower().split()
        return " ".join(word for word in words if len(word) > 3)

    def save_learned_data(self, filepath: str) -> None:
        """Save learned data to a file."""
        data = {
            "tables": {k: v.__dict__ for k, v in self.tables.items()},
            "relationships": self.relationships,
            "common_queries": self.common_queries,
            "error_patterns": self.error_patterns
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def load_learned_data(self, filepath: str) -> None:
        """Load learned data from a file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Reconstruct objects from dict
        self.tables = {
            k: TableInfo(**v) for k, v in data["tables"].items()
        }
        self.relationships = data["relationships"]
        self.common_queries = data["common_queries"]
        self.error_patterns = data["error_patterns"]
