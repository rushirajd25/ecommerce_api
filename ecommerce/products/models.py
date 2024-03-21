from django.db import models

# Create your models here.

FEATURED_TYPE_CHOICES = [
    ("FP", "Featured product"),
    ("BS", "Best seller"),
    ("NA", "New arrival"),
]

MEDIA_TYPE_CHOICES = [
    ("IMG", "Image"),
    ("VID", "Video"),
]

class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    parent_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'({self.id}) {self.name}'
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(upload_to="product_media/")
    type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default='IMG')

class FeaturedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=FEATURED_TYPE_CHOICES)
