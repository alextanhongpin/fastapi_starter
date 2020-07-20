from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID


class PersonBase(BaseModel):
    name: str
    description: str


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: UUID

    class Config:
        orm_mode = True
