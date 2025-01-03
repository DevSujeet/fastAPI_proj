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

    source venv-telstra/bin/activate //activate env
    pip install -r requirement.txt
    uvicorn src.main:app --reload

# In case you face any issue:

    follow this step:-
    deactivate
    rm -rf venv-telstra
    python3 -m venv venv-telstra
    source venv-telstra/bin/activate
    pip install uvicorn fastapi
    uvicorn src.main:app
