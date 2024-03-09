from rest_framework import serializers

from .models import Product, FeaturedProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'category'
        ]

class FeaturedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = FeaturedProduct
        fields = ['type', 'product']