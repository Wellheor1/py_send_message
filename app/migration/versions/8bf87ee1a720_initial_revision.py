"""Initial revision

Revision ID: 8bf87ee1a720
Revises:
Create Date: 2025-04-14 21:31:31.716892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8bf87ee1a720"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "slogs",
        sa.Column("log_type", sa.Enum("MAIL", name="logtype"), nullable=True),
        sa.Column("sender", sa.String(length=255), nullable=True),
        sa.Column("recipient", sa.String(length=255), nullable=True),
        sa.Column("status", sa.Boolean(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("slogs")
    # ### end Alembic commands ###
