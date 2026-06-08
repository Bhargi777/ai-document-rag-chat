from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class HistoryResponse(BaseModel):
    session_id: str
    messages: list[dict]

@router.get("/sessions/{session_id}/history", response_model=HistoryResponse)
def session_history(session_id: str):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")
    return {"session_id": session_id, "messages": []}
