# auth_oauth/auth_oauth.py

import httpx
from fastapi import HTTPException
from src.auth_oauth.jwt_utils import create_jwt_token
from src.auth_oauth.auth_config import TOKEN_URL, USER_INFO_URL, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

async def exchange_code_for_token(code: str) -> dict:
    """Exchange authorization code for an access token."""
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(TOKEN_URL, data=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to exchange code for token")
        return response.json()


async def fetch_user_details(access_token: str) -> dict:
    """Fetch user details using the access token."""
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {access_token}"}
        response = await client.get(USER_INFO_URL, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch user details")
        return response.json()


async def authenticate_user(code: str) -> str:
    """Authenticate the user using the authorization code and return a JWT token."""
    tokens = await exchange_code_for_token(code)
    access_token = tokens.get("access_token")

    # Fetch user details from Azure
    user_info = await fetch_user_details(access_token)

    # Create a JWT token with user details
    jwt_data = {
        "username": user_info.get("displayName"),
        "email": user_info.get("mail") or user_info.get("userPrincipalName"),
        "roles": user_info.get("roles", ["Viewer"]),  # Default role if roles are missing
    }
    return create_jwt_token(jwt_data)
