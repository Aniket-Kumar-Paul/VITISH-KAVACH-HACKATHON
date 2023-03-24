import os
import shutil
import uuid

from fastapi import APIRouter, Form, HTTPException, Request, UploadFile

from app.config import Config
from app.schemas import DeleteSchema, Entity, ErrorMessage
from app.services import (create_entity, create_image_for_entity,
                          delete_entity_by_meta_id, delete_images_for_entity,
                          get_all_entities, get_entity_by_data)

router = APIRouter(
    prefix="/entity",
    tags=["entity"],
)


@router.get("/", response_model=list[Entity])
async def get_entities(request: Request):
    return get_all_entities(request)


@router.post("/", response_model=Entity, responses={400: {"model": ErrorMessage}})
async def post_entity(
    name: str = Form(...),
    meta_id: str = Form(...),
    tag: str = Form(...),
    images: list[UploadFile] = [],
    request: Request = None,
):
    entity_exists = get_entity_by_data(request, {"meta_id": meta_id})
    if entity_exists:
        raise HTTPException(status_code=400, detail="Entity already exists")
    if tag not in Config.ALLOWED_TAGS:
        raise HTTPException(status_code=400, detail=f"Tag not supported : {tag}")
    for image in images:
        if image.content_type not in Config.ALLOWED_IMAGE_MIMETYPES:
            raise HTTPException(
                status_code=400, detail=f"Image type not supported : {image.filename}"
            )
    entity_created = create_entity(
        request, {"name": name, "meta_id": meta_id, "tag": tag}
    )
    for image in images:
        rid = uuid.uuid4()
        pth = f"app/static/images/{meta_id}"
        if not os.path.exists(pth):
            os.makedirs(pth)
        pth = f"{pth}/{rid}.png"
        with open(pth, "wb") as buffer:
            buffer.write(image.file.read())
        create_image_for_entity(request, pth, meta_id)
    return entity_created


@router.delete(
    "/{meta_id}", response_model=DeleteSchema, responses={400: {"model": ErrorMessage}}
)
async def delete_entity(meta_id: str, request: Request):
    entity_exists = get_entity_by_data(request, {"meta_id": meta_id})
    if not entity_exists:
        raise HTTPException(status_code=400, detail="Entity does not exist")
    delete_images_for_entity(request, meta_id)
    pth = f"app/static/images/{meta_id}"
    shutil.rmtree(pth)
    is_deleted = delete_entity_by_meta_id(request, meta_id)
    return {"is_deleted": is_deleted}


@router.get(
    "/meta/{meta_id}", response_model=Entity, responses={400: {"model": ErrorMessage}}
)
async def get_entity_from_meta_id(meta_id: str, request: Request):
    entity_exists = get_entity_by_data(request, {"meta_id": meta_id})
    if not entity_exists:
        raise HTTPException(status_code=400, detail="Entity does not exist")
    return entity_exists
