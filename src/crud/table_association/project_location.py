from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy import and_, asc
from src.models.association.project_location import ProjectLocationData
from src.crud.base_curd import BaseCRUD
from src.schemas.mapping.project_location import ProjectLocationMapping

class ProjectLocationCRUD(BaseCRUD):

    def create_user_activity(self, proj_loc_mapping:ProjectLocationMapping):
        try:
            mapping_obj = ProjectLocationData(**proj_loc_mapping.model_dump())
            self.db_session.add(mapping_obj)

            self.db_session.flush()
            self.db_session.commit()
            self.db_session.refresh(mapping_obj)
            return mapping_obj
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            print(f"Exception details: {e.orig}")
            if "UNIQUE constraint failed" in str(e.orig):
                print("forgein key constraint failed: project_id doesn't exists.")
                raise HTTPException(status_code=400, detail="project_id doesn't exists")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        