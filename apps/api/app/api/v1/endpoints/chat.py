from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    query: str

class ChatResponse(BaseModel):
    answer: str

@router.post("/query", response_model=ChatResponse)
def query_chat(payload: ChatRequest):
    if not payload.query:
        raise HTTPException(status_code=400, detail="Query text cannot be empty")
    return {"answer": "RAG search is not set up yet"}
