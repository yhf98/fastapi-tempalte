
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InterfaceInfoBase(BaseModel):
    name: str
    description: str
    url: str
    requestParams: str
    requestHeader: str
    responseHeader: str
    status: int
    method: str
    userId: int
    createTime: datetime
    updateTime: datetime
    isDelete: bool
    class Config:
        from_attributes = True

class InterfaceInfoCreate(InterfaceInfoBase):
    pass

class InterfaceInfoUpdate(InterfaceInfoBase):
    pass

class InterfaceInfo(InterfaceInfoBase):
    id: int
    createTime: datetime
    updateTime: datetime
    isDelete: bool

    class Config:
        orm_mode = True
