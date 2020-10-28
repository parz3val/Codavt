# Simple to do app with fast API

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session as st 
from app import ops, models, schema 
from app.db import LocalSession as lst 
from app.db import engine


app = FastAPI()

# Manage dependencies
def get_db():
    db = lst()
    try:
        yield db
    finally:
        db.close()

# Route for getting all to do
@app.get("/")
async def read_todos(skip: int = 0, limit: int = 100, db: lst = Depends(get_db)):
    todos = ops.get_todos(db, skip = skip, limit = limit)
    return todos 

# Route to create a new to do
@app.post("/")
async def create_todo(todo: schema.TodoCreate, db: lst = Depends(get_db)):
    db_todo = await ops.create_todo(db, todo)
    return db_todo

# Route to change the to do to complete
@app.put("/{id}")
async def update_todo(id: int, done: bool = True, db: lst = Depends(get_db)):
    db_todo = await ops.update_todo(db, todo_id = id, done = done)
    return db_todo


""" @app.get("/")
async def root():
    return {"Messsage" : "This works"} """

