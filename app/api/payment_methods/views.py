from typing import List
from fastapi import APIRouter, status, Depends
from app.models.models import Payment_method
from .schemas import Payment_methodSchema, ShowPayment_methodSchema
from app.repositories.payment_method_repository import Payment_methodRepository
from app.services.auth_service import only_admin


router = APIRouter(dependencies=[Depends(only_admin)])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    payment_method: Payment_methodSchema,
    repository: Payment_methodRepository = Depends(),
):
    repository.create(Payment_method(**payment_method.dict()))


@router.get("/", response_model=List[ShowPayment_methodSchema])
def index(repository: Payment_methodRepository = Depends()):
    return repository.get_all()


@router.put("/{id}")
def update(
    id: int,
    payment_method: Payment_methodSchema,
    repository: Payment_methodRepository = Depends(),
):
    repository.update(id, payment_method.dict())


@router.get("/{id}", response_model=ShowPayment_methodSchema)
def show(id: int, repository: Payment_methodRepository = Depends()):
    return repository.get_by_id(id)
