from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Task
from config.schema import TaskCreate

async def create_task(db: AsyncSession, task_data: TaskCreate):
    new_task = Task(**task_data.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def get_all_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()

async def get_task(db: AsyncSession, task_id: int):
    return await db.get(Task, task_id)

async def update_task(db: AsyncSession, task, task_data):
    for key, value in task_data.dict().items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task):
    await db.delete(task)
    await db.commit()
