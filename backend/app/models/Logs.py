from sqlalchemy import Column, Double, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    frame_id = Column(Integer, ForeignKey("frames.id"))
    entity_id = Column(Integer, ForeignKey("entities.id"))
    x1 = Column(Double, nullable=False)
    x2 = Column(Double, nullable=False)
    y1 = Column(Double, nullable=False)
    y2 = Column(Double, nullable=False)
    entity = relationship("Entity", back_populates="frames")
    frame = relationship("Frame", back_populates="logs")
