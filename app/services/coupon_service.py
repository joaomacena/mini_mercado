from datetime import datetime
from fastapi import Depends, status
from app.models.models import Coupon
from app.repositories.coupon_repository import CouponRepository
from app.api.coupon.schemas import ShowCouponSchema, UpdateCoupon,CouponSchema
from app.common.exceptions import CouponCodeAlreadyExistsException


class CouponService:
    def __init__(self, couponRepository: CouponRepository = Depends()):
        self.couponRepository = couponRepository

    def is_exists_code(self, code):
        return self.couponRepository.filter({"code": code})

    def expiration_date(self,date):
        if date > datetime.now():
            return True
        return False
    
    #def id by codigo

    def discount_mode(self,type,value,value_total_order):
        if type=="percentage":
            return (value/100)*value_total_order
        return value


    def is_valid_coupon(self,coupon:CouponSchema,value_total_order):
        if self.expiration_date(coupon.coupon):
            if 1 >= coupon.limit:
                coupon.limit -= 1
                return self.discount_mode(coupon.type,coupon.value,value_total_order)



    def create_coupon(self, coupon: ShowCouponSchema):
        if self.is_exists_code(coupon.code):
            self.couponRepository.create(Coupon(**coupon.dict()))
        else:
            raise CouponCodeAlreadyExistsException()
