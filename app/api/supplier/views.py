from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.models.models import Supplier
from .schemas import SupplierSchema,ShowSupplierSchemas
from app.repositories.supplier_repository import SupplierRepository


router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(suppllier:SupplierSchema, repoistory: SupplierRepository = Depends()):
    repoistory.create(Supplier(**suppllier.dict()))


@router.get('/',response_model=List[ShowSupplierSchemas])
def index(repoistory: SupplierRepository= Depends()):
    return repoistory.get_all()


@router.put('/{id}')
def update(id: int, suppller:SupplierSchema,repoistory: SupplierRepository= Depends()):
    repoistory.update(id,suppller.dict())
    
    
@router.get('/{id}',response_model=ShowSupplierSchemas)
def show(id: int, repoistory: SupplierRepository= Depends()):
    return repoistory.get_by_id(id)
    