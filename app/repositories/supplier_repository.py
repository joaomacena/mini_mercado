from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.db import get_db
from app.models.models import Supplier
from .base_repository import BaseRepository


class SupplierRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Supplier)
