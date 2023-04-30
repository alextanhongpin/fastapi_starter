# The recommended file by pytest to store fixture.
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from api.root import app
from database.migrate import run_migrations
from database.session import inject_session

# Global application scope, create Session class, engine.
Session = sessionmaker()

POSTGRES_VERSION = "postgres:15.1-alpine"


# We bind this to session level to ensure it is only
# initialized once.
@pytest.fixture(scope="session")
def db_engine():
    with PostgresContainer(POSTGRES_VERSION) as postgres:
        engine = create_engine(postgres.get_connection_url())

        # Run migrations.
        run_migrations(engine)

        yield engine


# For each function, we connect to the db_engine, create a
# new transaction, and roll back once the operation is
# done.
@pytest.fixture(scope="function")
def db(db_engine):
    # Connect to the database.
    connection = db_engine.connect()

    # Begin a non-ORM transaction.
    trans = connection.begin()

    # Bind an individual Session to the connectiona.
    session = Session(bind=connection)

    yield session

    session.close()
    # Rollback - everything that happened with the
    # Session above (including calls to commit()) is
    # rolled back.
    trans.rollback()
    connection.close()


@pytest.fixture(scope="function")
def api(db):
    app.dependency_overrides[inject_session] = lambda: db

    with TestClient(app) as c:
        yield c
