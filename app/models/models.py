from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, Integer, String, Float, DateTime
from app.db.db import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))


class Payment_method(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enabled = Column(Boolean, default=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    supplier = relationship(Supplier)


class Product_discount(Base):
    __tablename__ = "product_discounts"

    id = Column(Integer, primary_key=True)
    mode = Column(String(45))
    value = Column(Float())
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship(Product)
    payment_method_id = Column(Integer, ForeignKey("payment_methods.id"))
    payment_method = relationship(Payment_method)


class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True)
    expire_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    display_name = Column(String(100))
    email = Column(String(50))
    role = Column(String(10))
    password = Column(String(100))


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    fist_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45), unique=True)
    birth_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    Address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean, default=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship(Customer)


class Order(Base):
    __tablename__= "orders"

    id = Column(Integer, primary_key=True)
    number = Column(String(10))
    status =  Column(String(15))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship(Customer)
    created_at = Column(DateTime)
    address_id = Column(Integer, ForeignKey("addresses.id"))
    address = relationship(Address)
    value = Column(Float(10,2))# valor total
    payment_form_id = Column(Integer, ForeignKey("payment_methods.id")) # payment_method_id
    payment_form = relationship(Payment_method)
    total_discount = Column(Float(10,2))# valor total desconto 


class Ordem_status(Base):
    __tablename__ = "ordem_statuses"

    id = Column(Integer, primary_key=True)
    status =  Column(String(15))
    created_at = Column(DateTime)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship(Order)


class OrderProducts(Base):
    __tablename__ = 'order_products'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship(Order)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)
    quantity = Column(Integer)