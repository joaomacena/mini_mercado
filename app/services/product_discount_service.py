from fastapi import Depends,status
from app.models.models import Product_discount
from app.repositories.payment_method_repository import Payment_methodRepository
from app.repositories.product_discount_repository import Product_discountRepository
from app.api.product_discount.schemas import Product_discountSchema
from fastapi.exceptions import HTTPException

class ProducDiscountService:
    def __init__(self, payment_methodRepository:Payment_methodRepository=Depends(),
                product_discountRepository:Product_discountRepository=Depends()):
        self.payment_methodRepository = payment_methodRepository
        self.product_discountRepository = product_discountRepository
    
    #def is_enabled(self,discount_payment_method_id):
    
    def create_discount(self, discount:Product_discountSchema):
        payment_method = self.payment_methodRepository.get_by_id(discount.payment_method_id) 
        productDiscount_by_product_id= self.product_discountRepository.get_by_product_id(discount.product_id)
        #print(list(productDiscount_by_product_id))
        if payment_method.enabled and discount.payment_method_id :
            self.product_discountRepository.create(Product_discount(**discount.dict()))
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'{payment_method.name} esta desativado e nao pode criar desconto')

    
    def update_discount(self,id:int,discount:Product_discountSchema):
        payment_method = self.payment_methodRepository.get_by_id(discount.payment_method_id)
        if payment_method.enabled:
            self.product_discountRepository.update(id,discount.dict())
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'{payment_method.name} esta desativado e nao pode criar desconto')

