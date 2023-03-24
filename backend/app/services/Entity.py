from fastapi import HTTPException, Request

from app.models import Entity, Image


def get_all_entities(request: Request) -> list[Entity]:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    return request.state.db.query(Entity).all()


def get_entity_by_data(request: Request, data: dict) -> Entity:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    return request.state.db.query(Entity).filter_by(**data).first()


def create_entity(request: Request, data: dict) -> Entity:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    entity = Entity(**data)
    request.state.db.add(entity)
    request.state.db.commit()
    request.state.db.refresh(entity)
    return entity


def delete_entity_by_meta_id(request: Request, meta_id: str) -> bool:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    entity = get_entity_by_data(request, {"meta_id": meta_id})
    if not entity:
        return False
    request.state.db.delete(entity)
    request.state.db.commit()
    return True


def create_image_for_entity(request: Request, path: str, meta_id: str) -> bool:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    entity = get_entity_by_data(request, {"meta_id": meta_id})
    if not entity:
        return False
    image = Image(path=path, owner_id=entity.id)
    request.state.db.add(image)
    request.state.db.commit()
    return True


def delete_images_for_entity(request: Request, meta_id: str) -> bool:
    if not request.state.db:
        raise HTTPException(status_code=500, detail="No database connection")
    entity = get_entity_by_data(request, {"meta_id": meta_id})
    if not entity:
        return False
    for image in entity.images:
        request.state.db.delete(image)
    request.state.db.commit()
    return True
