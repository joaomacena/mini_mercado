from pydantic import BaseModel
from enum import Enum

class DiscountMode(str,Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'

class Product_discountSchema(BaseModel):
    mode:DiscountMode
    value:float
    product_id:int
    payment_method_id:int

class ShowProduct_discountSchema(Product_discountSchema):
    id:int

    class Config:
        orm_mode =True
