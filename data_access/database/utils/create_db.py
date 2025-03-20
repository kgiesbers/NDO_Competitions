from data_access.database.config import database_url
from sqlalchemy import create_engine
from data_access.database_models.base import Base


def create_database_framework():
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
