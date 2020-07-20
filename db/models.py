from sqlalchemy import Column, String, text
from sqlalchemy.dialects import postgresql

from .database import Base

class Person(Base):
    __tablename__ = 'person'

    # as_uuid=True returns the id as UUID type in python.
    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, index=True, server_default=text('gen_random_uuid()'))
    name = Column(String)
    description = Column(String)
