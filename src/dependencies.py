
from fastapi import Header, HTTPException
from fastapi.logger import logger

async def get_user_id_header(x_user_id: str = Header(...)):
    if not x_user_id or x_user_id == "undefined":
        logger.error("Invalid user_id sent for rest call")
        raise HTTPException(status_code=406, detail="x_user_id field is required in header")
    return x_user_id