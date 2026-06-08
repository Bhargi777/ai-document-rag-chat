from sqlmodel import create_engine, Session
from app.config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, echo=False)

def get_session() -> Session:
    return Session(engine)
