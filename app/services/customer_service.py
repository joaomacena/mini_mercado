from fastapi.param_functions import Depends
from app.api.admin_user.schemas import ShowAdmin_UserSchemas
from app.repositories.customer_repository import CustomerRepository
from app.repositories.user_repository import UserRepository
from app.services.admin_user_services import Admin_userService
from app.api.customer.schemas import CustomerSchema
from app.models.models import Customer

class CustomerService :
    def __init__(self,customerRepository:CustomerRepository = Depends(),
                userRepository:UserRepository = Depends(),
                admin_userService: Admin_userService = Depends()):
        self.customerRepository = customerRepository
        self.userRepository = userRepository
        self.admin_userService = admin_userService
    
    


    def create_customer(self,customer:CustomerSchema):
        self.admin_userService.create_admin_user(customer.user_id)
        user_create = self.userRepository.find_by_email(customer.user_id.email)
        customer.user_id = user_create.id
        self.customerRepository.create(Customer(**customer.dict()))
    

    def update_customer(self,id,customer:CustomerSchema): #finalizar
        self.admin_userService.create_admin_user(customer.user_id)
        user_create = self.userRepository.find_by_email(customer.user_id.email)
        customer.user_id = user_create.id
        self.customerRepository.create(Customer(**customer.dict()))