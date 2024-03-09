from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, FeaturedProductViewSet

router = DefaultRouter()
router.register(r'products', viewset=ProductViewSet, basename='product')
router.register(r'featured_products', viewset=FeaturedProductViewSet, basename='featured_product')

urlpatterns = [
    path('', include(router.urls)),
]