from sqlalchemy.orm import Session
from . import models, schemas
from pydantic import BaseModel, Field

class test_user(BaseModel):
    email:str
    password:str

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user:schemas.RequestUser):
    fake_hashed_password = user.password
    db_user = models.User(email=user.email,password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

