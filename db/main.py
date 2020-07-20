from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    print(person)
    db_person = crud.get_person_by_name(db, person.name)
    if db_person:
        return HTTPException(status_code=400, detail='Email already registered')
    return crud.create_person(db, person)

@app.get('/{user_id}', response_model=schemas.Person)
def read_person(user_id: UUID, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, id=user_id)
    if db_person is None:
        return HTTPException(status_code=404, detail='User not found')
    return db_person

@app.get('/', response_model=List[schemas.Person])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_persons(db, skip=skip, limit=limit)
