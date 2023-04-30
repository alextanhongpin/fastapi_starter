import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

dsn = "postgresql://{user}:{password}@{host}:{port}/{name}"

SQLALCHEMY_DATABASE_URL = dsn.format(
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT"),
    name=os.environ.get("DB_NAME"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
