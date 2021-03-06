from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.models.models import Address
from app.services.auth_service import only_admin
from .schemas import AddressSchema, ShowAddressSchemas
from app.repositories.address_repository import AddressRepository
from app.services.address_service import AddressService
from fastapi.exceptions import HTTPException


router = APIRouter(dependencies=[Depends(only_admin)])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model = ShowAddressSchemas)
def create(address: AddressSchema, service: AddressService = Depends()):
    return service.create_address(address)


@router.get("/", response_model=List[ShowAddressSchemas])
def index(repoistory: AddressRepository = Depends()):
    return repoistory.get_all()


@router.put("/{id}", status_code = status.HTTP_200_OK, response_model = ShowAddressSchemas)
def update(id: int, address: AddressSchema, service: AddressService = Depends()):
    return service.update_addres(id, address)


@router.get("/{id}", response_model=ShowAddressSchemas)
def show(id: int, repoistory: AddressRepository = Depends()):
    return repoistory.get_by_id(id)


@router.delete("/{id}")
def deletar(id: int, repository: AddressRepository = Depends()):
    return repository.remove(id)
