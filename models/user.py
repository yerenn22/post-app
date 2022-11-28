from sqlmodel import SQLModel

from utils import AbstractEntity


class UserBase(SQLModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class User(AbstractEntity, UserBase, table=True):
    pass
