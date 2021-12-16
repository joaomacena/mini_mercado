from datetime import date
from pydantic import BaseModel
from app.api.user.schemas import UserSchemas_customer,ShowUserSchemas


class CustomerSchema(BaseModel):
    fist_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user_id: UserSchemas_customer


class UpdateCustomerSchema(BaseModel):
    fist_name: str
    last_name: str
    phone_number: str
    genre: str
    birth_date: date
    user_id: UserSchemas_customer

class ShowCustomerSchemas(BaseModel):
    id: int
    fist_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user_id: ShowUserSchemas

    class Config:
        orm_mode = True
