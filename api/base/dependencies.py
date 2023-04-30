from database.session import SessionLocal, Session
from typing import Annotated
from fastapi import Depends
from usecase.user import UserUsecase
from repository.user import UserRepository


def inject_session() -> Session:
    """
    Injects the session for FastAPI
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


SessionDep = Annotated[Session, Depends(inject_session)]


def inject_user_usecase(session: SessionDep):
    repo = UserRepository(session)
    usecase = UserUsecase(repo)

    return usecase


UserUsecaseDep = Annotated[UserUsecase, Depends(inject_user_usecase)]
