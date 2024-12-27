from typing import List
from src.schemas.user_analytics.location_analytics import LocationOverViewResponse
from src.schemas.user_analytics.project_analytics import ProjectOverViewResponse, ProjectsByLocationResponse
from src.schemas.location import LocationRequest    

def getLocationOverView() -> LocationOverViewResponse:
    pass

def getProjectOverView() -> ProjectOverViewResponse:
    pass

def getProjectsByLocation(request:LocationRequest) -> List[ProjectsByLocationResponse]:
    pass