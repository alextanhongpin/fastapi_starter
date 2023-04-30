from uuid import UUID

from database.session import Session
from database.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, name: str, *, session: Session = None) -> User:
        """creates a new user"""
        session = session or self.session

        user = User(name=name)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get_user_by_name(self, name: str, *, session: Session = None) -> User | None:
        session = session or self.session

        return session.query(User).filter(User.name == name).first()

    def get_user(self, id: UUID, *, session: Session = None) -> User | None:
        session = session or self.session

        return session.query(User).filter(User.id == id).first()

    def get_users(
        self, *, skip: int = 0, limit: int = 10, session: Session = None
    ) -> list[User]:
        """returns the list of paginated users"""
        session = session or self.session

        return session.query(User).offset(skip).limit(limit).all()
