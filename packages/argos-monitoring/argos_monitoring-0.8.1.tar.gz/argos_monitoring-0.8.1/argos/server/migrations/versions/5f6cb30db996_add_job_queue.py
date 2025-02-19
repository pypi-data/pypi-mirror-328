"""Add job queue

Revision ID: 5f6cb30db996
Revises: bd4b4962696a
Create Date: 2025-02-17 16:56:36.673511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5f6cb30db996"
down_revision: Union[str, None] = "bd4b4962696a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("todo", sa.Enum("RELOAD_CONFIG", name="todo_enum"), nullable=False),
        sa.Column("args", sa.String(), nullable=False),
        sa.Column(
            "current", sa.Boolean(), server_default=sa.sql.false(), nullable=False
        ),
        sa.Column("added_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("jobs")
