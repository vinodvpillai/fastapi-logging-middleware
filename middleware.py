from fastapi import Request
from logger import logger

async def log_middleware(request: Request, call_next):
    # Here we can get the request information from every request and log it out
    log_dict = {
        'url': request.url.path,
        'method': request.method
    }
    logger.info(log_dict)
    
    # Here we can get the response and modify the response prior returning
    respose = await call_next(request)
    return respose