from sqlalchemy.orm import Session
from app.db.session import Base
from app.db.session import engine

def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
