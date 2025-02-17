import os
from dotenv import load_dotenv
from src.config.configs import OAUTH_Settings, JWT_Settings
# Load environment variables from .env (for local development)
# load_dotenv()

auth_settings = OAUTH_Settings()
jwt_settings = JWT_Settings()

# OAuth 2.0 Configurations
TENANT_ID = auth_settings.tenant_id
CLIENT_ID = auth_settings.client_id
CLIENT_SECRET = auth_settings.client_secret
REDIRECT_URI = auth_settings.redirect_uri
SCOPE = auth_settings.scope

AUTHORIZATION_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
USER_INFO_URL = "https://graph.microsoft.com/v1.0/me"
ISSUER = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0"

# JWT Configurations
SECRET_KEY = jwt_settings.secret_key  # Use a strong, unique secret in production
ALGORITHM = jwt_settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = jwt_settings.access_token_expire_minutes

# Validate critical configurations
required_env_vars = [TENANT_ID, CLIENT_ID, CLIENT_SECRET, SECRET_KEY]
if not all(required_env_vars):
    raise RuntimeError("Missing required environment variables. Check your configuration.")
