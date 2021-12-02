from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.models.models import Supplier
from .schemas import SuppllierSchema,ShowSuppllierSchemas
from sqlalchemy.orm import Session, query
from app.db.db import get_db


router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(suppllier:SuppllierSchema, db: Session= Depends(get_db)):
    db.add(Supplier(**suppllier.dict()))
    db.commit()


@router.get('/',response_model=List[ShowSuppllierSchemas])
def index(db: Session= Depends(get_db)):
    return db.query(Supplier).all()


@router.put('/{id}')
def update(id: int, suppller:SuppllierSchema,db: Session= Depends(get_db)):
    query = db.query(Supplier).filter_by(id=id)
    query.update(suppller.dict())
    db.commit()


@router.get('/{id}',response_model=ShowSuppllierSchemas)
def show(id: int,db: Session= Depends(get_db)):
    return db.query(Supplier).filter_by(id=id).filter()
    