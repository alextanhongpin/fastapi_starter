import repository.user as repo
from database.session import Session


def test_user_crud(db: Session):
    john = repo.create_user(db, "John")
    assert john.id is not None

    user = repo.get_user_by_name(db, john.name)
    assert john.id == user.id

    user = repo.get_user(db, john.id)
    assert john.id == user.id
