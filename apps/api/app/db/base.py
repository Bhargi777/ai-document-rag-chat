from sqlmodel import SQLModel
from app.db.models import User, Document, DocumentChunk, ChatSession, ChatMessage

models = [User, Document, DocumentChunk, ChatSession, ChatMessage]

def create_db_tables(engine):
    SQLModel.metadata.create_all(engine)
