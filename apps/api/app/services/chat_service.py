from app.db.session import get_session
from app.db.models import ChatSession, ChatMessage

class ChatService:
    def __init__(self):
        self.session = get_session()

    def create_session(self, owner_id: int, title: str) -> ChatSession:
        session = ChatSession(owner_id=owner_id, title=title)
        self.session.add(session)
        self.session.commit()
        self.session.refresh(session)
        return session

    def add_message(self, session_id: int, sender: str, content: str) -> ChatMessage:
        message = ChatMessage(session_id=session_id, sender=sender, content=content)
        self.session.add(message)
        self.session.commit()
        self.session.refresh(message)
        return message

    def get_messages(self, session_id: int):
        return self.session.query(ChatMessage).filter(ChatMessage.session_id == session_id).all()
