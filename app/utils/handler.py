from fastapi.responses import JSONResponse
from fastapi import Request
import logging
from fastapi import Request

from app.schemas.response import ResponseModel


async def custom_exception_handler(request: Request, exc: Exception):
    logging.error(f"Exception: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content=ResponseModel(code=500, message="系统内部错误！").dict(),
    )
