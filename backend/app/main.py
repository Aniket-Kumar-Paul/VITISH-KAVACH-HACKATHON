from dotenv import load_dotenv

load_dotenv(override=True)

from fastapi import FastAPI, Request, Response

from app.database import SessionLocal
from app.routers import CameraRouter, EntityRouter, LogsRouter

from . import models

models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
async def root():
    return {"message": "Kavach Server running"}


app.include_router(EntityRouter)
app.include_router(CameraRouter)
app.include_router(LogsRouter)