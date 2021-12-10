from fastapi import Depends
from app.models.models import Ordem_status,Order,OrderProducts
from app.repositories.order_repository import OrderRepository, Ordem_status_Repository,OrderProducts_Repository
from app.repositories.produc_repository import ProductRepository
from app.services.product_discount_service import ProducDiscountService
from app.api.order.schemas import OrderSchema, OrderStatusSchema, OrderStatus ,OrderProducts_sum_Schema,creat_OrderProductSchema
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

    def create_order_products(self, id_order,list_products:list[OrderProducts_sum_Schema]):
        list(lambda x:
        self.orderProducts_Repository.create(OrderProducts(**creat_OrderProductSchema(
            id_order, x.product_id, x.quantity).dict())),list_products)
        

    def creat_order(self, input_order_schema: OrderSchema):
        #order_schema = OrderSchema()
        input_order_schema.number = self.order_number() #gerao numero da ordem
        input_order_schema.status = OrderStatus.ORDER_PLACED
        #order_schema.status = OrderStatus.ORDER_PLACED criar modelo
        input_order_schema.created_at = datetime.now()
        input_order_schema.payment_form_id #verificar
        input_order_schema.customer_id = self.get_customer_id(user.id)
        # order_schema.address_id = input_order_schema.address_id
        input_order_schema.value = self.get_products_value(input_order_schema.products) #valor total
        input_order_schema.total_discount = self.get_discount_value(input_order_schema.coupon_code, order_schema.total_value)
        #self.validate_address(order_schema.customer_id, order_schema.address_id) varificar outro lugar
        #self.order_repository.create(Order(**order_schema.dict())) criar
        id_order = self.order_repository.get_by_number(input_order_schema.number).id
        self.init_status_order(id_order) #iniciar ORDER_PLACED
        self.create_order_products(id_order,input_order_schema.list_products)
    