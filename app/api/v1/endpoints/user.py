
from app.crud import user as crud_user
from app.schemas import user as schema_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.core.security import verify_password, create_access_token
from app.api.v1.deps import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.token import Token
from app.schemas import ResponseModel, UserBase

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=ResponseModel)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_account(db, user.userAccount)
    if db_user:
        return ResponseModel(code=500, message="用户创建成功！", data= f"【{user.userAccount}】: 该用户已存在")
    
    user_data = UserBase.from_orm(crud_user.create_user(db, user))
    return ResponseModel(code=200, message="用户创建成功！", data=user_data)


@router.get("/{user_id}", response_model=ResponseModel)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="找不到该用户")
    user_data = UserBase.from_orm(db_user)
    return ResponseModel(code=200, message="操作成功", data=user_data)


@router.put("/{user_id}", response_model=ResponseModel)
def update_user(user_id: int, user_update: schema_user.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id)
    if db_user is None:
        return ResponseModel(code=200, message="操作成功", data="找不到该用户")

    user_data = UserBase.from_orm(
        crud_user.update_user(db, db_user, user_update))
    return ResponseModel(code=200, message="操作成功", data=user_data)


@router.delete("/{user_id}", response_model=ResponseModel)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id)
    if db_user is None:
        return ResponseModel(code=200, message="操作成功", data="找不到该用户")
    user_data = UserBase.from_orm(
        crud_user.delete_user(db, user_id))
    return ResponseModel(code=200, message="操作成功", data = user_data)


@router.post("/login", response_model=ResponseModel)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud_user.get_user_by_account(db, form_data.username)
    if not user:
        return ResponseModel(code=200, message="操作失败", data=f"用户：【{form_data.username}】，还没注册！")
    if not verify_password(form_data.password, user.userPassword):
        return ResponseModel(code=200, message="操作失败", data=f"密码不正确！")

    access_token = create_access_token(data={"sub": user.userAccount})

    return ResponseModel(code=200, message="操作成功", data={"access_token": access_token, "token_type": "bearer"})
