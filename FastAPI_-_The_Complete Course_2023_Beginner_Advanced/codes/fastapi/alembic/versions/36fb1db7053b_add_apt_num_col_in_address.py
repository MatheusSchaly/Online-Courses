"""Add apt num col in ADDRESS

Revision ID: 36fb1db7053b
Revises: 5755551661de
Create Date: 2023-03-08 11:56:35.302767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36fb1db7053b'
down_revision = '5755551661de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
