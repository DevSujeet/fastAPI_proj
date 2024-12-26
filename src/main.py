from fastapi import FastAPI
from src.config.configs import _db_settings
from typing import Dict
import os
from src.routes import intro,user, record, location, project, analytics, userActivity
from src.middleware import add_process_time
# from fastapi_pagination import add_pagination
from contextlib import asynccontextmanager
from src.db import init_db

# os.environ["DEVELOPMENT_DATABASE_HOST"] = "test_os_host"
# os.environ["DEVELOPMENT_DATABASE_USERNAME"] = "test_os_user"
os.environ.pop('DEVELOPMENT_DATABASE_HOST', None) 
os.environ.pop('DEVELOPMENT_DATABASE_USERNAME', None) 


#life span event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("in life span")
    init_db()
    yield

def create_app(lifespan:lifespan) -> FastAPI:
    fastapi_app = FastAPI(title="telstra infa co",
                          description="Telstra document retrieval service",
                          version="0.0.1",
                          lifespan=lifespan
                          )
    # Middleware Settings
    fastapi_app.middleware("http")(add_process_time)
    # fastapi_app.middleware("http")(set_project_context)
    # fastapi_app.add_exception_handler(AgentException, agent_exception_handler)
    for router in get_fastapi_routers():
        fastapi_app.include_router(router)

    return fastapi_app

def get_fastapi_routers():
    return [
       analytics.router,
       intro.router,
       user.router,
       userActivity.router,
       record.router,
       location.router,
       project.router
    ]


app = create_app(lifespan=lifespan)
# add_pagination(app)
if __name__ == "__main__":
    uvicorn.run("main:app")




