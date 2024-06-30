from sqlalchemy import Column, String, Integer, BigInteger, DateTime, Boolean, Text
from app.models import Base
from datetime import datetime

class InterfaceInfo(Base):
    __tablename__ = 'interface_info'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    description = Column(String(256), nullable=True)
    url = Column(String(512), nullable=False)
    requestParams = Column(Text, nullable=False)
    requestHeader = Column(Text, nullable=True)
    responseHeader = Column(Text, nullable=True)
    status = Column(Integer, default=0, nullable=False)
    method = Column(String(256), nullable=False)
    userId = Column(BigInteger, nullable=False)
    createTime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updateTime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    isDelete = Column(Boolean, default=False, nullable=False)
