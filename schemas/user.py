from sqlmodel import SQLModel
from typing import Optional

from models import UserBase
from utils.abstract import AbstractEntity


class UserCreate(UserBase):
    pass


class UserRead(UserBase, AbstractEntity):
    pass


class UserUpdate(SQLModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True
