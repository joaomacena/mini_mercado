from fastapi import APIRouter, status, Depends
from app.api.order.schemas import OrderSchema, OrderStatus
from app.models.models import User
from app.services.auth_service import only_admin,only_customer
from app.services.order_service import OrderService

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/')
def create(input_order_schema: OrderSchema, service: OrderService = Depends()):
    service.generate_total_desconto(1,1)

@router.put('/{id}')
def update(id: int, order_status: OrderStatus, service: OrderService = Depends()):
    service.update(id,order_status)