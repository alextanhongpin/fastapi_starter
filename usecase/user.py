from typing import Protocol
from uuid import UUID
from app.exceptions import NotFoundError
from database.session import Session
from database.user import User

# Error codes.
USER_NOT_FOUND = "user_not_found"


class UserRepository(Protocol):
    def get_user(self, id: UUID, *, session: Session = None) -> User | None:
        pass

    def get_users(
        self, *, skip: int = 0, limit: int = 10, session: Session = None
    ) -> list[User]:
        pass


class UserUsecase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user(self, id: UUID, *, session: Session = None) -> User | None:
        user = self.repo.get_user(id)
        if user is None:
            raise NotFoundError(reason=USER_NOT_FOUND)
        return user

    def get_users(
        self, skip: int = 0, limit: int = 10, *, session: Session = None
    ) -> list[User]:
        return self.repo.get_users(skip=skip, limit=limit)
