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
    
    def is_enabled(self,discount):
        payment_method = self.payment_methodRepository.get_by_id(discount.payment_method_id) 
        productDiscount= self.product_discountRepository.get_by_product_id_and_pyment_method_id(discount.payment_method_id,discount.product_id)

        if payment_method.enabled :
            if not productDiscount :
                return  
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f'o pagemeto ja esta resitrado para este produto ')
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{payment_method.name} esta desativado e nao pode criar desconto')
    
         
    def create_discount(self, discount:Product_discountSchema):
        if self.is_enabled(discount):
           self.product_discountRepository.create(Product_discount(**discount.dict()))
           

    def update_discount(self,id:int,discount:Product_discountSchema):
       if self.is_enabled(discount):
            self.product_discountRepository.update(id,discount.dict())
       
