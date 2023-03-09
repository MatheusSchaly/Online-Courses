"""create phone number for user col

Revision ID: 00265b5790f3
Revises: 
Create Date: 2023-03-08 10:30:00.846302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00265b5790f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "phone_number")
