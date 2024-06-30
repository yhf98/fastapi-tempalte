import uvicorn
import logging
from fastapi import FastAPI
from app.api.v1 import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.middleware import TokenValidationMiddleware, RequestLoggingMiddleware
from app.core.logging import setup_logger
from app.utils.handler import custom_exception_handler

app = FastAPI(
    title="fastapi-template",
    description="Fast-API 项目模板",
    version="0.0.1"
)

app.include_router(api_router, prefix="/api/v1")
# exempt_routes = ["/favicon.ico", "/api/v1/users/register",
#                  "/api/v1/users/login", "/docs", "/docs/", "/openapi.json", "/redoc", "/api/v1/logs/test", "/api/v1/logs/publish", "/v1/apis/validate_key"]
exempt_routes = [
    r"/favicon\.ico",
    r"/api/v1/users/register",
    r"/api/v1/users/login",
    r"/docs",
    r"/docs/",
    r"/openapi\.json",
    r"/redoc",
    r"/api/v1/logs/test",
    r"/api/v1/logs/publish",
    r"/api/v1/apis/validate_key.*"
]

# app.add_middleware(TokenValidationMiddleware, exempt_routes=exempt_routes)

app.add_middleware(TokenValidationMiddleware, exempt_routes=exempt_routes)

# 注册全局异常处理器
app.add_exception_handler(Exception, custom_exception_handler)

# 添加日志中间件
app.add_middleware(RequestLoggingMiddleware)
# 添加Token验证中间件

app.add_middleware(TokenValidationMiddleware, exempt_routes=exempt_routes)

# 添加CORS中间件
origins = [
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





if __name__ == "__main__":
    logging.info("服务启动...")
    uvicorn.run(app, host="0.0.0.0", port=9527)
