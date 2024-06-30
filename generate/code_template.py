TEMPLATE_SCHEMA = '''
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ${ModelName}Base(BaseModel):
    ${fields}
    class Config:
        from_attributes = True

class ${ModelName}Create(${ModelName}Base):
    pass

class ${ModelName}Update(${ModelName}Base):
    pass

class ${ModelName}(${ModelName}Base):
    id: int
    createTime: datetime
    updateTime: datetime
    isDelete: bool

    class Config:
        orm_mode = True
'''
# return ResponseModel(code=500, message="操作失败", data= "null")
# return ResponseModel(code=200, message="操作成功", data= db_interface_info)

TEMPLATE_API = '''
from app.crud import ${model_name_lower} as crud_${model_name_lower}
from app.schemas import ${model_name_lower} as schema_${model_name_lower}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.${model_name_lower} import ${ModelName}, ${ModelName}Create, ${ModelName}Update
from app.api.v1.deps import get_db
from app.schemas import ResponseModel

router = APIRouter()

@router.post("/", response_model = ResponseModel)
def create_${model_name_lower}(${model_name_lower}: ${ModelName}Create, db: Session = Depends(get_db)):
    db_${model_name_lower} = crud_${model_name_lower}.create_${model_name_lower}(db, ${model_name_lower})
    return ResponseModel(code=200, message="操作成功", data= db_${model_name_lower})

@router.get("/{${model_name_lower}_id}", response_model = ResponseModel)
def read_${model_name_lower}(${model_name_lower}_id: int, db: Session = Depends(get_db)):
    db_${model_name_lower} = crud_${model_name_lower}.get_${model_name_lower}(db, ${model_name_lower}_id)
    if db_${model_name_lower} is None:
        return ResponseModel(code=500, message="操作失败", data= "null")
    return ResponseModel(code=200, message="操作成功", data= db_${model_name_lower})

@router.put("/{${model_name_lower}_id}", response_model = ResponseModel)
def update_${model_name_lower}(${model_name_lower}_id: int, ${model_name_lower}: ${ModelName}Update, db: Session = Depends(get_db)):
    db_${model_name_lower} = crud_${model_name_lower}.get_${model_name_lower}(db, ${model_name_lower}_id)
    if db_${model_name_lower} is None:
        return ResponseModel(code=500, message="操作失败", data= "null")
    return ResponseModel(code=200, message="操作成功", data= crud_${model_name_lower}.update_${model_name_lower}(db, db_${model_name_lower}, ${model_name_lower}))

@router.delete("/{${model_name_lower}_id}", response_model = ResponseModel)
def delete_${model_name_lower}(${model_name_lower}_id: int, db: Session = Depends(get_db)):
    db_${model_name_lower} = crud_${model_name_lower}.get_${model_name_lower}(db, ${model_name_lower}_id)
    if db_${model_name_lower} is None:
        return ResponseModel(code=500, message="操作失败", data= "null")
    return ResponseModel(code=200, message="操作成功", data= crud_${model_name_lower}.delete_${model_name_lower}(db, ${model_name_lower}_id))
'''

TEMPLATE_CRUD = '''
from sqlalchemy.orm import Session
from app.models.${model_name_lower} import ${ModelName}
from app.schemas.${model_name_lower} import ${ModelName}Create, ${ModelName}Update

def get_${model_name_lower}(db: Session, ${model_name_lower}_id: int):
    return db.query(${ModelName}).filter(${ModelName}.id == ${model_name_lower}_id).first()

def get_${model_name_lower}s(db: Session, skip: int = 0, limit: int = 100):
    return db.query(${ModelName}).offset(skip).limit(limit).all()

def create_${model_name_lower}(db: Session, ${model_name_lower}: ${ModelName}Create):
    db_${model_name_lower} = ${ModelName}(**${model_name_lower}.dict())
    db.add(db_${model_name_lower})
    db.commit()
    db.refresh(db_${model_name_lower})
    return db_${model_name_lower}

def update_${model_name_lower}(db: Session, db_${model_name_lower}: ${ModelName}, ${model_name_lower}: ${ModelName}Update):
    update_data = ${model_name_lower}.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_${model_name_lower}, key, value)
    db.commit()
    db.refresh(db_${model_name_lower})
    return db_${model_name_lower}

def delete_${model_name_lower}(db: Session, ${model_name_lower}_id: int):
    db_${model_name_lower} = get_${model_name_lower}(db, ${model_name_lower}_id)
    if db_${model_name_lower}:
        db.delete(db_${model_name_lower})
        db.commit()
    return db_${model_name_lower}
'''
