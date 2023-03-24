from fastapi import HTTPException, Request

from app.models import Log


def log_entity_frame_association(
    request: Request,
    entity_id: int,
    frame_id: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> Log:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    association = Log(
        entity_id=entity_id, frame_id=frame_id, x1=xmin, x2=xmax, y1=ymin, y2=ymax
    )
    request.state.db.add(association)
    request.state.db.commit()
    request.state.db.refresh(association)
    return association


def get_association_by_data(request: Request, data: dict) -> Log:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    association = (
        request.state.db.query(Log).filter_by(**data).first()
    )
    return association
