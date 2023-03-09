"""Create addess table

Revision ID: 1e1e62dcd00f
Revises: 00265b5790f3
Create Date: 2023-03-08 10:40:42.507311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e1e62dcd00f'
down_revision = '00265b5790f3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("address1", sa.String(), nullable=False),
        sa.Column("address2", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("postalcode", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("address")
