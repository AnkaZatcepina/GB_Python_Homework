"""
    📌 Создать API для получения списка фильмов по жанру. Приложение должно
    иметь возможность получать список фильмов по заданному жанру.
    📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
    📌 Создайте класс Movie с полями id, title, description и genre.
    📌 Создайте список movies для хранения фильмов.
    📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
    📌 Реализуйте валидацию данных запроса и ответа.
"""
from enum import Enum
from typing import List
import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = []

class Genre(Enum):
    ACTION ='action'
    COMEDY ='comedy'
    HORROR ='horror'


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: Genre


class MovieIn(BaseModel):
    title: str
    description: str
    genre: Genre

fake_db = [
    Movie(id=1, title='Movie 1', description='Descr 1', genre=Genre.HORROR),
    Movie(id=2, title='Movie 2', description='Descr 2', genre=Genre.COMEDY),
    Movie(id=3, title='Movie 3', description='Descr 3', genre=Genre.COMEDY)
]
movies = fake_db.copy()

@app.get("/movies/", response_model=List[Movie])
async def get_all_movies():
    return movies

@app.post("/movies/", response_model=Movie)
async def create_movie(new_movie: MovieIn):
    movies.append(
        Movie(id=len(movies) + 1, title=new_movie.title, description=new_movie.description, genre=new_movie.genre)
    )
    return movies[-1]


@app.get("/movies/{genre}", response_model=List[Movie])
async def get_movies(genre: str):
    result = []
    for movie in movies:
        if movie.genre.value == genre:
            result.append(movie)
    if result:      
        return result
    raise HTTPException(status_code=404, detail="Genre not found")   


if __name__ == "__main__":
    uvicorn.run("task_2_movies:app", host="127.0.0.1", port=8000, reload=True)