from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)


@app.post("/users/")
def create_user(user:schemas.RequestUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    print("Hello1")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    del db_user.password
    return db_user


@app.post("/users/login/")
def login_user(user: schemas.RequestUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    print(db_user)
    
    if db_user and db_user.password == user.password:
        return {"authenticated": True}
    
    raise HTTPException(status_code=401, detail="Unauthenticated")