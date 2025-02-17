from src.crud.table_association.project_location import ProjectLocationCRUD
from src.db import get_session
from src.enum.actions import ActionType
from src.schemas.mapping.project_location import ProjectLocationMapping
from src.schemas.pagination.pagination import PageParams, ResponseSchema
from src.schemas.project import ProjectCreate, ProjectResponse
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

def create_project_entry(user_id:str, project:ProjectCreate):
     with get_session() as session:
        project_obj = ProjectCRUD(db_session=session).create_project_entry(project=project)

        if project.locations and len(project.locations) > 0:
            # Todo:- 1. add the entry to location table, fetch location data from 3rd party data base
            # Todo:- 2. add the entry to project location association table
            print("add the entry to project location association table")
            # proceeding assuming the location entry os already made in location table
            # for location in project.locations:
            #     project_location_mapping = ProjectLocationMapping(location_id=location.location_id,
            #                                                       project_id=project_obj.get('project_id'),
            #                                                       location_type=location.location_type)
            #     ProjectLocationCRUD(db_session=session).create_user_activity(proj_loc_mapping=project_location_mapping)

        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           project_id=project_obj.get('project_id'),
                                           action=ActionType.CREATE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        # return project_obj
        return ResponseSchema[ProjectResponse](status="success",
                                               code=200,
                                                message="Project created successfully",
                                                  data=project_obj)
     
def delete_project_by_id(user_id:str, project_id:str):
    with get_session() as session:
        project = ProjectCRUD(db_session=session).delete_project_by_id(project_id=project_id)
        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           project_id=project_id,
                                           action=ActionType.DELETE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        
        return project