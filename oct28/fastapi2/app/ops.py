# Simple ops to do the CRUD on server
# Handle the endpoint requests from the client

from sqlalchemy.orm import Session as st
from . import  models, schema

# Get all todos
async def get_todos(db: st, skip: int = 0, limit: int = 100):
    results = await db.query(models.Todo).offset(skip).limit(limit).all()
    return results

# Create a to do from data
async def create_todo(db: st, todo:schema.TodoCreate):
    db_todo = models.Todo(content = todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo

# Update to do data
async def update_todo(db: st, todo_id: int, done: bool):
    db_todo = await db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db_todo.done = done
    db.commit()
    db.refresh(db_todo)
    return db_todo 
    
    

