from app.db.session import get_session
from app.db.models import User
from app.core.security import hash_password

class UserService:
    def __init__(self):
        self.session = get_session()

    def create_user(self, email: str, password: str) -> User:
        target = self.session.query(User).filter(User.email == email).first()
        if target:
            raise ValueError("User already exists")
        user = User(email=email, hashed_password=hash_password(password))
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter(User.email == email).first()
