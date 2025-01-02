from sqlalchemy.exc import IntegrityError
import sqlite3
from fastapi import HTTPException
from sqlalchemy import and_, asc
from src.schemas.pagination.pagination import PageParams, paginate
from src.schemas.project import Project
from src.models.project import ProjectData
from src.crud.base_curd import BaseCRUD

class ProjectCRUD(BaseCRUD):
    def all_Project(self, page_params:PageParams):
        query = self.db_session.query(ProjectData).order_by(asc(ProjectData.created))
        return paginate(page_params, query, Project)

    def get_project_by_id(self, project_id:str):
        if not project_id:
            raise HTTPException(status_code=400, detail="Project ID must be provided")
        
        filters = [ProjectData.project_id == project_id]
        query = self.db_session.query(ProjectData).filter(and_(*filters)).order_by(asc(ProjectData.created))
        project = query.first()
        if project:
            return project
        else:
            raise HTTPException(status_code=404, detail="Project not found")

    def create_project_entry(self, project:Project):
        try:
            project_obj = ProjectData(**project.model_dump(exclude={"locations"}))
            self.db_session.add(project_obj)
            print(f'create_project in crud post{project_obj}')
            self.db_session.flush()
            self.db_session.commit()
            self.db_session.refresh(project_obj)
            print(f'project is created {project_obj}')
            project_dict = project_obj.__dict__.copy()
            project_dict.pop("_sa_instance_state", None)  # Remove SQLAlchemy internal state
            return project_dict
            # return project_obj
        except IntegrityError as e:
            print(f"IntegrityError: {e}")  # Log the full exception
            print(f"Exception details: {e.orig}")  # Print out the underlying database exception details

            # Handle SQLite unique constraint violation
            if "UNIQUE constraint failed" in str(e.orig):
                print("Unique constraint failed: project_id already exists.")
                raise HTTPException(status_code=400, detail="Project ID already exists")
            
            # Catch other IntegrityErrors and re-raise with a generic error
            raise HTTPException(status_code=500, detail="Internal Server Error")
        except Exception as e:
        # This will catch any unexpected exceptions that are not specifically caught by the above blocks
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
    
    def delete_project_by_id(self, project_id:str):
        project = self.get_project_by_id(project_id=project_id)
        if project:
            self.db_session.delete(project)
            self.db_session.commit()
            return project
        else:
            raise HTTPException(status_code=404, detail="Project not found")