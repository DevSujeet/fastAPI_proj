from src.db import get_session
from src.enum.actions import ActionType
from src.schemas.pagination.pagination import PageParams
from src.schemas.project import Project
from src.schemas.user_activity import UserActivityCreate
from src.crud.project import ProjectCRUD
from src.crud.activity import UserActivityCRUD

def all_Project(page_params:PageParams):
    with get_session() as session:
        projects = ProjectCRUD(db_session=session).all_Project(page_params=page_params)
        return projects

def get_project_by_id(user_id:str, project_id:str):
    with get_session() as session:
        project = ProjectCRUD(db_session=session).get_project_by_id(project_id=project_id)

        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           project_id=project.project_id,
                                           action=ActionType.SEARCH)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)

        return project

def create_project_entry(user_id:str, project:Project):
     with get_session() as session:
        project_obj = ProjectCRUD(db_session=session).create_project_entry(project=project)

        if project.locations and len(project.locations) > 0:
            # Todo:- add the entry to project location association table
            print("MISING:-add the entry to project location association table")

        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           project_id=project_obj.get('project_id'),
                                           action=ActionType.CREATE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        # return project_obj
        return project_obj
     
def delete_project_by_id(user_id:str, project_id:str):
    with get_session() as session:
        project = ProjectCRUD(db_session=session).delete_project_by_id(project_id=project_id)
        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           project_id=project_id,
                                           action=ActionType.DELETE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        
        return project