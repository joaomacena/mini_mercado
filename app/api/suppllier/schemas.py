from pydantic import BaseModel


class SuppllierSchema(BaseModel):
    name : str


class ShowSuppllierSchemas(SuppllierSchema):
    id : int

    class Config:
        orm_mode = True
