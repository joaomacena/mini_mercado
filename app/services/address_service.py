from fastapi import Depends
from app.models.models import Address
from app.repositories.address_repository import AddressRepository
from app.api.address.schemas import AddressSchema
from fastapi.exceptions import HTTPException
from app.common.exceptions import CouponCodeAlreadyExistsException

class AddressService:
    def __init__(self, addressRepository:AddressRepository=Depends()):
        self.addressRepository = addressRepository

    def is_primary(self,customer_id):
       return self.addressRepository.get_by_product_id_and_pyment_method_id()

    def create_address(self,address:AddressSchema):
        old_address = self.addressRepository.get_by_product_id_and_pyment_method_id(address.customer_id, address.primary)
        print(old_address)
        if address.primary == True and old_address:
            print(123)
            self.addressRepository.update(old_address.id,{'primary':False})
        self.addressRepository.create(Address(**address.dict()))    
            