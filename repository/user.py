from database.user import User
from sqlalchemy.orm import Session
from uuid import UUID


def create_user(session: Session, name: str) -> User:
    user = User(name=name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_name(session: Session, name: str) -> User:
    return session.query(User).filter(User.name == name).first()


def get_user(session: Session, id: UUID) -> User:
    return session.query(User).filter(User.id == id).first()


def get_users(session: Session, skip: int = 0, limit: int = 10):
    return session.query(User).offset(skip).limit(limit).all()
