import datetime

from pydantic import BaseModel, Field
from enum import Enum

class Status(Enum):
    CREATED ='created'
    IN_WORK ='in_work'
    PAID = 'paid'
    SHIPPED = 'shipped'
    DECLINED = 'declined'
    DONE = 'done'

class OrderIn(BaseModel):    
    user_id: int
    product_id: int
    order_date: datetime.date
    status: Status


class Order(OrderIn):
    id: int
