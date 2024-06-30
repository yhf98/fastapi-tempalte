from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

security = HTTPBasic()

username = "admin"
password = "123456"

async def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == username and credentials.password == password:
        return True
    else:
        return False

class DocsAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/docs") or request.url.path.startswith("/redoc"):
            credentials = HTTPBasicCredentials(
                username=request.headers.get("Authorization", "").split(":")[0],
                password=request.headers.get("Authorization", "").split(":")[1],
            )
            if not await authenticate(credentials):
                return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
        response = await call_next(request)
        return response