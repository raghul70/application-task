from schemas.task_validation import CreateTask
from sqlalchemy.ext.asyncio import AsyncSession
from models.task_table import Task
from sqlalchemy import select
from fastapi import HTTPException, Depends
from database import get_db


async def create_task(info:CreateTask,db:AsyncSession= Depends(get_db)):
    task = Task(
        title = info.title,
        completed = info.completed
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks(db:AsyncSession= Depends(get_db)):
    result = await db.execute(select(Task))
    wap = result.scalars().all()
    if not wap:
        raise HTTPException(status_code=404, detail="Task not found")

    return wap