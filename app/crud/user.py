from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_account(db: Session, user_account: str):
    return db.query(User).filter(User.userAccount == user_account).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db_user.userPassword = get_password_hash(user.userPassword)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: User, user_update: UserUpdate):
    for var, value in vars(user_update).items():
        if var == 'userPassword':
            print("修改密码：：", var, value)
            setattr(db_user, var, get_password_hash(value))
        print("修改属性：：", var, value)
        setattr(db_user, var, value) if value else None
    db.commit()
    print(db_user)
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    db_user.isDelete = True
    db.commit()
    db.refresh(db_user)
    return db_user
