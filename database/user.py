from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base

gen_uuid = text("gen_random_uuid()")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(), primary_key=True, index=True, server_default=gen_uuid)
    name = Column(String, index=True)
    created_at = DateTime(timezone=True)
    updated_at = DateTime(timezone=True)
