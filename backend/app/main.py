from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
class test_user(BaseModel):
    username:str
    email:str
    password:str

@app.post("/users/")
def create_user(user:test_user, db: Session = Depends(get_db)):
    """
    Create a new user with the provided username, email, and password.
    
    - *username*: unique username for the user
    - *email*: unique email address for the user
    - *password*: strong password for the user
    """
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    print("Hello1")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by their ID.
    
    - *user_id*: ID of the user to retrieve
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    del db_user.password
    return db_user
