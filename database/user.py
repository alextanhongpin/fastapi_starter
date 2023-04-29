from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(), primary_key=True, index=True, server_default=text("gen_random_uuid()")
    )
    name = Column(String, index=True)
    created_at = DateTime(timezone=True)
    updated_at = DateTime(timezone=True)
