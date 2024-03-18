from rest_framework import serializers

from .models import Product, Media, FeaturedProduct

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    media = MediaSerializer(source='media_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class FeaturedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = FeaturedProduct
        fields = '__all__'