from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductListView, ProductDetailView, ReviewListView, ReviewDetailView

urlpatterns = [
    path('api/v1/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/v1/categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('api/v1/products/', ProductListView.as_view(), name='product-list'),
    path('api/v1/products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/v1/reviews/', ReviewListView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
]