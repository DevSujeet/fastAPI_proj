from sqlalchemy import and_, asc
from src.schemas.project import Project
from src.models.project import ProjectData
from src.crud.base_curd import BaseCRUD

class ProjectCRUD(BaseCRUD):
    def all_Project(self):
        query = self.db_session.query(ProjectData).order_by(asc(ProjectData.created))
        return query.all()

    def get_project_by_id(self, id:str):
        filters = []
        if id:
            filters.append(ProjectData.project_system_id == id)
        query = self.db_session.query(ProjectData).filter(and_(*filters)).order_by(asc(ProjectData.created))
        return query.all()

    def create_project_entry(self, project:Project):
        project_obj = ProjectData(**project)
        self.db_session.add(project_obj)
        print(f'create_project in crud post{project_obj}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(project_obj)
        print(f'project is created {project_obj}')
        return project_obj