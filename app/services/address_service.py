from fastapi import Depends
from app.models.models import Address
from app.repositories.address_repository import AddressRepository
from app.api.address.schemas import AddressSchema
from fastapi.exceptions import HTTPException
from app.common.exceptions import CouponCodeAlreadyExistsException


class AddressService:
    def __init__(self, addressRepository: AddressRepository = Depends()):
        self.addressRepository = addressRepository

    def validate_address(self):
        pass

    def switch_to_false_address(self, address):
        old_address = self.addressRepository.is_primary(
            address.customer_id, address.primary)
            
        if address.primary and old_address:
            self.addressRepository.update(old_address.id, {'primary': False})

    def create_address(self, address: AddressSchema):
        self.switch_to_false_address(address)
        self.addressRepository.create(Address(**address.dict()))

    def update_addres(self, address: AddressSchema):
        self.switch_to_false_address(address)
