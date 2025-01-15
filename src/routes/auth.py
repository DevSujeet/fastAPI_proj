from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.auth.auth import create_access_token, extract_user_details_from_saml, get_current_user, validate_saml_response_with_signature
from src.config.log_config import logger
from src.dependencies import get_user_id_header


router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

# Endpoint to receive the SAML response from the frontend and generate JWT
@router.post("/saml/response")
async def saml_response(saml_response: str, validate_signature: bool = True):
    """
    Endpoint to receive the SAML response from the frontend after the user has authenticated via IDP.
    If validate_signature is True, the signature will be validated using the public certificate.
    """
    # Choose whether to validate signature or just extract user details
    if validate_signature:
        # Validate the SAML response and extract user information using signature verification
        user_info = validate_saml_response_with_signature(saml_response)
    else:
        # Directly extract user details from the SAML response (without signature verification)
        user_info = extract_user_details_from_saml(saml_response)

    # Create a JWT token with user information
    access_token_expires = timedelta(minutes=30)  # Token expiration time
    access_token = create_access_token(
        data={"sub": user_info["username"], "roles": user_info["roles"]},
        expires_delta=access_token_expires,
    )

    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"})

# Example protected route requiring a valid JWT token
@router.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    # Check if user has 'user' role
    if "user" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return {"message": "Access granted", "user": current_user}

# Admin route requiring 'admin' role
@router.get("/admin")
async def admin_route(current_user: dict = Depends(get_current_user)):
    # Check if user has 'admin' role
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return {"message": "Admin access granted", "user": current_user}

# Logout route (optional, for demonstration purposes)
@router.get("/logout")
async def logout():
    # logout user session if maintained
    return {"message": "Logged out successfully"}