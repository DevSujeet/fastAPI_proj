import time
from fastapi import Request
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from src.config.configs import _ctx_var

class ErrorTemplate:
    pass

async def add_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = str(process_time)
    return response