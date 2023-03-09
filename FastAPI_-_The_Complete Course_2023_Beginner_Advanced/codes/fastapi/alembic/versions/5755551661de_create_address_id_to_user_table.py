"""Create address_id to USER table

Revision ID: 5755551661de
Revises: 1e1e62dcd00f
Create Date: 2023-03-08 10:53:55.893342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5755551661de'
down_revision = '1e1e62dcd00f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("address_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        "address_users_fk",
        source_table="users",
        referent_table="address",
        local_cols=["address_id"],
        remote_cols=["id"],
        ondelete="CASCADE"
    )

def downgrade() -> None:
    op.drop_constraint(
        "address_users_fk",
        table_name="users"
    )
    op.drop_column(
        "users",
        "address_id"
    )

