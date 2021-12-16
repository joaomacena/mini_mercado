from typing import List
from fastapi import APIRouter, status, Depends
from app.models.models import Product_discount
from .schemas import Product_discountSchema, ShowProduct_discountSchema
from app.services.product_discount_service import ProducDiscountService
from app.repositories.product_discount_repository import Product_discountRepository
from app.services.auth_service import only_admin
from app.common.exceptions import PaymentMethodDiscountAlreadyExistsException,PaymentMethodsNotAvailableException
from fastapi.exceptions import HTTPException

router = APIRouter(dependencies=[Depends(only_admin)])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(product_discount: Product_discountSchema,
             services: ProducDiscountService = Depends()):
    try:
        return services.create_discount(product_discount)
    except PaymentMethodDiscountAlreadyExistsException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
         detail=msg.message)
    except PaymentMethodsNotAvailableException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
         detail=msg.message)



@router.get("/", response_model=List[ShowProduct_discountSchema])
def index(repository: Product_discountRepository = Depends()):
    return repository.get_all()


@router.put("/{id}")
def update(id: int, product_discount: Product_discountSchema,
            services: ProducDiscountService = Depends()):
    return services.update_discount(id,product_discount)


@router.get("/{id}", response_model=ShowProduct_discountSchema)
def show(id: int, repository: Product_discountRepository = Depends()):
    return repository.get_by_id
