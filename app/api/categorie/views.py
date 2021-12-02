from typing import List
from fastapi import APIRouter,status
from fastapi import Depends
from fastapi.applications import FastAPI
from app.models.models import Categorie
from .schemas import CategorieSchema, ShowCategorieSchemas
from sqlalchemy.orm import Session, query
from app.db.db import get_db

router = FastAPI()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(categorie:CategorieSchema,db: Session = Depends(get_db)):
    db.add(Categorie(**categorie.dict()))
    db.commit()


@router.get('/',status_code=status.HTTP_200_OK,
response_model=List[ShowCategorieSchemas])
def index(db:Session = Depends(get_db)):
    return db.query(Categorie).all()


@router.put('/{id}')
def update(id:int,categorie:CategorieSchema,db:Session = Depends(get_db)):
    query = db.query(Categorie).filter_by(id=id)
    query.update(categorie.dict())


@router.get('/{id}', response_model=ShowCategorieSchemas)
def show(id:int, db:Session = Depends(get_db)):
    return db.query(Categorie).filter_by(id=id).filter()
