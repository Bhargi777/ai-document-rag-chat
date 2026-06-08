from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.summary_service import SummaryService

router = APIRouter()
summary_service = SummaryService()

class SummaryRequest(BaseModel):
    content: str

class SummaryResponse(BaseModel):
    summary: str

@router.post("/document", response_model=SummaryResponse)
def summarize_document(payload: SummaryRequest):
    if not payload.content:
        raise HTTPException(status_code=400, detail="Content is required")
    summary = summary_service.summarize(payload.content)
    return {"summary": summary}
