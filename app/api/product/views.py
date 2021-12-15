from typing import List
from fastapi import APIRouter, status, Depends
from app.models.models import Product
from app.repositories.produc_repository import ProductRepository
from .schemas import ProductSchema, ShowProductSchemas
from app.services.auth_service import only_admin


router = APIRouter(dependencies=[Depends(only_admin)])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowProductSchemas)
def create(product: ProductSchema, repository: ProductRepository = Depends()):
    return repository.create(Product(**product.dict()))


@router.get("/", response_model=List[ShowProductSchemas])
def index(repository: ProductRepository = Depends()):
    return repository.get_all()


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=ShowProductSchemas)
def update(id: int, product: ProductSchema, repository: ProductRepository = Depends()):
    return repository.update(id, product.dict())


@router.get("/{id}", response_model=ShowProductSchemas)
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)
