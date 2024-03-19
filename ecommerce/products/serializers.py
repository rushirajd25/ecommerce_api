from rest_framework import serializers

from .models import Product, ProductMedia, FeaturedProduct

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    media = ProductMediaSerializer(source='productmedia_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class FeaturedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = FeaturedProduct
        fields = '__all__'