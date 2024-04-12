from django.contrib import admin
from .models import Attribute, AttributeGroup
from .models import Product, ProductAttribute, ProductCategory, ProductMedia, FeaturedProduct

class ProductMediaInline(admin.StackedInline):
    model = ProductMedia

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductMediaInline,
    ]

# Register your models here.
admin.site.register(Attribute)
admin.site.register(AttributeGroup)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductAttribute)
admin.site.register(ProductMedia)
admin.site.register(FeaturedProduct)