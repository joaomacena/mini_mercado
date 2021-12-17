from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.db import get_db
from app.models.models import Base, Category, Supplier, User ,Payment_method,Product,Product_discount, Address,Customer
from app.app import app
import pytest
import factory


@pytest.fixture()
def db_session():
    engine = create_engine('sqlite:///./test.db',
                           connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    db = Session()
    yield db
    db.close()


@pytest.fixture()
def override_get_db(db_session):
    def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    return client


@pytest.fixture()
def user_factory(db_session):
    class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = User
            sqlalchemy_session = db_session

        id = None
        display_name = factory.Faker('name')
        email = factory.Faker('email')
        role = None
        password = '$2b$12$2F.MmED.HUKwVq74djSzguVYu4HBYEkKYNqxRnc/.gVG24QyYcC9m'
    

    return UserFactory


@pytest.fixture()
def category_factory(db_session):
    class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Category
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return CategoryFactory


@pytest.fixture()
def supplier_factory(db_session):
    class SupplierFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Supplier
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return SupplierFactory


@pytest.fixture()
def payment_method_factory(db_session):
    class Payment_methodFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Payment_method
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')
        enabled = True

    return Payment_methodFactory


@pytest.fixture()
def product_factory(db_session,supplier_factory,category_factory):
    class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Product
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        description = factory.Faker('word')
        price = factory.Faker('pyint')
        technical_details = factory.Faker('word')
        visible = True
        category = factory.SubFactory(category_factory)
        supplier = factory.SubFactory(supplier_factory)

    return ProductFactory


@pytest.fixture()
def product_discount_factory(db_session,product_factory,payment_method_factory):
    class Product_discount_Factory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Product_discount
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        mode = 'value'
        product = factory.SubFactory(product_factory)
        payment_method = factory.SubFactory(payment_method_factory)
        
        
    return Product_discount_Factory


@pytest.fixture()
def customer_factory(db_session,):
    class Customer_Factory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Customer
            sqlalchemy_session = db_session

        id = factory.sequence(int)
        fist_name = factory.Faker('first_name')
        last_name = factory.Faker('last_name')
        phone_number = factory.Faker('phone_number')
        genre = factory.Faker('word')
        document_id = factory.Faker('pyint')
        birth_date = factory.Faker('date_between_dates')
        user_id = factory.Faker('pyint')
        
        
    return Customer_Factory


# @pytest.fixture()
# def address_factory(db_session,user_factory):
#     class Address_discount_Factory(factory.alchemy.SQLAlchemyModelFactory):
#         class Meta:
#             model = Address
#             sqlalchemy_session = db_session

#         id = factory.Faker('pyint')
#         Address = factory.Faker('word')
#         city = factory.Faker('city')
#         state = factory.Faker('country_code')
#         number = factory.Faker('building_number')
#         zipcode = factory.Faker('postcode')
#         neighbourhood = factory.Faker('current_country')
#         primary = True
#         #customer = )
        
#     return Address_discount_Factory


@pytest.fixture()
def user_admin_token(user_factory):
    user_factory(role='admin')

    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjY1NDIwODc0fQ.o_syoOwrg8VOvl5nWYnA0waXxL0pFLdUgJY8HoqMVjM'


@pytest.fixture()
def admin_auth_header(user_admin_token):
    return {'Authorization': f'Bearer {user_admin_token}'}


