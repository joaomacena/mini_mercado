from fastapi import Depends
from app.models.models import Ordem_status,Order,OrderProducts
from app.repositories.order_repository import OrderRepository, Ordem_status_Repository,OrderProducts_Repository
from app.repositories.produc_repository import ProductRepository
from app.services.product_discount_service import ProducDiscountService
from app.api.order.schemas import OrderSchema, OrderStatusSchema, OrderStatus ,OrderProducts_sum_Schema
from datetime import datetime
#from fastapi.exceptions import HTTPException
#from app.common.exceptions import CouponCodeAlreadyExistsException
import random
result = random.sample(range(0,100), 4)

class OrderService:
    def __init__(self, orderRepository: OrderRepository = Depends(),
                ordem_status_Repository: Ordem_status_Repository = Depends(),
                orderProducts_Repository: OrderProducts_Repository = Depends(),
                productRepository:ProductRepository = Depends(),
                producDiscountService:ProducDiscountService = Depends()):
        self.orderRepository = orderRepository
        self.ordem_status_Repository = ordem_status_Repository
        self.orderProducts_Repository = orderProducts_Repository
        self.productRepository = productRepository
        self.producDiscountService = producDiscountService
    
    def order_number(self):
        n_order = random.sample(range(0,100), 5)
        return n_order

    # Da atualização do status: Só poderá ser feita pelo admin.
    #  Toda vez que o status for alterado, esse novo status deverá 
    #  ser salvo na tabela order_statuses. Para fins de histórico. 
    #  Os possíveis status são: ORDER PLACED, ORDED PAID, ORDER SHIPPED, 
    #  ORDER RECEIVED, ORDER COMPLETED, ORDER CANCELLED
    def criar_status(self, id_order , current_status:OrderStatus):
        self.ordem_status_Repository.create(**OrderStatusSchema(id_order,current_status,datetime.now()).dict())


    def update(self, id:int, order_status:OrderStatus):
        self.orderRepository.update(id,{'status':order_status})
        self.criar_status(id, order_status)

    #O status inicial da ordem deverá ser ORDER PLACED
    def init_status_order(self,id_order):
        self.criar_status(id_order,OrderStatus.ORDER_PLACED)


    # def next_status_order(self,id):
    #     pass
    
    def get_listProductsOrder(self,order_id):
        return self.orderProducts_Repository.get_by_order_id(order_id)

    def generate_total_value(self, order_id):
        listProducts_in_order:OrderProducts_sum_Schema = self.get_listProductsOrder(order_id)
        return print (sum(list(map(lambda x:x.quantity*
        self.productRepository.get_by_id(x.product_id).price,listProducts_in_order))))

    def generate_total_desconto(self, order_id, payment_form_id):
        listProducts_in_order:OrderProducts_sum_Schema = self.get_listProductsOrder(order_id)
        self.producDiscountService.get_productDiscounts(listProducts_in_order,payment_form_id)