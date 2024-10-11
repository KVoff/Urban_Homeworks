from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from typing import Annotated


from app.backend.db_depends import get_db
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask


router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.execute(select(Task)).scalars().all()

    return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.execute(select(Task).where(Task.id == task_id)).scalars().first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
        )

    return task


@router.post("/create")
async def create_task(
    db: Annotated[Session, Depends(get_db)],
    create_task: CreateTask,
    user_id: int
):
    user = db.execute(select(User).where(User.id == user_id)).scalars().first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )

    task = insert(Task).values(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority,
        user_id=user_id,
        slug=slugify(create_task.title)
    ).returning(Task.id)

    db.execute(task)
    db.commit()

    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Successful"
    }


@router.put("/update")
async def update_task(
    db: Annotated[Session, Depends(get_db)],
    update_task: UpdateTask,
    task_id: int
):

    task_exist = db.execute(
            select(Task).where(Task.id == task_id)
            ).scalars().first()

    if not task_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )

    task = update(Task).where(Task.id == task_id).values(
        content=update_task.content,
        priority=update_task.priority
        )

    db.execute(task)
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):

    task_exist = db.execute(
        select(Task).where(Task.id == task_id)
        ).scalars().first()

    if not task_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found'
        )

    task = delete(Task).where(Task.id == task_id)

    db.execute(task)
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task delete is successful!'
    }
