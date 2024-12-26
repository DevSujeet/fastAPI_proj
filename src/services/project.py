from src.db import get_session
from src.schemas.project import Project
from src.crud.project import ProjectCRUD

def all_Project():
    with get_session() as session:
        projects = ProjectCRUD(db_session=session).get_all_project()
        return projects

def get_project_by_id(id:str):
    with get_session() as session:
        project = ProjectCRUD(db_session=session).get_project(project_system_id=id)
        return project

def create_project_entry(project:Project):
     with get_session() as session:
        project = ProjectCRUD(db_session=session).create_project(project=project)
        return project