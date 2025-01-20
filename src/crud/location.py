from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_, asc
from src.models.location import LocationData
from src.schemas.location import Location, LocationResponse
from src.crud.base_curd import BaseCRUD
from src.schemas.pagination.pagination import PageParams, paginate

class LocationCRUD(BaseCRUD):
    def all_Location(self, page_params:PageParams):
        query = self.db_session.query(LocationData).order_by(asc(LocationData.submitted_date))
        return paginate(page_params=page_params, query=query, ResponseSchema=LocationResponse, model=LocationData)
        # return paginate(page_params, query, LocationResponse)

    def get_location_by_id(self, id:str):
        if not id:
            raise HTTPException(status_code=400, detail="Location ID must be provided")
    
        filters = [LocationData.location_id == id]
        query = self.db_session.query(LocationData).filter(and_(*filters)).order_by(asc(LocationData.submitted_date))
        location = query.first()
        if location:
            return location
        else:
            raise HTTPException(status_code=404, detail="Location not found")
    
    def create_location_entry(self, location=Location):
        try:
            location_obj = LocationData(**location.model_dump(exclude={"complete_address"}))
            self.db_session.add(location_obj)
            print(f'create_location in crud post{location_obj}')
            self.db_session.flush()
            self.db_session.commit()
            self.db_session.refresh(location_obj)
            print(f'location is created {location_obj.__dict__}')
            location_dict = location_obj.__dict__.copy()
            location_dict.pop("_sa_instance_state", None)  # Remove SQLAlchemy internal state
            return location_dict
        except IntegrityError as e:
            print(f"IntegrityError: {e}")  # Log the full exception
            print(f"Exception details: {e.orig}")  # Print out the underlying database exception details

            # Handle SQLite unique constraint violation
            if "UNIQUE constraint failed" in str(e.orig):
                print("Unique constraint failed: adbor_id already exists.")
                raise HTTPException(status_code=400, detail="adbor_id already exists")
            
            # Catch other IntegrityErrors and re-raise with a generic error
            raise HTTPException(status_code=500, detail="Internal Server Error")
        except Exception as e:
        # This will catch any unexpected exceptions that are not specifically caught by the above blocks
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        # return location_obj
    
    def delete_location_by_id(self, id:str):
        location = self.get_location_by_id(id=id)
        if location:
            self.db_session.delete(location)
            self.db_session.commit()
            return location
        else:
            raise HTTPException(status_code=404, detail="Location not found")