from fastapi import APIRouter
from fastapi.logger import logger
from src.schemas.project import Project
from typing import List

from src.services.project import all_Project, get_project_by_id, create_project_entry

router = APIRouter(
    prefix="/project",
    tags=["project"],
    responses={404: {"description": "project not in db"}}
)

@router.post('')
async def create_project_entry(project:Project) -> Project:
    print(f'create a project entry')
    project = create_project_entry(project=project)
    return project

@router.get('/all')
async def all_Project() -> List[Project]:
   return all_Project()

@router.get('')
async def get_project_by_id(id:str) -> Project:
    # return record for a given id
    return get_project_by_id(id=id)

