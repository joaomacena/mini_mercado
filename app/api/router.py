from fastapi import APIRouter
from .product.views import router as product_router
from .suppllier.views import router as suppllier_router
from .categorie.views import router as categorie
from .payment_methods.views import router as payment_method

router = APIRouter()

router.include_router(product_router, prefix='/product')

router.include_router(suppllier_router, prefix='/suppllier')

router.include_router(categorie, prefix='/categorie')

router.include_router(payment_method, prefix='/payment_method')