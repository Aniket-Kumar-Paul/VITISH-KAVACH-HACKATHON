from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    meta_id = Column(String, unique=True, index=True)
    name = Column(String)
    tag = Column(String, nullable=False)
    images = relationship("Image", back_populates="owner")
    frames = relationship("Log", back_populates="entity")
    

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("entities.id"))
    owner = relationship("Entity", back_populates="images")
