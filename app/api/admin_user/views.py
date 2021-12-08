from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from app.api.admin_user.schemas import Admin_UserSchemas, ShowAdmin_UserSchemas
from app.models.models import User
from app.repositories.user_repository import UserRepository
from app.services.admin_user_services import Admin_userService
from typing import List
from app.common.exceptions import Admin_userAlereadyExistsEmailException
from fastapi.exceptions import HTTPException


router = APIRouter()


@router.post("/")
def create(user: Admin_UserSchemas, services: Admin_userService = Depends()):
    try:
        services.create_admin_user(user)
    except Admin_userAlereadyExistsEmailException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)

@router.get("/", response_model=List[ShowAdmin_UserSchemas])
def index(repository: UserRepository = Depends()):
    return repository.get_all()


@router.put("/{id}")
def update(id: int, user: Admin_UserSchemas, services: Admin_userService = Depends()):
    try:
        services.update_admin_user(id, user)
    except Admin_userAlereadyExistsEmailException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/{id}", response_model=ShowAdmin_UserSchemas)
def show(id: int, repository: UserRepository = Depends()):
    return repository.get_by_id(id)


@router.delete("/{id}")
def deletar(id: int, repository: UserRepository = Depends()):
    return repository.remove(id)