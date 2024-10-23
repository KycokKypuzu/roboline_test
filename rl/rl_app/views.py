from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rl_app.models import ProductCategory, Product
from .forms import ProductCategoryForm, ProductForm
from django.views.generic.edit import DeleteView

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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'rl_app/add_product.html'

    def form_valid(self, form):
        form.instance.product = get_object_or_404(Product, pk=self.kwargs['productcategory_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('rl_app:productcategory_detail', kwargs={'productcategory_id': self.kwargs['productcategory_id']})
    
class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'rl_app/productcategory_update.html'
    pk_url_kwarg = 'productcategory_id'
    success_url = reverse_lazy('rl_app:productcategory_list')

def update_product(request, productcategory_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('rl_app:product_detail', productcategory_id=productcategory_id, product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'rl_app/product_update.html', {'form': form, 'product': product})

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    pk_url_kwarg = 'productcategory_id'
    success_url = reverse_lazy('rl_app:productcategory_list')
    template_name = 'rl_app/productcategory_confirm_delete.html'

class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = 'product_id'

    def get_success_url(self):
        return reverse_lazy('rl_app:productcategory_detail', kwargs={'productcategory_id': self.object.category_id.id})