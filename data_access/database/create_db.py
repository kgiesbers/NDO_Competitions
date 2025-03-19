from data_access.database.config import database_url
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


def create_database_framework():
    # Database setup
    engine = create_engine(database_url, echo=False)
    Base = declarative_base()

    class Competition(Base):
        __tablename__ = "competitions"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, unique=True, nullable=False)
        url = Column(String, unique=True, nullable=False)
        brackets = relationship("Bracket", back_populates="competition")

    class Bracket(Base):
        __tablename__ = "brackets"
        id = Column(Integer, primary_key=True, autoincrement=True)
        competition_id = Column(Integer, ForeignKey("competitions.id"), nullable=False)
        name = Column(String, nullable=False)
        url = Column(String, unique=True, nullable=False)
        competition = relationship("Competition", back_populates="brackets")
        listings = relationship("Listing", back_populates="bracket")

    class Listing(Base):
        __tablename__ = "listings"
        id = Column(Integer, primary_key=True, autoincrement=True)
        bracket_id = Column(Integer, ForeignKey("brackets.id"), nullable=False)
        place = Column(Integer, nullable=False)
        number = Column(String, nullable=False)
        couple = Column(String, nullable=False)
        bracket = relationship("Bracket", back_populates="listings")

    Base.metadata.create_all(engine)
