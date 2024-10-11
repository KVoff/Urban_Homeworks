from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from typing import Annotated

from app.backend.db_depends import get_db
from app.models import User
from app.schemas import CreateUser, UpdateUser


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.execute(select(User)).scalars().all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.execute(select(User).where(User.id == user_id)).scalars().first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )

    return user


@router.post('/create')
async def create_user(
    db: Annotated[Session, Depends(get_db)],
    create_user: CreateUser
):

    user_exist = db.execute(
            select(User).where(User.username == create_user.username)
            ).scalars().first()

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this username already exists'
        )

    user = insert(User).values(
            username=create_user.username,
            firstname=create_user.firstname,
            lastname=create_user.lastname,
            age=create_user.age,
            slug=slugify(create_user.username)
        )

    db.execute(user)
    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
        }


@router.put('/update')
async def update_user(
    db: Annotated[Session, Depends(get_db)],
    update_user: UpdateUser,
    user_id: int
):

    user_exist = db.execute(
            select(User).where(User.id == user_id)
            ).scalars().first()

    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    user = update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age
        )

    db.execute(user)
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_user(
    db: Annotated[Session, Depends(get_db)],
    user_id: int
):

    user_exist = db.execute(
        select(User).where(User.id == user_id)
        ).scalars().first()

    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    user = delete(User).where(User.id == user_id)

    db.execute(user)
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is successful!'
    }
