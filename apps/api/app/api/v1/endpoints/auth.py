from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.core.security import verify_password, create_access_token
from app.db.session import get_session
from app.db.models import User

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Login not implemented")
