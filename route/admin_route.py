from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from services.service_admin import (
    insert_admin,
    get_admin,
    delete_admin,
    patch_admin
)
from schemas.admin_validation import (
    admin_create,
    admin_response,
    admin_update
)
from typing import List
from database import get_db

router = APIRouter()

@router.post("/insert", response_model= admin_create)
async def insert(admin: admin_create,db: AsyncSession = Depends(get_db)):
    return await insert_admin(admin,db)

@router.get("/get",response_model=List[admin_response])
async def retrive_admin(db: AsyncSession = Depends(get_db)):
    return await get_admin(db)

@router.delete("/delete/{id}")
async def del_admin(id:int ,db: AsyncSession = Depends(get_db)):
    return await delete_admin(id,db)

@router.patch("/update/{id}",response_model=admin_response)
async def update_admin(id:int ,admin: admin_update,db: AsyncSession = Depends(get_db)):
    return await patch_admin(id,admin,db)