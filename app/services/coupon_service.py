from datetime import datetime
from fastapi import Depends,status
from app.models.models import Coupon
from app.repositories.coupon_repository import CouponRepository
from app.api.coupon.schemas import ShowCouponSchema,UpdateCoupon
from app.common.exceptions import CouponCodeAlreadyExistsException

class CouponService:
    def __init__(self,couponRepository:CouponRepository= Depends()):
        self.couponRepository = couponRepository


    def is_exists_code(self,code):
        return self.couponRepository.filter({'code': code})
        

    def create_coupon(self, coupon:ShowCouponSchema):
        if  self.is_exists_code(coupon.code):
           self.couponRepository.create(Coupon(**coupon.dict()))
        else:
            raise CouponCodeAlreadyExistsException()



    
