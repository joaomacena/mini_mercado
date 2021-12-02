from typing import List
from fastapi import APIRouter,status,Depends
from app.models.models import Payment_method
from .schemas import Payment_methodSchema,ShowPayment_methodSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()


@router.post('/',status_code= status.HTTP_201_CREATED)
def create(payment_method: Payment_methodSchema, db: Session = Depends(get_db)):
    db.add(Payment_method(**payment_method.dict()))
    db.commit()


@router.get('/',response_model=List[ShowPayment_methodSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Payment_method).all()


@router.put('/{id}')
def update(id: int,payment_method:Payment_methodSchema,db: Session = Depends(get_db)):
    query = db.query(Payment_method).filter_by(id=id)
    query.update(payment_method.dict())
    db.commit()


@router.get('/{id}', response_model=ShowPayment_methodSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Payment_method).filter_by(id=id).first()