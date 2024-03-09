from django.contrib import admin
from .models import Product, FeaturedProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(FeaturedProduct)