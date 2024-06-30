
from app.crud import interface_info as crud_interface_info
from app.schemas import interface_info as schema_interface_info
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.interface_info import InterfaceInfo, InterfaceInfoCreate, InterfaceInfoUpdate
from app.api.v1.deps import get_db
from app.schemas import ResponseModel, InterfaceInfoBase

router = APIRouter()

@router.post("/", response_model=ResponseModel)
def create_interface_info(interface_info: InterfaceInfoCreate, db: Session = Depends(get_db)):
    db_interface_info = crud_interface_info.create_interface_info(db, interface_info)
    interface_info_data = InterfaceInfoBase.from_orm(db_interface_info) 
    return ResponseModel(code=200, message="操作成功", data= interface_info_data)

@router.get("/{interface_info_id}", response_model=ResponseModel)
def read_interface_info(interface_info_id: int, db: Session = Depends(get_db)):
    db_interface_info = crud_interface_info.get_interface_info(db, interface_info_id)
    if db_interface_info is None:
        return ResponseModel(code=500, message="操作失败", data= "null")
    interface_info_data = InterfaceInfoBase.from_orm(db_interface_info) 
    return ResponseModel(code=200, message="操作成功", data= interface_info_data)

@router.put("/{interface_info_id}", response_model=ResponseModel)
def update_interface_info(interface_info_id: int, interface_info: InterfaceInfoUpdate, db: Session = Depends(get_db)):
    db_interface_info = crud_interface_info.get_interface_info(db, interface_info_id)
    if db_interface_info is None:
        return ResponseModel(code=500, message="操作失败", data= "null") 
    interface_info_data = InterfaceInfoBase.from_orm(crud_interface_info.update_interface_info(db, db_interface_info, interface_info)) 
    return ResponseModel(code=200, message="操作成功", data= interface_info_data)

@router.delete("/{interface_info_id}", response_model=ResponseModel)
def delete_interface_info(interface_info_id: int, db: Session = Depends(get_db)):
    db_interface_info = crud_interface_info.get_interface_info(db, interface_info_id)
    if db_interface_info is None:
        return ResponseModel(code=500, message="操作失败", data= "null")  
    interface_info_data = InterfaceInfoBase.from_orm(crud_interface_info.delete_interface_info(db, interface_info_id)) 
    return ResponseModel(code=200, message="操作成功", data= interface_info_data) 
