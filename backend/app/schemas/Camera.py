from datetime import datetime

from pydantic import BaseModel

class Frame(BaseModel):
    id: int
    path: str
    latitude: float
    longitude: float
    timestamp: datetime

    class Config:
        orm_mode = True
