from datetime import date
from pydantic import BaseModel


class CustomerSchema(BaseModel):
    fist_name :str
    last_name :str
    phone_number :str
    genre :str
    document_id :str
    birth_date :date


class UpdateCustomerSchema(BaseModel):
    fist_name :str
    last_name :str
    phone_number :str
    genre :str
    birth_date :date


class ShowCustomerSchemas(CustomerSchema):
    id:int

    class Config:
        orm_mode = True
