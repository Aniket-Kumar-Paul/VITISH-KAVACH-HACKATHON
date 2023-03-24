import os


class Config:
    DB_URL = os.getenv("DB_URL") or "localhost"
    DB_PORT = os.getenv("DB_PORT") or "5432"
    DB_USER = os.getenv("DB_USER") or "postgres"
    DB_PASSWORD = os.getenv("DB_PASSWORD") or "password"
    DB_NAME = os.getenv("DB_NAME") or "kavach-server"
    ALLOWED_IMAGE_MIMETYPES = ["image/png"]
    ALLOWED_TAGS = ["person", "vehicle"]
    DEFAULT_PAGE_SIZE = 10
