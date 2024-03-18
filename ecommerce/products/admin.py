from django.contrib import admin
from .models import Product, Media, FeaturedProduct

class MediaInline(admin.StackedInline):
    model = Media

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Media)
admin.site.register(FeaturedProduct)