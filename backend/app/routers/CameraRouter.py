import os
import uuid

from dateutil import parser
from fastapi import APIRouter, Form, HTTPException, Request, UploadFile

from app.config import Config
from app.schemas import DeleteSchema, ErrorMessage, Frame
from app.services import (create_frame, delete_frame_by_id, get_all_frames,
                          get_frame_by_data, get_frame_by_id)

router = APIRouter(
    prefix="/frame",
    tags=["frame"],
)


@router.get("/", response_model=list[Frame])
async def get_frames(
    page: int = 1, size: int = Config.DEFAULT_PAGE_SIZE, request: Request = None
):
    return get_all_frames(request, page, size)


@router.post("/", response_model=Frame, responses={400: {"model": ErrorMessage}})
async def post_entity(
    latitude: float = Form(...),
    longitude: float = Form(...),
    timestamp: str = Form(...),
    image: UploadFile = None,
    request: Request = None,
):
    if latitude < -90 or latitude > 90:
        raise HTTPException(status_code=400, detail="Latitude not in range")
    if longitude < -180 or longitude > 180:
        raise HTTPException(status_code=400, detail="Longitude not in range")
    tstamp = None
    try:
        tstamp = parser.parse(timestamp)
    except ValueError:
        raise HTTPException(status_code=400, detail="Timestamp not in correct format")
    if not image:
        raise HTTPException(status_code=400, detail="No image provided")
    if image.content_type not in Config.ALLOWED_IMAGE_MIMETYPES:
        raise HTTPException(
            status_code=400, detail=f"Image type not supported : {image.filename}"
        )
    rid = uuid.uuid4()
    pth = f"app/static/frames/{rid}.png"
    with open(pth, "wb") as buffer:
        buffer.write(image.file.read())
    frame_created = create_frame(
        request,
        {
            "path": pth,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": tstamp,
        },
    )
    return frame_created


@router.delete(
    "/{id}", response_model=DeleteSchema, responses={400: {"model": ErrorMessage}}
)
async def delete_entity(id: str, request: Request):
    frame_exists = get_frame_by_id(request, id)
    if not frame_exists:
        raise HTTPException(status_code=400, detail="Frame does not exist")
    os.remove(frame_exists.path)
    is_deleted = delete_frame_by_id(request, id)
    return {"is_deleted": is_deleted}


@router.get("/path", response_model=Frame, responses={400: {"model": ErrorMessage}})
async def get_frame_by_path(path: str, request: Request):
    frame = get_frame_by_data(request, {"path": path})
    if not frame:
        raise HTTPException(status_code=400, detail="Frame does not exist")
    return frame
