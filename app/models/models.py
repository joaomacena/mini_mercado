from os import name
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String, Float, SmallInteger 
from app.db.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technnical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean , default=True)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Categorie(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Payment_method(Base):
    __tablename__ = 'Payment_methods'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enableb= Column(SmallInteger)