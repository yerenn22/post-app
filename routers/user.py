from fastapi import APIRouter, Depends
from sqlmodel import Session

from core import get_session
from models import User
from schemas import UserCreate, UserRead, UserUpdate
from typing import List


router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", response_model=List[UserRead])
async def get_users(session: Session = Depends(get_session)):
    return session.query(User).all()


@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = User(**user.dict())
    session.add(db_user)

    return db_user


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: str, session: Session = Depends(get_session)):
    return session.query(User).get(user_id)


@router.put("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: str, user: UserUpdate, session: Session = Depends(get_session)
):
    db_user = session.query(User).get(user_id)

    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    session.add(db_user)

    return db_user


@router.delete("/{user_id}")
async def delete_user(user_id: str, session: Session = Depends(get_session)):
    db_user = session.query(User).get(user_id)
    session.delete(db_user)

    return db_user
