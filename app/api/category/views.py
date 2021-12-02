from typing import List
from fastapi import APIRouter,status
from fastapi import Depends
from fastapi.applications import FastAPI
from app.models.models import Category
from .schemas import CategorySchema, ShowCategorySchemas
from sqlalchemy.orm import Session, query
from app.db.db import get_db

router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(category:CategorySchema,db: Session = Depends(get_db)):
    db.add(Category(**category.dict()))
    db.commit()


@router.get('/',status_code=status.HTTP_200_OK,
response_model=List[ShowCategorySchemas])
def index(db:Session = Depends(get_db)):
    return db.query(Category).all()


@router.put('/{id}')
def update(id:int,category:CategorySchema,db:Session = Depends(get_db)):
    query = db.query(Category).filter_by(id=id)
    query.update(category.dict())


@router.get('/{id}', response_model=ShowCategorySchemas)
def show(id:int, db:Session = Depends(get_db)):
    return db.query(Category).filter_by(id=id).filter()
