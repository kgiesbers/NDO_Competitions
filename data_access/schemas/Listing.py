from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data_access.schemas.base import Base


class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bracket_id = Column(Integer, ForeignKey("brackets.id"), nullable=False)
    place = Column(Integer, nullable=False)
    number = Column(String, nullable=False)
    couple = Column(String, nullable=False)
    bracket = relationship("Bracket", back_populates="listings")