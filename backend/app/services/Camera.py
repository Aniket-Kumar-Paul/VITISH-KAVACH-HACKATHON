from fastapi import HTTPException, Request

from app.models import Frame


def get_all_frames(request: Request, page : int, size : int) -> list[Frame]:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    return request.state.db.query(Frame).limit(size).offset((page - 1) * size).all()


def get_frame_by_id(request: Request, id: int) -> Frame:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    return request.state.db.query(Frame).filter_by(id=id).first()


def create_frame(request: Request, data: dict) -> Frame:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    frame = Frame(**data)
    request.state.db.add(frame)
    request.state.db.commit()
    request.state.db.refresh(frame)
    return frame


def delete_frame_by_id(request: Request, id: int) -> bool:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    frame = request.state.db.query(Frame).filter_by(id=id).first()
    if not frame:
        return False
    request.state.db.delete(frame)
    request.state.db.commit()
    return True

def get_frame_by_data(request: Request, data: dict) -> Frame:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    return request.state.db.query(Frame).filter_by(**data).first()