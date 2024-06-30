import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logging.info(f"Request: {request.method} {request.url}")
        logging.info(f"Header: {request.headers}")
        logging.info(f"Params: {request.query_params}")
        logging.info(f"Body: {await request.body()}")

        response = await call_next(request)

        logging.info(f"Response: {response.status_code}")
        return response