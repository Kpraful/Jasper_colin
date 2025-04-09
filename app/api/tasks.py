from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
import crud, schemas
import database as dependencies

router = APIRouter()

@router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(dependencies.get_db)):
    print("task is ",task)
    print("db is ",db)
    return crud.create_task(db=db, task=task)

@router.get("/tasks/", response_model=schemas.PaginatedTasksResponse)
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
    next_skip = skip + limit if len(tasks) == limit else None
    return {
        "tasks": tasks,
        "next": f"/tasks/?skip={next_skip}&limit={limit}" if next_skip else None
    }

@router.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: UUID, db: Session = Depends(dependencies.get_db)):
    db_task = crud.get_task_by_id(db=db, task_id=task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: UUID, task: schemas.TaskUpdate, db: Session = Depends(dependencies.get_db)):
    db_task = crud.update_task(db=db, task_id=task_id, task_update=task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: UUID, db: Session = Depends(dependencies.get_db)):
    db_task = crud.delete_task(db=db, task_id=task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
