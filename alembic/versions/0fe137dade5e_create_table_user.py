"""create-table-user

Revision ID: 0fe137dade5e
Revises: 836205e482c8
Create Date: 2020-07-20 16:39:57.046277

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0fe137dade5e'
down_revision = '836205e482c8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, unique=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('name', postgresql.TEXT, nullable=False),
        sa.Column('description', postgresql.TEXT)
    )


def downgrade():
    op.drop_table('person')
