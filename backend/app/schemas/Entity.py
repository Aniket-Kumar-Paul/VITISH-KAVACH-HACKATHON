from typing import Union

from pydantic import BaseModel

from app.schemas import Frame


class ImageBase(BaseModel):
    path: str
    description: Union[str, None] = None


class Image(ImageBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class EntityBase(BaseModel):
    name: str
    meta_id: str
    tag: str


class Log(BaseModel):
    id: int
    x1: float
    x2: float
    y1: float
    y2: float
    frame: Frame

    class Config:
        orm_mode = True


class Entity(EntityBase):
    id: int
    images: list[Image] = []
    frames: list[Log] = []

    class Config:
        orm_mode = True
