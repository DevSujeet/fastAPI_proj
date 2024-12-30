from fastapi import HTTPException
from sqlalchemy import and_, asc
from src.schemas.project import Project
from src.models.project import ProjectData
from src.crud.base_curd import BaseCRUD

class ProjectCRUD(BaseCRUD):
    def all_Project(self):
        query = self.db_session.query(ProjectData).order_by(asc(ProjectData.created))
        return query.all()

    def get_project_by_id(self, project_system_id:str):
        if not project_system_id:
            raise HTTPException(status_code=400, detail="Project system ID must be provided")
        
        filters = [ProjectData.project_system_id == project_system_id]
        query = self.db_session.query(ProjectData).filter(and_(*filters)).order_by(asc(ProjectData.created))
        project = query.first()
        if project:
            return project
        else:
            raise HTTPException(status_code=404, detail="Project not found")

    def create_project_entry(self, project:Project):
        project_obj = ProjectData(**project.model_dump(exclude={"locations"}))
        self.db_session.add(project_obj)
        print(f'create_project in crud post{project_obj}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(project_obj)
        print(f'project is created {project_obj}')
        return project_obj
    
    def delete_project_by_id(self, project_system_id:str):
        project = self.get_project_by_id(project_system_id=project_system_id)
        if project:
            self.db_session.delete(project)
            self.db_session.commit()
            return project
        else:
            raise HTTPException(status_code=404, detail="Project not found")