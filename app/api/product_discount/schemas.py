from pydantic import BaseModel
from enum import Enum
from app.api.product.schemas import ShowProductSchemas
from app.api.payment_methods.schemas import ShowPayment_methodSchema


class DiscountMode(str, Enum):
    VALUE = "value"
    PERCENTAGE = "percentage"


class Product_discountSchema(BaseModel):
    mode: DiscountMode
    value: float
    product_id: int
    payment_method_id: int  # 1


class ShowProduct_discountSchema(Product_discountSchema):
    id: int
    # product_id:ShowProductSchemas
    # payment_method_id:ShowPayment_methodSchema

    class Config:
        orm_mode = True
