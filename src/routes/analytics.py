from fastapi import APIRouter, Depends
from fastapi.logger import logger
from logging import getLogger

from src.schemas.location import LocationRequest
from src.services.analytics import getLocationOverView, getProjectOverView, getProjectsByLocation

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
    # dependencies=[Depends(get_project_header)],
    # responses={404: {"description": "X_ProjectID field is required in header"}}
)


@router.get("/all_projects_by_location")
async def get_all_projects_by_location(location:LocationRequest):
    """
    get projects by location    
    """
    logger.debug(f"get_project_location_overview, for {location}!")
    return getProjectsByLocation(location)


@router.get("/project_overview")
async def get_project_overview(location:str):
    """
    ## get_project_overview
    Endpoint to fetch project status count by category
    """
    logger.debug("get_project_overview")
    return f"get_location_overview, for {location}!"

@router.get("/location_overview")
async def get_location_overview(location:str):
    """
    ## get_location_overview
    Endpoint to fetch project status count by category for a given location
    """
    logger.debug("get_location_overview")
    return f"get_location_overview, for {location}!"


@router.get("/upload_data_category_distribution")
async def get_upload_data_category_distribution():
 """
    ## upload_data_category_distribution
    Endpoint to upload_data_category_distribution throughout the service usage
    """
 logger.debug("get_upload_data_category_distribution")
 return f"upload_data_category_distribution"

@router.get("/user_role_distribution")
async def get_user_role_distribution():
 """
    ## get_user_role_distribution
    Endpoint to get_user_role_distribution throughout the org
    """
 logger.debug("get_user_role_distribution")
 return f"get_user_role_distribution"


@router.get("/data_utilization")
async def get_user_role_distribution():
 """
    ## data_utilization
    Endpoint to track the storage of document system, showing how much storage is used vs. available
    """
 logger.debug("get_user_role_distribution")
 return f"get_user_role_distribution"



@router.get("/users_activity_log")
async def get_all_users_activity_log():
 """
    ## get_all_users_activity_log
    Endpoint to get_all_users_activity_log sorted by most recent and paginated response
    """
 logger.debug("get_all_users_activity_log")
 return f"get_user_activities for user"