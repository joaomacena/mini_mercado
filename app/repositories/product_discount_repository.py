from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Product_discount
from .base_repository import BaseRepository
from app.api.product_discount.schemas import Product_discountSchema


class Product_discountRepository(BaseRepository):
    def __init__(self, session:Session = Depends(get_db)):
        super().__init__(session, Product_discount)

    def get_by_product_id_and_pyment_method_id(self,payment_method_id,product_id):  
        return self.session.query(self.model).filter_by(product_id=product_id, payment_method_id=payment_method_id).first()