from pydantic import BaseModel
from datetime import datetime
from app.models.models import TaskStatus

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.TODO

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    created_at: datetime 
    updated_at: datetime

    class Config:
        from_attributes = True
