from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from rl_app.models import ProductCategory, Product
from .forms import ProductCategoryForm

# Create your views here.

class IndexView(View):
    def get(delf, request, *args, **kwargs):
        return render(request, 'rl_app/index.html')
    
class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'rl_app/productcategory_list.html'

class ProductCategoryDetailView(DetailView):
    model = ProductCategory
    pk_url_kwarg = 'productcategory_id'
    template_name = 'rl_app/productcategory_detail.html'
    
class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'rl_app/product_detail.html'

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'rl_app/productcategory_create.html'
    success_url = reverse_lazy('rl_app:productcategory_list')