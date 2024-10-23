from django.contrib import admin
from .models import ProductCategory, Product
# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    ordering = ('id', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_id')
    search_fields = ('name', 'category_id')
    ordering = ('price', )