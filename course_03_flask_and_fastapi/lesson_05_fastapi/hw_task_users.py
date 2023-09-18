"""
    📌 Создать API для добавления нового пользователя в базу данных. Приложение
    должно иметь возможность принимать POST запросы с данными нового
    пользователя и сохранять их в базу данных.
    📌 Создать API для обновления информации о пользователе в базе данных.
    Приложение должно иметь возможность принимать PUT запросы с данными
    пользователей и обновлять их в базе данных.
    📌 Создать API для удаления информации о пользователе из базы данных.
    Приложение должно иметь возможность принимать DELETE запросы и
    удалять информацию о пользователе из базы данных.
    📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
    📌 Создайте класс User с полями id, name, email и password.
    📌 Создайте список users для хранения пользователей.
    📌 Создайте маршрут для добавления нового пользователя (метод POST).
    📌 Создайте маршрут для обновления информации о пользователе (метод PUT).
    📌 Создайте маршрут для удаления информации о пользователе (метод DELETE).
    📌 Реализуйте валидацию данных запроса и ответа.
    📌 Создать веб-страницу для отображения списка пользователей. Приложение
    должно использовать шаблонизатор Jinja для динамического формирования HTML
    страницы.
    📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
    содержать заголовок страницы, таблицу со списком пользователей и кнопку для
    добавления нового пользователя.
    📌 Создайте маршрут для отображения списка пользователей (метод GET).
    📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""

from typing import Optional, List
import uvicorn as uvicorn
from fastapi import FastAPI, Request, HTTPException, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class UserIn(BaseModel):
    name: str
    email: str
    password: str

class User(UserIn):
    id:int    

class UserOut(BaseModel):
    id:int    
    name: str
    email: str

fake_db = []
users = []
for i in range(10):
    fake_db.append(User(
                        id=i + 1,
                        name=f'name{i + 1}',
                        email=f'email{i + 1}@mail.ru',
                        password='123'
                        ))
users = fake_db.copy()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users":users})

@app.post("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users":users})    

@app.get("/users/id/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    current_user = None
    for i in range(0, len(users)):
        if users[i].id == user_id:
            user_out = UserOut(id=users[i].id, name=users[i].name, email=users[i].email)
            return user_out
    raise HTTPException(status_code=404, detail="user not found")

@app.post("/users/", response_model=UserOut)
async def create_user(new_user: UserIn):
    created_user = User(
                        id=len(users) + 1,
                        name=new_user.name,
                        email=new_user.email,
                        password=new_user.password,
                    )
    users.append(created_user)
    user_out = UserOut(id=created_user.id, name=created_user.name, email=created_user.email)
    return user_out


@app.put("/users/", response_model=User)
async def edit_user(user_id:int, new_user: UserIn):
    current_user = None
    for i in range(0, len(users)):
        if users[i].id == user_id:
            current_user = users[user_id - 1]
            current_user.name = new_user.name
            current_user.email = new_user.email
            current_user.password = new_user.password
            return current_user
    raise HTTPException(status_code=404, detail="user not found")


@app.delete("/users/", response_model=dict)
async def delete_user(user_id: int):
    for i in range(0, len(users)):
        if users[i].id == user_id:
            users.remove(users[i])
            return {"message": f"user {user_id} was deleted"}
    raise HTTPException(status_code=404, detail="user not found")


@app.get("/users/add_user", response_class=HTMLResponse)
async def add_user(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request})  

@app.post("/users/add_user", response_model=UserOut)
async def add_user_confirm(name=Form(), email=Form(), password=Form()):
    new_user = UserIn(name=name, email=email, password=password)
    if new_user:
        users.append(
            User(id=len(users) + 1, name=name, email=email,
                 password=password))
        return users[-1]
    raise HTTPException(status_code=404, detail="Cant create User")       

if __name__ == "__main__":
    uvicorn.run("hw_task_users:app", host="127.0.0.1", port=6000, reload=True)
