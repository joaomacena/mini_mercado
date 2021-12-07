from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.models.models import Address
from .schemas import AddressSchema,ShowAddressSchemas
from app.repositories.address_repository import AddressRepository
from app.services.address_service import AddressService
from fastapi.exceptions import HTTPException
from app.common.exceptions import AddressAlereadyExistsPrimaryException


router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(address:AddressSchema, service: AddressService = Depends()):
    service.create_address(address)
    
@router.get('/',response_model=List[ShowAddressSchemas])
def index(repoistory: AddressRepository= Depends()):
    return repoistory.get_all()


@router.put('/{id}')
def update(id: int, address:AddressSchema,repoistory: AddressRepository= Depends()):
    repoistory.update(id,address.dict())
    
    
@router.get('/{id}',response_model=ShowAddressSchemas)
def show(id: int, repoistory: AddressRepository= Depends()):
    return repoistory.get_by_id(id)
    

@router.delete('/{id}')
def deletar(id:int,repository:AddressRepository= Depends()):
    return repository.remove(id) 