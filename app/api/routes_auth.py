from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_access_token

router = APIRouter()

class UserCredentials(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(credentials: UserCredentials):
    # Validate user credentials (this is just a placeholder)
    if credentials.username == "user" and credentials.password == "pass":
        token = create_access_token({"sub": credentials.username})
        return {"access_token": token}
    return {"error": "Invalid credentials"}