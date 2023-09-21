from fastapi import APIRouter, HTTPException
from db import products, database
from models.product import Product, ProductIn

router = APIRouter()

@router.get("/")
async def read_all_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == products_id)
    result = await database.fetch_one(query)  
    if result is None:
        raise HTTPException(status_code=404, detail='Product not found') 
    return result


@router.post("/", response_model=Product)
async def create_product(new_product: ProductIn):
    query = products.insert().values(name=new_product.name,
                                    description=new_product.description, 
                                    price=new_product.price)
    last_record_id = await database.execute(query)
    return {**new_product.dict(), "id": last_record_id}


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    if not await database.execute(query):
        raise HTTPException(status_code=404, detail="Product not found")
    return {**new_product.dict(), "id": product_id}


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    if not await database.execute(query):
        raise HTTPException(status_code=404, detail="Product not found")
    return {'message': f'Product {product_id} deleted'}   


@router.post("/fake_products/{count}")
async def create_fake_products(count: int):
    for i in range(count):
        query = products.insert().values(name=f'name{i}',
                                        description=f'description{i}',
                                        price=i)
        await database.execute(query)
    return {'message': f'{count} fake products created'}   