from fastapi import APIRouter, HTTPException, Request

from app.schemas import ErrorMessage
from app.services import (get_association_by_data, get_entity_by_data,
                          get_frame_by_data, log_entity_frame_association)

router = APIRouter(
    prefix="/log",
    tags=["log"],
)


@router.post("/", responses={400: {"model": ErrorMessage}})
async def post_frame_entity_log(
    entity_id: int,
    frame_id: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    request: Request,
):
    entity_exists = get_entity_by_data(request, {"id": entity_id})
    if not entity_exists:
        raise HTTPException(status_code=400, detail="Entity does not exist")
    frame_exists = get_frame_by_data(request, {"id": frame_id})
    if not frame_exists:
        raise HTTPException(status_code=400, detail="Frame does not exist")
    association_exists = get_association_by_data(
        request, {"entity_id": entity_id, "frame_id": frame_id}
    )
    if association_exists:
        raise HTTPException(status_code=400, detail="Association already exists")
    if xmin > xmax:
        raise HTTPException(status_code=400, detail="xmin > xmax")
    if ymin > ymax:
        raise HTTPException(status_code=400, detail="ymin > ymax")
    if xmin < 0 or xmax < 0 or ymin < 0 or ymax < 0:
        raise HTTPException(status_code=400, detail="Coordinates must be positive")
    if xmin > 1 or xmax > 1 or ymin > 1 or ymax > 1:
        raise HTTPException(
            status_code=400, detail="Coordinates must be between 0 and 1"
        )
    association = log_entity_frame_association(
        request, entity_id, frame_id, xmin, xmax, ymin, ymax
    )
    return association
