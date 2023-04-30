from uuid import UUID
from fastapi import APIRouter
from pydantic import BaseModel
from .base.dependencies import UserUsecaseDep
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
    usecase: UserUsecaseDep,
    skip: int = 0,
    limit: int = 10,
):
    users = usecase.get_users(skip=skip, limit=limit)
    return Response(data=users)


@router.get("/{id}", response_model=Response[User])
def read_person(
    id: UUID,
    # session: Session = Depends(inject_session),
    usecase: UserUsecaseDep,
):
    user = usecase.get_user(id)
    if user is None:
        raise NotFoundError(reason="user_not_found")

    return Response(data=user)
