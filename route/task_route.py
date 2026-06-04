from fastapi import FastAPI,APIRouter,Depends
from services.service_task import create_task,get_tasks
from schemas.task_validation import ResponseTask,CreateTask
from typing import List
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/get_task',response_model=List[ResponseTask])
async def get_task(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db)

@router.post('/add_task',response_model=ResponseTask)
async def add_task(task: CreateTask, db: AsyncSession = Depends(get_db)):
    return await create_task(task,db)



