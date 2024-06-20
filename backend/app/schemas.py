from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str = Field(..., example="john_doe")
    email: str = Field(..., example="john@example.com")

class UserCreate(UserBase):
    password: str = Field(..., example="strongpassword123")

class User(UserBase):
    id: int = Field(..., example=1)

    class Config:
       orm_mode=True