from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data_access.database_models.base import Base


class Competition(Base):
    __tablename__ = "competitions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String, unique=True, nullable=False)
    brackets = relationship("Bracket", back_populates="competition")