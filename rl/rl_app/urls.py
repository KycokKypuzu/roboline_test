from django.urls import path
from . import views

app_name = 'rl_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('productcategories/', views.ProductCategoryListView.as_view(), name='productcategory_list'),
    path('productcategories/<int:productcategory_id>/', views.ProductCategoryDetailView.as_view(), name='productcategory_detail'),
    path('productcategories/<int:productcategory_id>/products/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('productcategories/create/', views.ProductCategoryCreateView.as_view(), name='create_productcategory'),
] 