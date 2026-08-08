from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.base import create_db_tables
from app.db.session import engine

app = FastAPI(title="AI Document RAG Chat API", version="0.1.0")

app.include_router(api_router, prefix="/api/v1")

create_db_tables(engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}
