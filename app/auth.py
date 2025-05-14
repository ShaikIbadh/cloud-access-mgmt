# auth.py – API key-based authentication and RBAC
from fastapi import Depends, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from .db import db

API_KEY_NAME = "X-API-KEY"
# Define X-API-KEY header for FastAPI Security
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_current_user(api_key: str = Security(api_key_header)):
    if not api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API key missing")
    user = await db["users"].find_one({"api_key": api_key})
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
    return user

async def require_admin(current_user = Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return current_user

async def require_customer(current_user = Depends(get_current_user)):
    if current_user.get("role") != "customer":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Customer privileges required")
    return current_user
