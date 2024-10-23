from django.forms import ModelForm
from .models import ProductCategory, Product

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category_id']