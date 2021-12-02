from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String, Float, SmallInteger 
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
