from pydantic import BaseModel
from typing import  Optional


class UserSchemas_customer(BaseModel):
    display_name: str
    email: str
    password: str
    role ='customer'


class ShowUserSchemas(BaseModel):
    id:int
    display_name: str
    email: str
    role:str

    class Config:
        orm_mode = True