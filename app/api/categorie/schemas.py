from os import name
from pydantic import BaseModel


class CategorieSchema(BaseModel):
    name:str

class ShowCategorieSchemas(CategoriesSchema):
    id: int

    class Config:
        orm_mode = True