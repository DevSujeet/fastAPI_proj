# fastapi_proj

Experimenting with SQLModel, SQLAlchemy and working with them together
also exploring

1. sqlite
2. postgres
3. postgres on docker.

CURD
creation
delete
Pagination
filterng

## running this app.
    since venv is also part of the git..could be removed later
        source venv-telstra/bin/activate //activate env
        pip install -r requirement.txt
        uvicorn src.main:app --reload

    or
    ## Project setup
        using Uv as python package manager.
        $ uv venv
        $ source .venv/bin/activate
        $ uv pip install -r requirement.text 

# In case you face any issue:

    follow this step:-
    deactivate
    rm -rf venv-telstra
    python3 -m venv venv-telstra
    source venv-telstra/bin/activate
    pip install uvicorn fastapi
    uvicorn src.main:app

## TODO:-

    - Postgress integration
    - redis cache
    - Azure deployment
    - bulk upload/ download using AZURE

## Pip installs:

    Explanation of Each Package:

    fastapi:
        Core web framework for building APIs.
        Command: pip install fastapi

    uvicorn:
        ASGI server to run the FastAPI application.
        Command: pip install uvicorn

    pyjwt:
        JSON Web Token (JWT) implementation used to encode and decode JWT tokens.
        Command: pip install pyjwt

    lxml:
        Provides a high-performance XML parsing and manipulation library. Used here for parsing and extracting data from the SAML XML response.
        Command: pip install lxml

    python3-saml:
        SAML library for handling SAML responses, processing authentication, and managing attributes like roles. We are using OneLogin_Saml2_Auth to handle SAML logic.
        Command: pip install python3-saml

    xmlsec:
        A library used for XML signature validation, allowing you to verify the authenticity of the SAML response by checking the signature against the provided public certificate.
        Command: pip install xmlsec

    pip install pyyaml
