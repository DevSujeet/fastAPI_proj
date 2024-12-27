import time
from datetime import datetime, timezone
from functools import wraps
from logging import getLogger

logger = getLogger(__name__)

def timeit(func):
    """
    This function will tell the time taken by the function
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug(f"Time taken by {func.__name__} to run is {str(end - start)} seconds")
        # if isinstance(result, dict):
        #     result["time_taken"] = round(end - start, 2)
        # return result

    return wrapper