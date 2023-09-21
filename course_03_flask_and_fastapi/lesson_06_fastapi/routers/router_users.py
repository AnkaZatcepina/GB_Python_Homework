from typing import List
from fastapi import APIRouter, HTTPException
from db import users, database
from models.user import UserOut, UserIn

router = APIRouter()

@router.get("/", response_model=List[UserOut])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@router.get("/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    result = await database.fetch_one(query)  
    if result is None:
        raise HTTPException(status_code=404, detail='User not found') 
    return result  
  

@router.post("/", response_model=UserOut)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}      

@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, changed_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**changed_user.dict())
    await database.execute(query)
    return {**changed_user.dict(), "id": user_id}

@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    if not await database.execute(query):
        raise HTTPException(status_code=404, detail="User not found")
    return {'message': f'User {user_id} deleted'}   

@router.post("/fake_users/{count}")
async def create_fake_user(count: int):
    for i in range(count):
        query = users.insert().values(username=f'user{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users created'}