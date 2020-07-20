"""create table person

Revision ID: dd41d2935bcc
Revises: 230622bbf343
Create Date: 2020-07-20 18:17:13.549210

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'dd41d2935bcc'
down_revision = '230622bbf343'
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
