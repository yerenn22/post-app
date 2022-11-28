from sqlmodel import Field, SQLModel

from utils.abstract import AbstractEntity


class PostBase(SQLModel):
    title: str
    content: str
    is_published: bool

    author_id: str = Field(foreign_key="user.id")


class Post(AbstractEntity, PostBase, table=True):
    pass
