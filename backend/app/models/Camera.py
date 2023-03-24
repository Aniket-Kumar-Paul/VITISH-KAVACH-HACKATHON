from sqlalchemy import Column, DateTime, Double, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Frame(Base):
    __tablename__ = "frames"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String)
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    logs = relationship("Log", back_populates="frame")
