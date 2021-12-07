from pydantic import BaseModel
from app.api.customer.schemas import ShowCustomerSchemas

class AddressSchema(BaseModel):
    Address:str
    city:str
    state:str
    number:str
    zipcode:str
    neighbourhood:str
    primary:bool
    customer_id:int

class ShowAddressSchemas(AddressSchema):
    id : int
    customer_id: int

    class Config:
        orm_mode = True
