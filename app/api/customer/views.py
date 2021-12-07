from typing import List
from fastapi import APIRouter,status,Depends
from app.models.models import Customer
from app.repositories.customer_repository import CustomerRepository
from app.services.coupon_service import CouponService
from .schemas import ShowCustomerSchemas,CustomerSchema,UpdateCustomerSchema


router = APIRouter()


@router.post('/',status_code= status.HTTP_201_CREATED)
def create(customer: CustomerSchema, service: CustomerRepository = Depends()):
    service.create(Customer(**customer.dict()))


@router.get('/',response_model=List[ShowCustomerSchemas])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, customer :UpdateCustomerSchema,service: CustomerRepository = Depends()):
    service.update(id,customer.dict())


@router.get('/{id}', response_model=ShowCustomerSchemas)
def show(id: int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)
