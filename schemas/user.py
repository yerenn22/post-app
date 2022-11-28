from sqlmodel import SQLModel

from models import UserBase
from utils import AbstractEntity


class UserCreate(UserBase):
    pass


class UserRead(UserBase, AbstractEntity):
    pass


class UserUpdate(SQLModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
