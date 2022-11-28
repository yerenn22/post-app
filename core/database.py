from fastapi.logger import logger
from sqlmodel import Session, SQLModel, create_engine

from .settings import settings


engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.info(e)
