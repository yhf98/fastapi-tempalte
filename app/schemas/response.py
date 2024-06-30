from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None

    def dict(self, *args, **kwargs):
        return super().dict(*args, **kwargs)
