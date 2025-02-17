
from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.config.configs import _db_settings
from typing import Dict
from src.config.log_config import logger

router = APIRouter(
    prefix="/intro",
    tags=["intro"]
)

db_settings_instance = _db_settings()

@router.get('')
async def index() -> Dict[str, str]:
    logger.info("Fetching database settings")
    return db_settings_instance.model_dump()
    # return {'test':'hello'}

@router.get('/about')
async def about() -> str:
    return "great company"