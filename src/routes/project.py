from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.schemas.project import Project
from typing import List

from src.services.user import create_user, get_all_user, get_user_by_id

router = APIRouter(
    prefix="/project",
    tags=["project"],
    responses={404: {"description": "project not in db"}}
)

@router.get('/all')
async def all_Project() -> List[Project]:
   print(f'get all project')

@router.get('')
async def get_project_by_id(id:str) -> Project:
    # return record for a given id
    print(f'return project for a given id')

@router.post('')
async def create_project_entry(user:Project) -> Project:
    print(f'create a project entry')