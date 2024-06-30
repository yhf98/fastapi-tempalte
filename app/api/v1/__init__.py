from fastapi import APIRouter
from app.api.v1.endpoints import user, interface_info, apis, logs

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(interface_info.router, prefix="/interface_info", tags=["interface_info"])
api_router.include_router(apis.router, prefix="/apis", tags=["apis"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])
