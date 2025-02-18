"""Initial migration.

Revision ID: 001
Revises: 
Create Date: 2024-02-12 15:53:09.000000

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create initial tables."""
    # Create users table
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.String(36),
            primary_key=True,
            server_default=sa.text("hex(randomblob(16))"),
            nullable=False,
        ),
        sa.Column("username", sa.String(50), unique=True, nullable=False),
        sa.Column("email", sa.String(120), unique=True, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            server_onupdate=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
    )

    # Create api_keys table
    op.create_table(
        "api_keys",
        sa.Column(
            "id",
            sa.String(36),
            primary_key=True,
            server_default=sa.text("hex(randomblob(16))"),
            nullable=False,
        ),
        sa.Column("key", sa.String(64), unique=True, nullable=False),
        sa.Column("description", sa.String(200)),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("expires_at", sa.DateTime()),
        sa.Column("revoked_at", sa.DateTime()),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            server_onupdate=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Remove all tables."""
    op.drop_table("api_keys")
    op.drop_table("users")
