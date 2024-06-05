from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from api.router import router

app = FastAPI()
app.include_router(router)


class Todo(BaseModel):
    name: str
    completed: bool


# Mock database



todos = {}


@app.get("/", response_model=List[Todo])
async def read_root():
    return list(todos.values())


@app.post("/", response_model=Todo)
async def create_item(todo: Todo):
    todos[todo.name] = todo
    return todo


@app.get("/{name}", response_model=Todo)
async def read_item(name: str):
    if name not in todos:
        raise HTTPException(status_code=404, detail="Item not found")
    return todos[name]


@app.put("/{name}", response_model=Todo)
async def update_item(name: str, todo: Todo):
    if name not in todos:
        raise HTTPException(status_code=404, detail="Item not found")
    todos[name] = todo
    return todo


@app.delete("/{name}", response_model=Todo)
async def delete_item(name: str):
    if name not in todos:
        raise HTTPException(status_code=404, detail="Item not found")
    todo = todos[name]
    del todos[name]
    return todo
