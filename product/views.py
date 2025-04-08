# product/views.py
from django.http import JsonResponse
from django.views import View
from .models import Category, Product, Review
from django.http import Http404

class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all().values('id', 'name')
        return JsonResponse(list(categories), safe=False)

class CategoryDetailView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            return JsonResponse({
                'id': category.id,
                'name': category.name
            })
        except Category.DoesNotExist:
            raise Http404("Category not found")

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all().values('id', 'title', 'description', 'price', 'category__name')
        return JsonResponse(list(products), safe=False)

class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            return JsonResponse({
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'price': product.price,
                'category': product.category.name
            })
        except Product.DoesNotExist:
            raise Http404("Product not found")

class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all().values('id', 'text', 'product__title')
        return JsonResponse(list(reviews), safe=False)

class ReviewDetailView(View):
    def get(self, request, id):
        try:
            review = Review.objects.get(id=id)
            return JsonResponse({
                'id': review.id,
                'text': review.text,
                'product': review.product.title
            })
        except Review.DoesNotExist:
            raise Http404("Review not found")