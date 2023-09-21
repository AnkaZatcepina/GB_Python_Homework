from pydantic import BaseModel, Field

class ProductIn(BaseModel):
    name: str = Field(max_length=40)
    description: str = Field(max_length=256)
    price: int

class Product(ProductIn):
    id: int
