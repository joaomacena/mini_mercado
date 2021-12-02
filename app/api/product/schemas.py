from pydantic import BaseModel


class ProductSchema(BaseModel):
    description :str
    price: float
    technnical_details:str
    image: str
    visible: bool

class ShowProductSchemas(ProductSchema):
    id:int

    class Config:
        orm_mode = True