from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(
        ProductCategory,
        related_name='products',
        on_delete=models.CASCADE)