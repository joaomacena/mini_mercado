from pydantic import BaseModel


class Admin_UserSchemas(BaseModel):
    display_name: str
    email: str
    password: str
    role = 'admin'

class ShowAdmin_UserSchemas(BaseModel):
    id:int
    display_name: str
    email: str
    role:str

    class Config:
        orm_mode = True