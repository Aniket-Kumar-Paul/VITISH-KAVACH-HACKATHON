mkdir -p app/static/images
mkdir -p app/static/frames
uvicorn app.main:app --port 8000 --reload