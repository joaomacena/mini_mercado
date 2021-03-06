from fastapi import APIRouter
from fastapi.param_functions import Depends
from app.api.admin_user.schemas import Admin_UserSchemas
from app.models.models import User
from app.repositories.user_repository import UserRepository
import bcrypt

router = APIRouter()


@router.post("/")
def create(user: Admin_UserSchemas, repository: UserRepository = Depends()):
    user.password = bcrypt.hashpw(user.password.encode("utf8"), bcrypt.gensalt())
    repository.create(User(**user.dict()))
