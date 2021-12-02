from pydantic import BaseModel
from app.api.category.schemas import ShowCategorySchemas
from app.api.supplier.schemas import ShowSupplierSchemas

class ProductSchema(BaseModel):
    description :str
    price: float
    technnical_details:str
    image: str
    visible: bool
    category_id: int
    supplier_id: int

class ShowProductSchemas(ProductSchema):
    id:int
    category:ShowCategorySchemas
    supplier:ShowSupplierSchemas

    class Config:
        orm_mode = True