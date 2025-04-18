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

    def __repr__(self):
        return f"place='{str(self.place)}', number='{self.number}'"

    def to_dict(self):
        return {
            "id": self.id,
            "place": self.place,
            "number": self.number,
            "competitor_names": self.couple
        }
