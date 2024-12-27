from src.db import get_session
from src.enum.actions import ActionType
from src.schemas.project import Project, ProjectCreate
from src.schemas.user_activity import UserActivityCreate
from src.crud.project import ProjectCRUD
from src.crud.activity import UserActivityCRUD

def all_Project():
    with get_session() as session:
        projects = ProjectCRUD(db_session=session).get_all_project()
        return projects

def get_project_by_id(id:str):
    with get_session() as session:
        project = ProjectCRUD(db_session=session).get_project(project_system_id=id)

        # create user activity
        user_activity = UserActivityCreate(user_id=project.user_id,
                                           project_id=project.project_system_id,
                                           action=ActionType.SEARCH)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)

        return project

def create_project_entry(project:ProjectCreate):
     with get_session() as session:
        project_obj = ProjectCRUD(db_session=session).create_project(project=project)

        # create user activity
        user_activity = UserActivityCreate(user_id=project.user_id,
                                           project_id=project_obj.project_system_id,
                                           action=ActionType.CREATE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        # return project_obj
        return project_obj
     
def delete_project_by_id(user_id:str, project_system_id:str):
    with get_session() as session:
        project = ProjectCRUD(db_session=session).delete_project(project_system_id=id)
        # create user activity
        user_activity = UserActivityCreate(user_id=project.user_id,
                                           project_id=project_system_id,
                                           action=ActionType.CREATE)
        
        return project