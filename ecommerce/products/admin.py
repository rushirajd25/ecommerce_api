from django.contrib import admin
from .models import Product, ProductCategory, ProductMedia, FeaturedProduct

class ProductMediaInline(admin.StackedInline):
    model = ProductMedia

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductMediaInline,
    ]

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductMedia)
admin.site.register(FeaturedProduct)