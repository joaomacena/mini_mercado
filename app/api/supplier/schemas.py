from pydantic import BaseModel


class SupplierSchema(BaseModel):
    name: str


class ShowSupplierSchemas(SupplierSchema):
    id: int

    class Config:
        orm_mode = True
