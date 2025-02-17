# routes/protected.py

from fastapi import APIRouter, Depends, HTTPException
from src.auth_oauth.auth_config import AUTHORIZATION_URL, CLIENT_ID, REDIRECT_URI, SCOPE
from src.auth_oauth.auth_oauth import authenticate_user
from src.auth_oauth.jwt_utils import get_current_user, require_roles, create_jwt_token
from typing import List

from src.role_dependency import role_based_authorization_with_optional_permissions_oauth
from src.schemas.user import User

router = APIRouter(
    prefix="/auth",
    tags=["oauth_authentication"],
    responses={404: {"description": "user is not authorised."}}
)

@router.get("/login")
def login():
    """Generate the Azure OAuth 2.0 login URL."""
    auth_url = (
        f"{AUTHORIZATION_URL}?"
        f"client_id={CLIENT_ID}&"
        f"response_type=code&"
        f"redirect_uri={REDIRECT_URI}&"
        f"scope={SCOPE}"
    )
    return {"authorization_url": auth_url}


@router.get("/callback")
async def callback(code: str):
    """Handle the OAuth 2.0 callback and return a JWT token."""
    jwt_token = await authenticate_user(code)
    return {"access_token": jwt_token, "token_type": "bearer"}

#------------------------------------------------------------------------
@router.get("/get_current_user")
async def protected_route(user: dict = Depends(get_current_user)):
    """Example of a protected route."""
    return {"message": "Access granted", "user": user}

@router.get("/require_role_test")
async def admin_route(user: dict = Depends(require_roles(["Admin"]))):
    """Example of an admin-only route."""
    return {"message": "Welcome Admin", "user": user}

@router.post("/get_token")
async def get_token(user:User):
    jwt_data = {
        "username": user.user_name,
        "email": user.user_email,
        "roles": user.user_roles or ["Viewer"],  # Default role if roles are missing
    }
    return create_jwt_token(data=jwt_data) #,expires_delta=timedelta(minutes=30))

@router.get("/require_permission_test")
async def permission_route(user: dict = Depends(role_based_authorization_with_optional_permissions_oauth(["read_item"]))):
    """Example of an editor-only route."""
    return {"message": "Welcome Editor", "user": user}