from fastapi import APIRouter, FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
import jwt

router = APIRouter(
    prefix="/test",
    tags=["test auth header"],
)

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Security scheme for Authorization header
api_key_header = APIKeyHeader(name="Authorization", auto_error=True)
def get_current_user(api_key: str = Security(api_key_header)):
    # Validate JWT token
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(api_key.split("Bearer ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        roles = payload.get("roles")
        if username is None or roles is None:
            raise credentials_exception
        return {"username": username, "roles": roles}
    except Exception:
        raise credentials_exception

@router.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    if "user" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return {"message": "Access granted", "user": current_user}