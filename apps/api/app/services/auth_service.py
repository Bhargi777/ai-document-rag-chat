from app.db.session import get_session
from app.db.models import User
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self):
        self.session = get_session()

    def create_user(self, email: str, password: str) -> User:
        hashed = hash_password(password)
        user = User(email=email, hashed_password=hashed)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.session.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    def generate_token(self, user: User) -> str:
        return create_access_token(str(user.id))
