from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from sqlalchemy import insert, select, update, delete
from app.schemas import CreateUser, UpdateUser
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(get_db: Annotated[Session, Depends(get_db)]):
    users = get_db.scalars(select(User)).all()
    if users is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no users'
        )
    return users


@router.get('/user_id')
async def user_by_id(get_db: Annotated[Session, Depends(get_db)], user_id: int):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    return user


@router.get('/user_id/tasks')
async def tasks_by_user_id(get_db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = get_db.scalar(select(Task).where(Task.user_id == user_id))
    return tasks


@router.post('/create')
async def create_user(get_db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    get_db.execute(insert(User).values(id=create_user.id, username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    get_db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(get_db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    get_db.execute(update(User).where(User.id == user_id).values(id=create_user.id, username=create_user.username,
                                                             firstname=create_user.firstname,
                                                             lastname=create_user.lastname,
                                                             age=create_user.age,
                                                             slug=slugify(create_user.username)))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_user(get_db: Annotated[Session, Depends(get_db)], user_id: int):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    get_db.execute(delete(User).where(User.id == user_id))
    get_db.execute(delete(Task).where(Task.user_id == user_id))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
