from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

SQLALCHEMY_DATABASE_URL = "postgres://{user}:{password}@{host}:{port}/{name}".format(user=os.environ.get("DB_USER"),
                                                                                     password=os.environ.get("DB_PASS"),
                                                                                     host=os.environ.get("DB_HOST"),
                                                                                     port=os.environ.get("DB_PORT"),
                                                                                     name=os.environ.get("DB_NAME"))

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
