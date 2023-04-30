"""create_extensions

Revision ID: f1220107260e
Revises: 
Create Date: 2023-04-29 19:55:27.746221

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f1220107260e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION moddatetime;")


def downgrade() -> None:
    op.execute("DROP EXTENSION moddatetime;")
