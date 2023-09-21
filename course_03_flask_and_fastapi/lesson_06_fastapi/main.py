import uvicorn
from fastapi import FastAPI
from db import database
from routers import router_users
from fastapi.testclient import TestClient


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router_users.router, prefix="/users", tags=["users"])



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
