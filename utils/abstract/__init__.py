from .abstract_datetime import AbstractDatetime
from .abstract_uuid import AbstractUUID


class AbstractEntity(AbstractUUID, AbstractDatetime):
    class Config:
        orm_mode = True
