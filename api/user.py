from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database.session import inject_session, Session
from repository import user as user_repo
from uuid import UUID
from .response.response import Response


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
    return Response(data=user)
