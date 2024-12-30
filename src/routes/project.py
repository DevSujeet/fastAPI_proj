from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.dependencies import get_user_id_header
from src.schemas.project import Project
from typing import List

from src.services.project import all_Project, get_project_by_id, create_project_entry

router = APIRouter(
    prefix="/project",
    tags=["project"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

@router.post('')
async def create_project_entry(project:Project, user_id=Depends(get_user_id_header)) -> Project:
    print(f'create a project entry')
    project = create_project_entry(project=project)
    return project

@router.get('/all')
async def all_Project(user_id=Depends(get_user_id_header)) -> List[Project]:
   return all_Project()

@router.get('')
async def get_project_by_id(id:str, user_id=Depends(get_user_id_header)) -> Project:
    # return record for a given id
    return get_project_by_id(user_id=user_id, id=id)

