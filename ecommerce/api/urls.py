from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', viewset=ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]