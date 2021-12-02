from typing import List
from fastapi import APIRouter,status,Depends
from app.models.models import Product_discount
from .schemas import Product_discountSchema,ShowProduct_discountSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

from app.api.payment_methods import views
from fastapi.exceptions import HTTPException


router = APIRouter()

@router.post('/',status_code= status.HTTP_201_CREATED)
def create(product_discount:Product_discountSchema,db:Session = Depends(get_db)):
    payment_method = views.show(product_discount.payment_method_id,db)
    if payment_method.enabled :
        db.add(Product_discount(**product_discount.dict()))
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{payment_method.name} esta desativado e nao pode criar desconto')

    


@router.get('/',response_model=List[ShowProduct_discountSchema])
def index(db:Session = Depends(get_db)):
    return db.query(Product_discount).all()


@router.put('/{id}')
def update(id: int,product_discount:Product_discountSchema,db: Session = Depends(get_db)):
    query = db.query(Product_discount).filter_by(id=id)
    query.update(product_discount.dict())
    db.commit()


@router.get('/{id}', response_model=ShowProduct_discountSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Product_discountSchema).filter_by(id=id).first()