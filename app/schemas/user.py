from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    userName: Optional[str] = None
    userAccount: str
    userAvatar: Optional[str] = None
    gender: Optional[int] = None
    userRole: Optional[str] = "user"
    accessKey: str
    secretKey: str
    class Config:
        from_attributes = True
    

class UserCreate(UserBase):
    userPassword: str

class UserUpdate(UserBase):
    userPassword: Optional[str] = None

class User(UserBase):
    id: int
    createTime: datetime
    updateTime: datetime
    isDelete: bool

    class Config:
        orm_mode = True
