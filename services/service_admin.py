from schemas.admin_validation import (
    admin_create,
    admin_update,
    admin_response
)
from sqlalchemy.ext.asyncio import AsyncSession
from models.admin_table import Admin
from sqlalchemy import select
from fastapi import HTTPException, Depends


async def insert_admin(admin: admin_create, db: AsyncSession):
    admin1=Admin(name=admin.name,age=admin.age)
    db.add(admin1)
    await db.commit()
    await db.refresh(admin1)
    return admin1

async def get_admin(db: AsyncSession):
    x=await db.execute(select(Admin))
    result= x.scalars().all()
    return result

async def delete_admin(admin_id: int, db: AsyncSession):
    x= await db.execute(select(Admin).where(Admin.id == admin_id))
    result= x.scalars().one_or_none()
    if result:
        await db.delete(result)
        await db.commit()
        return {
            "message": "success"
        }
    raise HTTPException(status_code=404, detail="admin not found")

async def patch_admin(admin_id: int, admin:admin_update , db: AsyncSession):
    x=await db.execute(select(Admin).where(Admin.id == admin_id))
    result= x.scalars().one_or_none()
    if result:
        if admin.name is not None:
            result.name = admin.name

        if admin.age is not None:
            result.age = admin.age

        await db.commit()
        await db.refresh(result)
        return result
    raise HTTPException(status_code=404, detail="admin not found")
