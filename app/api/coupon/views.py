from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.models.models import Coupon
from .schemas import CouponSchema, ShowCouponSchema, UpdateCoupon
from app.repositories.coupon_repository import CouponRepository
from app.services.coupon_service import CouponService
from app.common.exceptions import CouponCodeAlreadyExistsException
from fastapi.exceptions import HTTPException
from app.services.auth_service import only_admin


router = APIRouter(dependencies=[Depends(only_admin)])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, service: CouponService = Depends()):
    try:
        service.create_coupon(Coupon(**coupon.dict()))
    except CouponCodeAlreadyExistsException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ShowCouponSchema])
def index(repository: CouponRepository = Depends()):
    return repository.get_all()


@router.put("/{id}")
def update(id: int, category: UpdateCoupon, repository: CouponRepository = Depends()):
    repository.update(id, category.dict())


@router.get("/{id}", response_model=ShowCouponSchema)
def show(id: int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)


@router.delete("/{id}")
def deletar(id: int, repository: CouponRepository = Depends()):
    return repository.remove(id)
