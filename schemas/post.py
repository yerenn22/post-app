from sqlmodel import SQLModel
from typing import Optional

from models import PostBase
from utils.abstract import AbstractEntity


class PostCreate(PostBase):
    pass


class PostRead(AbstractEntity, PostBase):
    pass


class PostUpdate(SQLModel):
    title: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True
