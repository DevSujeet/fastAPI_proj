from typing import List
from fastapi import APIRouter, Depends
from fastapi.logger import logger
from logging import getLogger

from src.dependencies import get_user_id_header
from src.schemas.location import LocationRequest
from src.schemas.user_analytics.project_analytics import ProjectStatusOverViewResponse, ProjectsCountByLocationResponse, ProjectsByLocationResponse
from src.services.analytics import getLocationOverView, getProjectOverView, getProjectsByLocation

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

@router.get("/projects_count_by_state")
async def get_projects_count_by_state(user_id=Depends(get_user_id_header)) -> List[ProjectsCountByLocationResponse]:
    """
    ## get_projects_count_by_state
    Endpoint to fetch project count by state
    """
    logger.debug("get_projects_count_by_state")
    return getLocationOverView()

@router.get("/all_projects_by_location")
async def get_all_projects_by_location(location:LocationRequest, user_id=Depends(get_user_id_header)) -> List[ProjectsByLocationResponse]:
    """
    get all projects for a given location    
    """
    logger.debug(f"get_project_location_overview, for {location}!")
    return getProjectsByLocation(location)


@router.get("/project_status_overview")
async def get_project_status_overview(location:LocationRequest, user_id=Depends(get_user_id_header)) -> ProjectStatusOverViewResponse:
    """
    ## project_status_overview
    get active/completed/onhold projects for a given location
    """
    logger.debug(f"get_project_status_overview, for {location}!")
    return getProjectOverView()


@router.get("/location_status_overview")
async def get_location_status_overview(location:LocationRequest, user_id=Depends(get_user_id_header)) -> ProjectStatusOverViewResponse:
    """
    ## location_status_overview
    get active/completed/onhold projects for a given location
    """
    logger.debug("get_location_overview")
    return f"get_location_overview, for {location}!"


@router.get("/upload_data_category_distribution")
async def get_upload_data_category_distribution(user_id=Depends(get_user_id_header)):
    """
    ## upload_data_category_distribution
    Endpoint to upload_data_category_distribution throughout the service usage
    """
    logger.debug("get_upload_data_category_distribution")
    return f"upload_data_category_distribution"

@router.get("/user_role_distribution")
async def get_user_role_distribution(user_id=Depends(get_user_id_header)):
    """
    ## get_user_role_distribution
    Endpoint to get_user_role_distribution throughout the org
    """
    logger.debug("get_user_role_distribution")
    return f"get_user_role_distribution"


@router.get("/data_utilization")
async def get_user_role_distribution(user_id=Depends(get_user_id_header)):
    """
    ## data_utilization
    Endpoint to track the storage of document system, showing how much storage is used vs. available
    """
    logger.debug("get_user_role_distribution")
    return f"get_user_role_distribution"



@router.get("/users_activity_log")
async def get_all_users_activity_log(user_id=Depends(get_user_id_header)):
    """
    ## get_all_users_activity_log
    Endpoint to get_all_users_activity_log sorted by most recent and paginated response
    """
    logger.debug("get_all_users_activity_log")
    return f"get_user_activities for user"