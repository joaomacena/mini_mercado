from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Product_discount
from .base_repository import BaseRepository


class Product_discountRepository(BaseRepository):
    def __init__(self, session:Session = Depends(get_db)):
        super().__init__(session, Product_discount)

    def get_by_product_id(self,product_id:int):  
        return self.session.query(self.model).filter_by(product_id=product_id).all()