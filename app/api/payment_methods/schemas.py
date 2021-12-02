from pydantic import BaseModel


class Payment_methodSchema(BaseModel):
    name :str
    enabled:int

class ShowPayment_methodSchema(Payment_methodSchema):
    id:int

    class Config:
        orm_mode = True
