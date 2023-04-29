"""create_table_users

Revision ID: 8793858eda6a
Revises: f1220107260e
Create Date: 2023-04-29 19:57:02.933088

"""
from alembic import op
import sqlalchemy as sa

# from sqlalchemy.dialects.postgresql import UUID, TEXT


# revision identifiers, used by Alembic.
revision = "8793858eda6a"
down_revision = "f1220107260e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """ 
        create table users (
            id uuid default gen_random_uuid(),
            name text not null,
            created_at timestamptz not null default current_timestamp,
            updated_at timestamptz not null default current_timestamp,
            primary key (id),
            unique(name)
        )
        """
    )
    op.execute(
        """
        create trigger moddatetime_users
            before update on users
            for each row
            execute procedure moddatetime(updated_at)
        """
    )
    # op.create_table(
    # "users",
    # sa.Column(
    # "id",
    # UUID(as_uuid=True),
    # primary_key=True,
    # unique=True,
    # server_default=sa.text("gen_random_uuid()"),
    # ),
    # sa.Column("email", TEXT, nullable=False),
    # )
    # pass


def downgrade() -> None:
    op.drop_table("users")
