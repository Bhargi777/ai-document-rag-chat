from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag_service import RagService

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    query: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []

rag_service = RagService()

@router.post("/query", response_model=ChatResponse)
def query_chat(payload: ChatRequest):
    if not payload.query:
        raise HTTPException(status_code=400, detail="Query text cannot be empty")

    results = rag_service.query(payload.query)
    answer = "".join([doc.page_content for doc in results[:3]]) if results else "No relevant documents found."
    sources = []
    for doc in results:
        if isinstance(doc.metadata, dict):
            sources.append(doc.metadata.get("source", "unknown"))
        else:
            sources.append(str(doc.metadata or "unknown"))
    return {"answer": answer, "sources": sources}
