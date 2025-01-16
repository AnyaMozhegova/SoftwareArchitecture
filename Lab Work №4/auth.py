from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

auth_router = APIRouter()

# Pydantic models for authentication
class RegisterUser(BaseModel):
    username: str
    password: str
    isAdmin: bool = False

class LoginUser(BaseModel):
    username: str
    password: str

@auth_router.post("/api/v1/users/register")
def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, password=user.password, isAdmin=user.isAdmin)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user_id": new_user.id}

@auth_router.post("/api/v1/users/login")
def login_user(user: LoginUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username, User.password == user.password).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": db_user.id}
