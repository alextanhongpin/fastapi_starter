import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{name}".format(
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT"),
    name=os.environ.get("DB_NAME"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def inject_session() -> Session:
    """
    Injects the session for FastAPI
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_session() -> Session:
    return SessionLocal()
