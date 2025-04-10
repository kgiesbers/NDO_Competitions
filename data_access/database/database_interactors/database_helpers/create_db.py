from data_access.database.database_config import database_url
from sqlalchemy import create_engine
from data_access.schemas.base import Base


def create_database_framework():
    """Creates the tables of the database and their relations"""
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
