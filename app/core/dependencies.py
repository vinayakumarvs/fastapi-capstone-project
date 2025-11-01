from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_access_token

def api_key_header(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API key")
    return True

async def get_current_user(token: str = Header(...)):
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid JWT authentication credentials")
    return payload