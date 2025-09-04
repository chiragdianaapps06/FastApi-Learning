from sqlalchemy.orm import Session
from app.schemas.users import UserCreate
from app.models.user import Users
from app.utils import auth

def create_user(db: Session, user: UserCreate):
    hashed_pw = auth.get_password_hash(user.password)
    db_user = Users(
        username=user.username,
        email=user.email,
        password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()
