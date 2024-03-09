from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, FeaturedProduct
from .serializers import ProductSerializer, FeaturedProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FeaturedProductViewSet(viewsets.ModelViewSet):
    queryset = FeaturedProduct.objects.filter(type__exact='FP')
    serializer_class = FeaturedProductSerializer
