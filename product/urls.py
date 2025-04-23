from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('api/v1/categories/',
         ProductListView.as_view(), name='category-list'),
    path('api/v1/categories/<int:id>/',
         ProductDetailView.as_view(), name='category-detail'),
    path('api/v1/products/',
         ProductListView.as_view(), name='product-list'),
    path('api/v1/products/<int:id>/',
         ProductDetailView.as_view(), name='product-detail'),

]