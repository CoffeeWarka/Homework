from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.task import Task
from app.models.user import User
from sqlalchemy import insert, select, update, delete
from app.schemas import CreateTask, CreateUser, UpdateTask

from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(get_db: Annotated[Session, Depends(get_db)]):
    tasks = get_db.scalars(select(Task)).all()
    if tasks is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no tasks'
        )
    return tasks


@router.get('/task_id')
async def task_by_id(get_db: Annotated[Session, Depends(get_db)], task_id: int):
    task = get_db.scalar(select(Task).where(Task.id == task_id))
    if Task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    return task


@router.post('/create')
async def create_task(get_db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    get_db.execute(insert(Task).values(title=create_task.title,
                                       content=create_task.content,
                                       priority=create_task.priority,
                                       slug=slugify(create_task.title),
                                       user_id=user_id))
    get_db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(get_db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = get_db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    get_db.execute(update(Task).where(Task.id == task_id).values(id=create_task.id, title=create_task.title,
                                                             content=create_task.content,
                                                             priority=create_task.priority,
                                                             completed=create_task.completed,
                                                             slug=slugify(create_task.title),
                                                             user_id=create_task.user_id))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete('/delete')
async def delete_task(get_db: Annotated[Session, Depends(get_db)], task_id: int):
    task = get_db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    get_db.execute(delete(Task).where(Task.id == task_id))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}