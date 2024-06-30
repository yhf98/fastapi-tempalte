

from fastapi import APIRouter, Query, HTTPException

router = APIRouter()

@router.get("/validate_key")
async def validate_key(key: str = Query(...)):
    if key != "123456":
        raise HTTPException(status_code=403, detail="Invalid API key")
    return {"status": "valid"}
