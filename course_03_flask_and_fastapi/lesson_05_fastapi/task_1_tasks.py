"""
    📌 Создать API для управления списком задач. Приложение должно иметь
    возможность создавать, обновлять, удалять и получать список задач.
    📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
    📌 Создайте класс Task с полями id, title, description и status.
    📌 Создайте список tasks для хранения задач.
    📌 Создайте маршрут для получения списка задач (метод GET).
    📌 Создайте маршрут для создания новой задачи (метод POST).
    📌 Создайте маршрут для обновления задачи (метод PUT).
    📌 Создайте маршрут для удаления задачи (метод DELETE).
    📌 Реализуйте валидацию данных запроса и ответа.
"""
from typing import Optional, List
import uvicorn as uvicorn
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: str

fake_db = [Task(id=1, title='Title 1', description='Descr 1', status='Created')]
tasks = fake_db.copy()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks


@app.post("/tasks/", response_model=List[Task])
async def create_task(new_task: TaskIn):

    tasks.append(
        Task(
            id=len(tasks) + 1,
            title=new_task.title,
            description=new_task.description,
            status=new_task.status,
        )
    )

    return tasks
"""
    Example post("/tasks/):
    curl -X 'POST' 'http://127.0.0.1:6000/tasks/' -H 'accept:application/json' -H 'Content-Type: application/json' -d'{"title": "test1", "description": "Test 123","status": "test_status"}'
"""

@app.put("/tasks/", response_model=Task)
async def edit_task(task_id:int, new_task: TaskIn):
    current_task = None
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            current_task = tasks[task_id - 1]
            current_task.title = new_task.title
            current_task.description = new_task.description
            current_task.status = new_task.status
            return current_task
    raise HTTPException(status_code=404, detail="Task not found")
"""
    Example put("/tasks/):
    curl -X 'PUT' 'http://127.0.0.1:6000/tasks/?task_id=1' -H 'accept:application/json' -H 'Content-Type: application/json' -d'{"title": "new_test1", "description": "new descr","status": "new_status"}'
"""

@app.delete("/tasks/", response_model=dict)
async def delete_task(task_id: int):
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            tasks.remove(tasks[i])
            return {"message": f"Task {task_id} was deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    uvicorn.run("task_1_tasks:app", host="127.0.0.1", port=6000, reload=True)
