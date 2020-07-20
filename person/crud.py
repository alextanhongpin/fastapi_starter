from sqlalchemy.orm import Session
from uuid import UUID

from . import models, schemas


def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(name=person.name, description=person.description)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_person_by_name(db: Session, name: str):
    return db.query(models.Person).filter(models.Person.name == name).first()


def get_person(db: Session, id: UUID):
    return db.query(models.Person).filter(models.Person.id == id).first()


def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Person).offset(skip).limit(limit).all()
