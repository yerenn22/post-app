from datetime import datetime

from sqlmodel import Field, SQLModel


class AbstractDatetime(SQLModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def update(self):
        self.updated_at = datetime.now()

    class Config:
        orm_mode = True
