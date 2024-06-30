from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_401_UNAUTHORIZED
from starlette.responses import JSONResponse
from app.core.security import verify_token
from app.crud.user import get_user_by_account
from app.api.v1.deps import get_db
from app.schemas.response import ResponseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenValidationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, exempt_routes: list):
        super().__init__(app)
        self.exempt_routes = exempt_routes

    async def dispatch(self, request: Request, call_next):
        if request.url.path in self.exempt_routes:
            return await call_next(request)
        
        token = request.headers.get("Authorization")
        if not token:
            return JSONResponse(
                status_code=HTTP_401_UNAUTHORIZED,
                content=ResponseModel(code=401, message="请求没有Token").dict()
            )
        
        try:
            scheme, token = token.split()
            if scheme.lower() != 'bearer':
                raise ValueError("Token 格式不正确")
            
            username = verify_token(token)
            if username is None:
                raise ValueError("无效Token")

            with next(get_db()) as db:
                user = get_user_by_account(db, username)
                if user is None:
                    raise ValueError("找不到用户信息")

        except Exception as e:
            return JSONResponse(
                status_code=HTTP_401_UNAUTHORIZED,
                content=ResponseModel(code=401, message=str(e)).dict()
            )

        response = await call_next(request)
        return response
