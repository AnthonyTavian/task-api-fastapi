from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

# Cria as tabelas no banco
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="API REST para gerenciamento de tarefas",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Task API running! Acesse /docs para ver a documentação"}

@app.post("/tasks", response_model=schemas.Task, status_code=201)
def create_tasks(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title, description=task.description, done=task.done)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
    

@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):    
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.title = task.title if task.title is not None else db_task.title
    db_task.description = task.description if task.description is not None else db_task.description
    db_task.done = task.done if task.done is not None else db_task.done
    db.commit()
    return db_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):    
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return None