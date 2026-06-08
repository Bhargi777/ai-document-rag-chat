from datetime import datetime
from app.db.session import get_session
from app.db.models import UsageMetric

class AnalyticsService:
    def __init__(self):
        self.session = get_session()

    def record_event(self, event_type: str, payload: dict[str, str]) -> UsageMetric:
        metric = UsageMetric(event_type=event_type, payload=payload)
        self.session.add(metric)
        self.session.commit()
        self.session.refresh(metric)
        return metric

    def list_events(self, limit: int = 50):
        return self.session.query(UsageMetric).order_by(UsageMetric.occurred_at.desc()).limit(limit).all()
