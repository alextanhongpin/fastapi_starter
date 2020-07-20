"""create-extension-pgcrypto

Revision ID: 836205e482c8
Revises: 2dd5e68872bd
Create Date: 2020-07-20 16:36:58.534839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836205e482c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute('CREATE EXTENSION IF NOT EXISTS pgcrypto')

def downgrade():
    conn = op.get_bind()
    conn.execute('DROP EXTENSION IF EXISTS pgcrypto')
