from django.forms import ModelForm
from .models import ProductCategory, Product

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']