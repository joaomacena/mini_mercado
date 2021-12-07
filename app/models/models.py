from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, Integer, String, Float, DateTime
from app.db.db import Base


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Payment_method(Base):
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enabled= Column(Boolean , default=True)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technnical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean , default=True)
    category_id = Column(Integer,ForeignKey('categories.id'))
    category = relationship(Category)
    supplier_id = Column(Integer,ForeignKey('suppliers.id'))
    supplier = relationship(Supplier)
    

class Product_discount(Base):
    __tablename__ = 'product_discounts'

    id = Column(Integer,primary_key=True)
    mode = Column(String(45))
    value = Column(Float())
    product_id = Column(Integer,ForeignKey('products.id'))
    payment_method_id = Column(Integer,ForeignKey('payment_methods.id'))


class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer,primary_key=True)
    code = Column(String(10),unique=True)
    expire_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float())


class Customer(Base):
    __tablename__='Customers'

    id = Column(Integer,primary_key=True)
    fist_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45),unique=True)
    birth_date = Column(Date)
    #user id


class Address(Base):
    __tablename__='Addresses'

    id = Column(Integer,primary_key=True)
    Address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean , default=True)
    customer_id = Column(Integer,ForeignKey('Customers.id'))
    customer = relationship(Customer)