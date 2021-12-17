from fastapi import Depends
from app.models.models import Address
from app.repositories.address_repository import AddressRepository
from app.api.address.schemas import AddressSchema
from app.common.exceptions import AddressAlereadyExistsCustomerException


class AddressService:
    def __init__(self, addressRepository: AddressRepository = Depends()):
        self.addressRepository = addressRepository

    def validate_address(self,Address_id,customer_id_byoder):
        Address = self.addressRepository.get_by_id(Address_id)
        if not Address.customer_id == customer_id_byoder:
            raise AddressAlereadyExistsCustomerException()
        return True

    def switch_to_false_address(self, address):
        old_address = self.addressRepository.is_primary(
            address.customer_id, address.primary)
            
        if address.primary and old_address:
            self.addressRepository.update(old_address.id, {'primary': False})

    def create_address(self, address: AddressSchema):
        self.switch_to_false_address(address)
        return self.addressRepository.create(Address(**address.dict()))

    def update_addres(self, id, address: AddressSchema):
        self.switch_to_false_address(address)
        return self.addressRepository.update(id,address.dict())
