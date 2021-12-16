from fastapi import Depends
from app.models.models import Ordem_status,Order,OrderProducts
from app.repositories.order_repository import OrderRepository, Ordem_status_Repository,OrderProducts_Repository
from app.repositories.produc_repository import ProductRepository
from app.services.product_discount_service import ProducDiscountService
from app.api.order.schemas import  OrderStatusSchema, OrderStatus ,OrderProducts_sum_Schema,creat_OrderProductSchema,creat_OrderSchema
from datetime import datetime
#from fastapi.exceptions import HTTPException
#from app.common.exceptions import CouponCodeAlreadyExistsException
import random
class OrderSchema_Dto:
    def __init__(self,number,status,customer_id,created_at,address_id,value,payment_form_id,total_discount):
        self.number = number
        self.status = status
        self.customer_id = customer_id
        self.created_at = created_at
        self.address_id = address_id
        self.value = value
        self.payment_form_id = payment_form_id
        self.total_discount = total_discount
        
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
        n_order = 9999
        return n_order

    
    def criar_status(self, id_order , current_status:OrderStatus):
        self.ordem_status_Repository.create(**OrderStatusSchema(id_order,current_status,datetime.now()).dict())


    def update(self, id:int, order_status:OrderStatus):
        self.orderRepository.update(id,{'status':order_status})
        return self.criar_status(id, order_status)

    #O status inicial da ordem deverá ser ORDER PLACED
    def init_status_order(self,id_order):
        return self.criar_status(id_order,OrderStatus.ORDER_PLACED)


    # def next_status_order(self,id):
    #     pass
    

    # def get_listProductsOrder(self,order_id):
    #     return self.orderProducts_Repository.get_by_order_id(order_id)


    def generate_total_value(self, list_products):
        return sum(list(map(lambda x:x.quantity* 
        self.productRepository.get_by_id(x.product_id).price,list_products)))


    def generate_total_desconto(self, list_products, payment_form_id):
        return self.producDiscountService.get_productDiscounts(list_products,payment_form_id)


    def create_order_products(self, id_order,list_products:list[OrderProducts_sum_Schema]):
        return list(lambda x:
        self.orderProducts_Repository.create(OrderProducts(**creat_OrderProductSchema(
            id_order, x.product_id, x.quantity).dict())),list_products)
    

    def creat_order(self, input_order_schema: creat_OrderSchema):
        
        number = self.order_number() #gerao numero da ordem
        status = OrderStatus.ORDER_PLACED
        #order_schema.status = OrderStatus.ORDER_PLACED criar modelo
        #order_schema.created_at = datetime.now()
        #order_schema.payment_form_id = input_order_schema.payment_form_id #verificar
        #order_schema.customer_id = 3
        # order_schema.address_id = input_order_schema.address_id
        value = self.generate_total_value(input_order_schema.list_products) #valor total
        total_discount = self.generate_total_desconto(input_order_schema.list_products,
        input_order_schema.payment_form_id)
        #self.validate_address(order_schema.customer_id, order_schema.address_id) #varificar outro lugar
        order_schema = OrderSchema_Dto(number,status,3,datetime.now(),
            input_order_schema.address_id,value,input_order_schema.payment_form_id,total_discount)
        self.orderRepository.create(Order(**order_schema.__dict__)) 
        # id_order = self.order_repository.get_by_number(order_schema.number).id
        # self.init_status_order(id_order) #iniciar ORDER_PLACED
        # self.create_order_products(id_order,input_order_schema.list_products)
    

    