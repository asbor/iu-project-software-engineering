from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from models import User
from schemas.token import Status
from schemas.users import UserOutSchema
from database import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user) -> UserOutSchema:
    hashed_password = pwd_context.hash(user.password)
    # Exclude password from database insert
    user_data = user.dict(exclude={"password"})

    try:
        db_user = User(**user_data, password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Username already exists"
        )

    return UserOutSchema.from_orm(db_user)


def delete_user(db: Session, user_id: int, current_user) -> Status:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found"
        )

    if db_user.id == current_user.id:
        db.delete(db_user)
        db.commit()
        return Status(message=f"Deleted user {user_id}")

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete"
    )
