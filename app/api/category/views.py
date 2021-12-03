from typing import List
from fastapi import APIRouter,status
from fastapi import Depends
from fastapi.applications import FastAPI
from app.models.models import Category
from .schemas import CategorySchema, ShowCategorySchemas
from sqlalchemy.orm import Session, query
from app.db.db import get_db
from app.repositories.category_repository import CategoryRepository

router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(category:CategorySchema,repository:CategoryRepository = Depends()):
    repository.create(Category(**category.dict()))


@router.get('/',status_code=status.HTTP_200_OK,
response_model=List[ShowCategorySchemas])
def index(repository:CategoryRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,category:CategorySchema,repository:CategoryRepository = Depends()):
    repository.update(id,category.dict())


@router.get('/{id}', response_model=ShowCategorySchemas)
def show(id:int, repository:CategoryRepository = Depends()):
    return repository.get_by_id(id)
