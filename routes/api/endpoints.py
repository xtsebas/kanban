from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config.schema import TaskCreate, TaskResponse
from services.crud import create_task, get_all_tasks, get_task, update_task, delete_task
from config.database import SessionLocal

router = APIRouter(prefix="/tasks", tags=["tasks"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=TaskResponse)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)

@router.get("/", response_model=list[TaskResponse])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await get_all_tasks(db)

@router.get("/{task_id}", response_model=TaskResponse)
async def get_single_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
async def update_existing_task(task_id: int, task_data: TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await update_task(db, task, task_data)

@router.delete("/{task_id}", status_code=204)
async def remove_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await delete_task(db, task)