from pydantic import BaseModel, Field



class RequestUser(BaseModel):
    email:str
    password:str

class UserBase(BaseModel):
    email: str = Field(..., example="john@example.com",unique=True, index=True)

class UserCreate(UserBase):
    password: str = Field(..., example="strongpassword123")

class User(UserBase):
    id: int = Field(..., example=1)

    class Config:
       from_attributes=True