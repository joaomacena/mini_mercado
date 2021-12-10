from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from app.api.product.schemas import ShowProductSchemas


class OrderProducts_sum_Schema(BaseModel): 
    product_id = ShowProductSchemas
    quantity:int

class OrderSchema(BaseModel):
    number :str
    status ='ORDER PLACED'
    #customer_id = Column(Integer, ForeignKey("customers.id"))
    customer_id:int
    created_at:datetime
    #address_id = Column(Integer, ForeignKey("addresses.id"))
    address_id:int
    value:float# valor total
    payment_form_id: int
    total_discount:float#

class OrderStatus(str, Enum):
    ORDER_CANCELLED = 'order_cancelled'
    ORDER_COMPLETED = 'order_completed'
    ORDER_RECEIVED = 'order_received'
    ORDER_PLACED = 'order_placed'
    ORDER_PAID = 'order_paid'
    ORDER_SHIPPED = 'order_shipped'

class OrderStatusSchema:
    def __init__(self,order_id: int, status:OrderStatus, created_at: datetime):
        self.order_id = order_id
        self.status = status
        self.created_at = created_at
