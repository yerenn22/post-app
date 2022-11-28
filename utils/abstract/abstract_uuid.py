from uuid import uuid4

from sqlmodel import Field, SQLModel


def generate_uuid():
    return str(uuid4())


class AbstractUUID(SQLModel):
    id: str = Field(default_factory=generate_uuid, primary_key=True)

    class Config:
        orm_mode = True
