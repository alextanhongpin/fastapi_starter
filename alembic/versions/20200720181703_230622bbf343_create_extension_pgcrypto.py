"""create extension pgcrypto

Revision ID: 230622bbf343
Revises:
Create Date: 2020-07-20 18:17:03.906782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '230622bbf343'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute('CREATE EXTENSION IF NOT EXISTS pgcrypto')

def downgrade():
    conn = op.get_bind()
    conn.execute('DROP EXTENSION IF EXISTS pgcrypto')
