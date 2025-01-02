from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.dependencies import get_user_id_header
from src.schemas.pagination.pagination import PageParams, PagedResponseSchema
from src.schemas.project import Project
from typing import List

import src.services.project as ProjectService

router = APIRouter(
    prefix="/project",
    tags=["project"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

@router.post('')
async def create_project_entry(project:Project, user_id=Depends(get_user_id_header)) -> Project:
    print(f'create a project entry')
    project = ProjectService.create_project_entry(user_id=user_id, project=project)
    return project

@router.get('/all', response_model=PagedResponseSchema[Project])
async def all_Project(user_id=Depends(get_user_id_header), page_params: PageParams = Depends()) -> List[Project]:
   return ProjectService.all_Project(page_params=page_params)

@router.get('')
async def get_project_by_id(project_id:str, user_id=Depends(get_user_id_header)) -> Project:
    # return project for a given id
    return ProjectService.get_project_by_id(user_id=user_id, project_id=project_id)

@router.delete('')
async def delete_project_by_id(project_id:str, user_id=Depends(get_user_id_header)) -> Project:
    # return project for a given id
    return ProjectService.delete_project_by_id(user_id=user_id, project_id=project_id)

