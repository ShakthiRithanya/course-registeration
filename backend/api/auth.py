from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from db.database import engine
from models.schema import User
from core.security import verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter()

class LoginData(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    user_id: str
    name: str

@router.post("/login", response_model=Token)
def login(data: LoginData):
    with Session(engine) as session:
        statement = select(User).where(User.email == data.email)
        user = session.exec(statement).first()
        
        if not user or not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token = create_access_token(
            data={"sub": user.id, "role": user.role}
        )
        return {
            "access_token": access_token, 
            "token_type": "bearer", 
            "role": user.role,
            "user_id": user.id,
            "name": user.name
        }
