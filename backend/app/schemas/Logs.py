from pydantic import BaseModel

from app.schemas import Frame


class Log(BaseModel):
    id: int
    x1: float
    x2: float
    y1: float
    y2: float
    frame_id: Frame

    class Config:
        orm_mode = True
