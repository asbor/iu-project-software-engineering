from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from crud.sqlalchemy_users import create_user, delete_user, get_user_by_username, get_user_by_id
from schemas.token import Status
from schemas.users import UserInSchema, UserOutSchema
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserOutSchema)
async def register_user(user: UserInSchema, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.post("/login")
async def login(user: UserInSchema, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires)
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response


@router.get("/users/whoami", response_model=UserOutSchema)
async def who_am_i(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user


@router.delete("/user/{user_id}", response_model=Status)
async def delete_user(user_id: int, db: Session = Depends(get_db), current_user: UserOutSchema = Depends(get_current_user)):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        if db_user.id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You are not allowed to delete this user")
        return delete_user(db, user_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
