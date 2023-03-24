from pydantic import BaseModel


class ErrorMessage(BaseModel):
    detail: str


class DeleteSchema(BaseModel):
    is_deleted: bool
