import datetime
import random

from fastapi import APIRouter
from db import products, database, orders, users
from models.order import Order, OrderIn, Status

router = APIRouter()

@router.get("/")
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)

@router.post("/", response_model=Order)
async def create_order(new_order: OrderIn):
    query = orders.insert().values(user_id=new_order.user_id, 
                                    product_id=new_order.product_id,
                                    order_date=datetime.date.today(),
                                    status=new_order.status.value)
    last_record_id = await database.execute(query)
    return {**new_order.dict(), "id": last_record_id}


@router.put("/{order_id}", response_model=Order)
async def update_order(order_id, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(
        user_id=new_order.user_id, 
        product_id=new_order.product_id,                                    
        status=new_order.status.value,
        order_date=datetime.date.today())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}

@router.delete("/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': f'Order {order_id} deleted'}

@router.post("/fake_orders/{count}", response_model=dict())
async def create_fake_order(count: int):
    users_query = users.select()
    users_list = await database.fetch_all(users_query)
    products_query = products.select()
    products_list = await database.fetch_all(products_query)
    for _ in range(count):
        user=random.choice(users_list) 
        product=random.choice(products_list)
        query = orders.insert().values(
            user_id=int(user[0]),
            product_id=int(product[0]),
            order_date=datetime.date.today(),
            status=Status.CREATED.value)
        print(query)                               
        await database.execute(query)
    return {'message': f'{count} fake orders created'}

