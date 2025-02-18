"""CLI tool to extract database schema information."""
import click
import psycopg2
from psycopg2.extras import DictCursor
import json
from datetime import datetime
from pathlib import Path
import sys

def write_log(message):
    """Write message to log file and print to console."""
    with open('schema_extractor.log', 'a') as f:
        f.write(f"{message}\n")
    print(message)

def get_table_info(cur, schema, table):
    """Get table information including columns and constraints."""
    try:
        # Get column information
        cur.execute("""
            SELECT 
                column_name,
                data_type,
                character_maximum_length,
                column_default,
                is_nullable,
                numeric_precision,
                numeric_scale
            FROM information_schema.columns
            WHERE table_schema = %s 
            AND table_name = %s
            ORDER BY ordinal_position;
        """, (schema, table))
        
        columns = [dict(row) for row in cur.fetchall()]
        
        # Build CREATE TABLE statement
        create_stmt = [f"CREATE TABLE {schema}.{table} ("]
        column_defs = []
        
        for col in columns:
            col_def = f"    {col['column_name']} {col['data_type']}"
            
            # Add length for character types
            if col['character_maximum_length']:
                col_def += f"({col['character_maximum_length']})"
            
            # Add numeric precision and scale
            elif col['numeric_precision'] and col['data_type'] not in ('integer', 'bigint', 'smallint'):
                if col['numeric_scale']:
                    col_def += f"({col['numeric_precision']},{col['numeric_scale']})"
                else:
                    col_def += f"({col['numeric_precision']})"
            
            # Add nullable constraint
            if col['is_nullable'] == 'NO':
                col_def += " NOT NULL"
            
            # Add default value
            if col['column_default']:
                col_def += f" DEFAULT {col['column_default']}"
            
            column_defs.append(col_def)
        
        # Get primary key constraints
        cur.execute("""
            SELECT 
                tc.constraint_name,
                kcu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu 
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            WHERE tc.constraint_type = 'PRIMARY KEY'
            AND tc.table_schema = %s
            AND tc.table_name = %s
            ORDER BY kcu.ordinal_position;
        """, (schema, table))
        
        pks = [row['column_name'] for row in cur.fetchall()]
        if pks:
            column_defs.append(f"    PRIMARY KEY ({', '.join(pks)})")
        
        # Get foreign key constraints
        cur.execute("""
            SELECT
                kcu.column_name,
                ccu.table_schema AS foreign_table_schema,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name,
                rc.delete_rule,
                rc.update_rule
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage ccu
                ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
            JOIN information_schema.referential_constraints rc
                ON rc.constraint_name = tc.constraint_name
                AND rc.constraint_schema = tc.table_schema
            WHERE tc.constraint_type = 'FOREIGN KEY'
            AND tc.table_schema = %s
            AND tc.table_name = %s
            ORDER BY kcu.ordinal_position;
        """, (schema, table))
        
        fks = [dict(row) for row in cur.fetchall()]
        for fk in fks:
            fk_def = f"    FOREIGN KEY ({fk['column_name']}) REFERENCES {fk['foreign_table_schema']}.{fk['foreign_table_name']}({fk['foreign_column_name']})"
            if fk['delete_rule'] != 'NO ACTION':
                fk_def += f" ON DELETE {fk['delete_rule']}"
            if fk['update_rule'] != 'NO ACTION':
                fk_def += f" ON UPDATE {fk['update_rule']}"
            column_defs.append(fk_def)
        
        create_stmt.append(',\n'.join(column_defs))
        create_stmt.append(');')
        create_stmt = '\n'.join(create_stmt)
        
        # Get indexes
        cur.execute("""
            SELECT
                i.relname as index_name,
                a.attname as column_name,
                ix.indisunique as is_unique,
                ix.indisprimary as is_primary
            FROM pg_class t
            JOIN pg_index ix ON t.oid = ix.indrelid
            JOIN pg_class i ON i.oid = ix.indexrelid
            JOIN pg_attribute a ON a.attrelid = t.oid AND a.attnum = ANY(ix.indkey)
            JOIN pg_namespace n ON n.oid = t.relnamespace
            WHERE t.relkind = 'r'
            AND n.nspname = %s
            AND t.relname = %s;
        """, (schema, table))
        
        indexes = [dict(row) for row in cur.fetchall()]
        
        return {
            'create_statement': create_stmt,
            'columns': columns,
            'primary_keys': pks,
            'foreign_keys': fks,
            'indexes': indexes
        }
        
    except Exception as e:
        write_log(f"Error getting table info for {schema}.{table}: {str(e)}")
        raise

@click.command()
@click.option('--host', default='c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com', help='Database host')
@click.option('--port', default=5432, help='Database port')
@click.option('--dbname', default='d9ia9eei6rkq90', help='Database name')
@click.option('--user', default='uem4h7dfn2ghbi', help='Database user')
@click.option('--password', default='p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb', help='Database password')
@click.option('--schema', required=True, help='Schema to extract')
@click.option('--output-dir', default='schema_output', help='Output directory')
@click.option('--format', type=click.Choice(['json', 'sql']), default='json', help='Output format')
def extract(host, port, dbname, user, password, schema, output_dir, format):
    """Extract schema information to files."""
    # Clear log file
    with open('schema_extractor.log', 'w') as f:
        f.write('')
    
    write_log(f"Connecting to database {dbname} on {host}...")
    
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        write_log("Database connection successful!")
        
        with conn.cursor(cursor_factory=DictCursor) as cur:
            # Verify schema exists
            cur.execute("""
                SELECT schema_name 
                FROM information_schema.schemata 
                WHERE schema_name = %s
            """, (schema,))
            
            if not cur.fetchone():
                write_log(f"Error: Schema '{schema}' does not exist")
                sys.exit(1)
            
            # Get all tables in schema
            cur.execute("""
                SELECT tablename 
                FROM pg_catalog.pg_tables 
                WHERE schemaname = %s
                ORDER BY tablename
            """, (schema,))
            
            tables = [row[0] for row in cur.fetchall()]
            
            if not tables:
                write_log(f"Warning: No tables found in schema '{schema}'")
                sys.exit(0)
            
            write_log(f"Found {len(tables)} tables in schema '{schema}'")
            
            schema_info = {
                'schema': schema,
                'tables': {},
                'extraction_time': datetime.now().isoformat()
            }
            
            # Get detailed information for each table
            for table in tables:
                write_log(f"Processing table: {table}")
                schema_info['tables'][table] = get_table_info(cur, schema, table)
            
            # Create output directory
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Generate timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if format == 'json':
                # Save as JSON
                output_file = output_path / f"schema_{schema}_{timestamp}.json"
                with open(output_file, 'w') as f:
                    json.dump(schema_info, f, indent=2, default=str)
                write_log(f"Schema information saved to {output_file}")
                
            elif format == 'sql':
                # Save as SQL
                output_file = output_path / f"schema_{schema}_{timestamp}.sql"
                with open(output_file, 'w') as f:
                    f.write(f"-- Schema: {schema}\n")
                    f.write(f"-- Extracted: {schema_info['extraction_time']}\n\n")
                    
                    # Write schema creation
                    f.write(f"CREATE SCHEMA IF NOT EXISTS {schema};\n\n")
                    
                    for table, info in schema_info['tables'].items():
                        f.write(f"-- Table: {table}\n")
                        f.write(f"{info['create_statement']}\n\n")
                        
                        # Write index information
                        for idx in info['indexes']:
                            if not idx['is_primary']:  # Skip primary key indexes
                                unique = "UNIQUE " if idx['is_unique'] else ""
                                f.write(f"CREATE {unique}INDEX IF NOT EXISTS {idx['index_name']} ")
                                f.write(f"ON {schema}.{table} ({idx['column_name']});\n")
                        f.write("\n")
                
                write_log(f"Schema information saved to {output_file}")
        
    except Exception as e:
        write_log(f"Error: {str(e)}")
        sys.exit(1)
    finally:
        if 'conn' in locals():
            conn.close()
            write_log("Database connection closed")

if __name__ == '__main__':
    extract()
