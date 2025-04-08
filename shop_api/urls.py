from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product.urls')),

    #Category
    path('api/v1/category/', views.category_list),
    path('api/v1/category/<int:id>/', views.category_detail),

    #Product
    path('api/v1/product/', views.product_list),
    path('api/v1/product/<int:id>/', views.product_detail),

    #Review
    path('api/v1/review/', views.review_list),
    path('api/v1/review/<int:id>/', views.review_detail),

    path('api/v1/categories/', views.category_list),
]
