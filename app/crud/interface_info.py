
from sqlalchemy.orm import Session
from app.models.interface_info import InterfaceInfo
from app.schemas.interface_info import InterfaceInfoCreate, InterfaceInfoUpdate

def get_interface_info(db: Session, interface_info_id: int):
    return db.query(InterfaceInfo).filter(InterfaceInfo.id == interface_info_id).first()

def get_interface_infos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InterfaceInfo).offset(skip).limit(limit).all()

def create_interface_info(db: Session, interface_info: InterfaceInfoCreate):
    db_interface_info = InterfaceInfo(**interface_info.dict())
    db.add(db_interface_info)
    db.commit()
    db.refresh(db_interface_info)
    return db_interface_info

def update_interface_info(db: Session, db_interface_info: InterfaceInfo, interface_info: InterfaceInfoUpdate):
    update_data = interface_info.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_interface_info, key, value)
    db.commit()
    db.refresh(db_interface_info)
    return db_interface_info

def delete_interface_info(db: Session, interface_info_id: int):
    db_interface_info = get_interface_info(db, interface_info_id)
    if db_interface_info:
        db.delete(db_interface_info)
        db.commit()
    return db_interface_info
