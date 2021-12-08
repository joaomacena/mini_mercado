from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.db import get_db
from .base_repository import BaseRepository
from app.models.models import Coupon


class CouponRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Coupon)
