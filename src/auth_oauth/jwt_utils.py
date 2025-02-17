# auth/jwt_utils.py
from typing import List
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, Security
from src.auth_oauth.auth_config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from typing import Union

def create_jwt_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """Create a JWT token with an expiration time."""
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt_token(token: str) -> dict:
    """Verify the JWT token and return the payload."""
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    expired_token_exception = HTTPException(
        status_code=401,
        detail="Token has expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode and validate the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Extract required fields from the payload
        username: str = payload.get("username")
        email: str = payload.get("email")
        roles: list = payload.get("roles")
        
        # Ensure all required claims are present
        if not username or not email or not roles:
            raise credentials_exception
        
        return {"username": username, "email": email, "roles": roles}
    
    except jwt.ExpiredSignatureError:
        # Handle expired token: Decode without verifying expiration to log user details
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_exp": False})
            username = payload.get("username")
            email = payload.get("email")
            roles = payload.get("roles")
            # Log details about the expired token
            if username and email:
                print(f"Expired token for user: {username} ({email}), roles: {roles}")
        except JWTError:
            raise credentials_exception  # Raise if decoding fails entirely
        # Token is expired but decoded successfully
        raise expired_token_exception
    
    except JWTError:
        # Generic error for any other JWT issues
        raise credentials_exception


# Define a security scheme for Bearer token
security = HTTPBearer()
def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    
    """Extract and verify JWT token from the Authorization header.
    {
        "message": "Access granted",
        "user": {
            "username": "user_test",
            "email": "user@example.com",
            "roles": [
            "admin"
            ],
            "exp": 1737476348
        }
    }
"""
    token = credentials.credentials  # Extract the token part
    try:
        payload = verify_jwt_token(token)  # Verify and decode the token
        return payload  # Return the payload (user details)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail="Invalid or expired token")



def require_roles(required_roles: List[str]):
    """Dependency for role-based access control."""
    async def role_checker(user: dict = Depends(get_current_user)):
        if not any(role in user["roles"] for role in required_roles):
            raise HTTPException(status_code=403, detail="Permission denied")
        return user
    return role_checker

'''
Advantages of python-jose over jwt (PyJWT)

    Broader Cryptographic Support:
        python-jose supports a wide range of cryptographic algorithms beyond HS256 and RS256, including ECDSA and RSA-PSS.
        Example algorithms in python-jose:
            ES256, PS256, RS256, HS256, etc.
        PyJWT primarily focuses on standard JWT algorithms like HS256 and RS256.

    More Secure Defaults:
        python-jose enforces stricter checks by default, such as requiring algorithm verification, making it harder to misconfigure.

    Ease of Handling Public Key Verification:
        With python-jose, verifying tokens with public keys (like Azure's JWKS) is straightforward, using constructs like jwk.construct.

    Library Maturity for Asymmetric Signing:
        If you use RSA or EC keys for signing and verifying JWTs, python-jose provides a more mature and robust implementation.

When to Use PyJWT

    Lightweight Applications:
        If your use case only requires symmetric signing (HS256) or basic RSA signing (RS256), PyJWT is simpler and faster.
    Small Learning Curve:
        PyJWT has a smaller API surface and simpler usage, making it beginner-friendly.

For working with Azure Entra ID or other OAuth providers,
I recommend python-jose because of its strong public key handling and security features.
 If you're implementing simpler authentication workflows, PyJWT might suffice.
'''