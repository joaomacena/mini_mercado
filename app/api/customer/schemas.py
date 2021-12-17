from datetime import date
from pydantic import BaseModel
from app.api.user.schemas import UserSchemas_customer,ShowUserSchemas


class UserSchema(BaseModel):
    email: str
    password: str
    display_name: str


class CustomerSchema(BaseModel):
    fist_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user: UserSchemas_customer


class UpdateUserSchema(UserSchema):
    id:int


class UpdateCustomerSchema(BaseModel):
    fist_name: str
    last_name: str
    phone_number: str
    genre: str
    birth_date: date
    user: UpdateUserSchema


class ShowCustomerSchemas(BaseModel):
    id: int
    fist_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user: ShowUserSchemas

    class Config:
        orm_mode = True
