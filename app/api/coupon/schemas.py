from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class CouponMode(str,Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'


class CouponSchema(BaseModel):
    code:str
    expire_at:datetime
    limit:int
    type:CouponMode
    value:float


class UpdateCoupon(BaseModel): #tarefa 4- 3 limit e expire_at 
    limit:int
    expire_at:datetime


class ShowCouponSchema(CouponSchema):
    id: int

    class Config:
        orm_mode =True
