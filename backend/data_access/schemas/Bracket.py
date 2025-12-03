from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.data_access.schemas.base import Base


class Bracket(Base):
    __tablename__ = "brackets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    competition_id = Column(Integer, ForeignKey("competitions.id"), nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    competition = relationship("Competition", back_populates="brackets")
    listings = relationship("Listing", back_populates="bracket")

    def __repr__(self):
        return f"place='{str(self.name)}', number='{self.url}'"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
        }
