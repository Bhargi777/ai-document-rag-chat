from fastapi import APIRouter
from pydantic import BaseModel
from app.services.analytics_service import AnalyticsService

router = APIRouter()
analytics_service = AnalyticsService()

class AnalyticsResponse(BaseModel):
    event_type: str
    payload: str
    occurred_at: str

@router.get("/events", response_model=list[AnalyticsResponse])
def list_events():
    events = analytics_service.list_events()
    return [AnalyticsResponse(event_type=e.event_type, payload=e.payload, occurred_at=e.occurred_at.isoformat()) for e in events]
