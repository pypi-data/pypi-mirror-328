"""Python 3.12 compatibility updates

Revision ID: 003
Revises: 002
Create Date: 2025-02-12 14:50:41.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
    """Apply Python 3.12 compatibility updates."""
    # Update column types for better type safety
    op.alter_column(
        "users",
        "preferences",
        type_=postgresql.JSONB(),
        postgresql_using="preferences::jsonb"
    )
    
    op.alter_column(
        "queries",
        "metadata",
        type_=postgresql.JSONB(),
        postgresql_using="metadata::jsonb"
    )
    
    op.alter_column(
        "query_results",
        "result_data",
        type_=postgresql.JSONB(),
        postgresql_using="result_data::jsonb"
    )
    
    op.alter_column(
        "datasets",
        "schema",
        type_=postgresql.JSONB(),
        postgresql_using="schema::jsonb"
    )
    
    op.alter_column(
        "datasets",
        "metadata",
        type_=postgresql.JSONB(),
        postgresql_using="metadata::jsonb"
    )
    
    op.alter_column(
        "data_tables",
        "schema",
        type_=postgresql.JSONB(),
        postgresql_using="schema::jsonb"
    )
    
    op.alter_column(
        "data_tables",
        "indexes",
        type_=postgresql.JSONB(),
        postgresql_using="indexes::jsonb"
    )
    
    op.alter_column(
        "data_tables",
        "constraints",
        type_=postgresql.JSONB(),
        postgresql_using="constraints::jsonb"
    )
    
    op.alter_column(
        "api_keys",
        "permissions",
        type_=postgresql.JSONB(),
        postgresql_using="permissions::jsonb"
    )
    
    op.alter_column(
        "audit_logs",
        "details",
        type_=postgresql.JSONB(),
        postgresql_using="details::jsonb"
    )
    
    op.alter_column(
        "agents",
        "configuration",
        type_=postgresql.JSONB(),
        postgresql_using="configuration::jsonb"
    )
    
    op.alter_column(
        "projects",
        "configuration",
        type_=postgresql.JSONB(),
        postgresql_using="configuration::jsonb"
    )
    
    op.alter_column(
        "teams",
        "configuration",
        type_=postgresql.JSONB(),
        postgresql_using="configuration::jsonb"
    )
    
    op.alter_column(
        "agent_actions",
        "input_data",
        type_=postgresql.JSONB(),
        postgresql_using="input_data::jsonb"
    )
    
    op.alter_column(
        "agent_actions",
        "output_data",
        type_=postgresql.JSONB(),
        postgresql_using="output_data::jsonb"
    )
    
    # Add check constraints for enum-like fields
    op.execute("""
        ALTER TABLE queries
        ADD CONSTRAINT check_query_status
        CHECK (status IN ('pending', 'running', 'completed', 'failed', 'cancelled'))
    """)
    
    op.execute("""
        ALTER TABLE datasets
        ADD CONSTRAINT check_dataset_format
        CHECK (format IN ('csv', 'json', 'parquet', 'avro', 'orc'))
    """)
    
    op.execute("""
        ALTER TABLE query_results
        ADD CONSTRAINT check_result_format
        CHECK (format IN ('json', 'csv', 'excel', 'html', 'markdown'))
    """)


def downgrade():
    """Revert Python 3.12 compatibility updates."""
    # Remove check constraints
    op.drop_constraint("check_query_status", "queries", type_="check")
    op.drop_constraint("check_dataset_format", "datasets", type_="check")
    op.drop_constraint("check_result_format", "query_results", type_="check")
    
    # Revert column types back to JSON
    op.alter_column(
        "users",
        "preferences",
        type_=postgresql.JSON(),
        postgresql_using="preferences::json"
    )
    
    op.alter_column(
        "queries",
        "metadata",
        type_=postgresql.JSON(),
        postgresql_using="metadata::json"
    )
    
    op.alter_column(
        "query_results",
        "result_data",
        type_=postgresql.JSON(),
        postgresql_using="result_data::json"
    )
    
    op.alter_column(
        "datasets",
        "schema",
        type_=postgresql.JSON(),
        postgresql_using="schema::json"
    )
    
    op.alter_column(
        "datasets",
        "metadata",
        type_=postgresql.JSON(),
        postgresql_using="metadata::json"
    )
    
    op.alter_column(
        "data_tables",
        "schema",
        type_=postgresql.JSON(),
        postgresql_using="schema::json"
    )
    
    op.alter_column(
        "data_tables",
        "indexes",
        type_=postgresql.JSON(),
        postgresql_using="indexes::json"
    )
    
    op.alter_column(
        "data_tables",
        "constraints",
        type_=postgresql.JSON(),
        postgresql_using="constraints::json"
    )
    
    op.alter_column(
        "api_keys",
        "permissions",
        type_=postgresql.JSON(),
        postgresql_using="permissions::json"
    )
    
    op.alter_column(
        "audit_logs",
        "details",
        type_=postgresql.JSON(),
        postgresql_using="details::json"
    )
    
    op.alter_column(
        "agents",
        "configuration",
        type_=postgresql.JSON(),
        postgresql_using="configuration::json"
    )
    
    op.alter_column(
        "projects",
        "configuration",
        type_=postgresql.JSON(),
        postgresql_using="configuration::json"
    )
    
    op.alter_column(
        "teams",
        "configuration",
        type_=postgresql.JSON(),
        postgresql_using="configuration::json"
    )
    
    op.alter_column(
        "agent_actions",
        "input_data",
        type_=postgresql.JSON(),
        postgresql_using="input_data::json"
    )
    
    op.alter_column(
        "agent_actions",
        "output_data",
        type_=postgresql.JSON(),
        postgresql_using="output_data::json"
    )
