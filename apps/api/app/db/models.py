from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    documents: List["Document"] = Relationship(back_populates="owner")
    chat_sessions: List["ChatSession"] = Relationship(back_populates="owner")

class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    title: str
    filename: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
    source: Optional[str] = None
    owner: Optional[User] = Relationship(back_populates="documents")
    chunks: List["DocumentChunk"] = Relationship(back_populates="document")

class DocumentChunk(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    document_id: int = Field(foreign_key="document.id")
    content: str
    metadata: Optional[str] = None
    document: Optional[Document] = Relationship(back_populates="chunks")

class ChatSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    title: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Optional[User] = Relationship(back_populates="chat_sessions")
    messages: List["ChatMessage"] = Relationship(back_populates="session")

class UsageMetric(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_type: str
    payload: str
    occurred_at: datetime = Field(default_factory=datetime.utcnow)

class ChatMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="chatsession.id")
    sender: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    session: Optional[ChatSession] = Relationship(back_populates="messages")
