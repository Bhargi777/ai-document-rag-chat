from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.schemas.user import UserCreate

router = APIRouter()

auth_service = AuthService()
user_service = UserService()

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/register", response_model=LoginResponse)
def register(payload: UserCreate):
    try:
        user = user_service.create_user(payload.email, payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

    token = auth_service.generate_token(user)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=LoginResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_service.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = auth_service.generate_token(user)
    return {"access_token": token, "token_type": "bearer"}
