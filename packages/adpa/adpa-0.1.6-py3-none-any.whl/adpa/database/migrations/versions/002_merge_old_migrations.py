"""Merge old migrations

Revision ID: 002
Revises: 001
Create Date: 2025-02-09 15:02:27.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None

def upgrade():
    """Merge changes from old migrations."""
    # Create agents table
    op.create_table(
        "agents",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("type", sa.String(50), nullable=False),
        sa.Column("configuration", postgresql.JSON(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("project_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False)
    )
    
    # Create projects table
    op.create_table(
        "projects",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("description", sa.Text()),
        sa.Column("configuration", postgresql.JSON(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False)
    )
    
    # Create teams table
    op.create_table(
        "teams",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("description", sa.Text()),
        sa.Column("configuration", postgresql.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False)
    )
    
    # Create team_assignments table
    op.create_table(
        "team_assignments",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("team_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("agent_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("role", sa.String(50), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"]),
        sa.ForeignKeyConstraint(["agent_id"], ["agents.id"])
    )
    
    # Create agent_actions table
    op.create_table(
        "agent_actions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("agent_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("action_type", sa.String(50), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("input_data", postgresql.JSON(), nullable=False),
        sa.Column("output_data", postgresql.JSON()),
        sa.Column("error_message", sa.Text()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["agent_id"], ["agents.id"])
    )
    
    # Add foreign key constraint for project_id in agents table
    op.create_foreign_key(
        "fk_agents_project_id",
        "agents",
        "projects",
        ["project_id"],
        ["id"]
    )
    
    # Update agent types to include new types
    op.execute("""
        ALTER TABLE agents
        ADD CONSTRAINT check_agent_type
        CHECK (type IN (
            'researcher',
            'planner',
            'executor',
            'reviewer',
            'coordinator',
            'specialist'
        ))
    """)

def downgrade():
    """Revert merged migrations."""
    # Drop constraints first
    op.drop_constraint("check_agent_type", "agents", type_="check")
    op.drop_constraint("fk_agents_project_id", "agents", type_="foreignkey")
    
    # Drop tables in reverse order
    op.drop_table("agent_actions")
    op.drop_table("team_assignments")
    op.drop_table("teams")
    op.drop_table("projects")
    op.drop_table("agents")
