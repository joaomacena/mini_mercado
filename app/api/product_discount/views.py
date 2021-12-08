from typing import List
from fastapi import APIRouter, status, Depends
from app.models.models import Product_discount
from .schemas import Product_discountSchema, ShowProduct_discountSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.services.product_discount_service import ProducDiscountService
from app.repositories.product_discount_repository import Product_discountRepository
from app.services.auth_service import only_admin


router = APIRouter(dependencies=[Depends(only_admin)])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    product_discount: Product_discountSchema,
    services: ProducDiscountService = Depends(),
):
    services.create_discount(product_discount)


@router.get("/", response_model=List[ShowProduct_discountSchema])
def index(repository: Product_discountRepository = Depends()):
    return repository.get_all()


@router.put("/{id}")
def update(
    id: int, product_discount: Product_discountSchema, services: ProducDiscountService = Depends()):
    services.update_discount(id,product_discount)


@router.get("/{id}", response_model=ShowProduct_discountSchema)
def show(id: int, repository: Product_discountRepository = Depends()):
    return repository.get_by_id(id)
