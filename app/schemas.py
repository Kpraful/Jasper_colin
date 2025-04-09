from pydantic import BaseModel
from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import datetime
from typing import List
class TaskStatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatusEnum

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[TaskStatusEnum] = None

class Task(TaskBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PaginatedTasksResponse(BaseModel):
    tasks: List[Task]  # This will be a list of Task Pydantic models
    next: Optional[str] = None