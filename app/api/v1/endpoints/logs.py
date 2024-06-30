import logging
from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/test")
async def test():
    return {"status": "test"}

@router.post("/publish")
async def receive_logs(request: Request):
    data = await request.json()
    logging.info(f"API访问日志信息: {data}")
    return {"status": "success"}