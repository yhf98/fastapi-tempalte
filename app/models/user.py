from sqlalchemy import Column, String, Integer, BigInteger, DateTime, Boolean
from app.models import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, index=True)
    userName = Column(String(256), nullable=True)
    userAccount = Column(String(256), nullable=False, unique=True)
    userAvatar = Column(String(1024), nullable=True)
    gender = Column(Integer, nullable=True)
    userRole = Column(String(256), default='user', nullable=False)
    userPassword = Column(String(512), nullable=False)
    accessKey = Column(String(512), nullable=False)
    secretKey = Column(String(512), nullable=False)
    createTime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updateTime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    isDelete = Column(Boolean, default=False, nullable=False)
