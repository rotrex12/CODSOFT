from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
