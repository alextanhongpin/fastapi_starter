from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from database.session import Session, inject_session
from repository import user as user_repo

from .base.response import Response
from app.exceptions import NotFoundError

router = APIRouter(prefix="/users", tags=["users"])


class UserBase(BaseModel):
    id: UUID
    name: str


class User(UserBase):
    class Config:
        orm_mode = True


# We need to do this to avoid including the trailing slash, e.g.
# calling "$ curl localhost:8000/users/"
@router.get("", response_model=Response[list[User]])
def read_persons(
    skip: int = 0, limit: int = 10, session: Session = Depends(inject_session)
):
    users = user_repo.get_users(session, skip=skip, limit=limit)
    return Response(data=users)


@router.get("/{id}", response_model=Response[User])
def read_person(id: UUID, session: Session = Depends(inject_session)):
    user = user_repo.get_user(session, id)
    if user is None:
        raise NotFoundError(reason="user_not_found")

    return Response(data=user)
