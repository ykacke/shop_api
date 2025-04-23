
from django.http import JsonResponse
from django.views import View
from .models import Category, Product, Review
from django.http import Http404
from rest_framework.decorators import api_view
from .serializers import ProductWithReviewsSerializer
from rest_framework import generics
from django.db.models import Count


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.annotate(products_count=Count('product'))
    data = [{
        'id': category.id,
        'name': category.name,
        'products_count': category.products_count
    } for category in categories]

    return JsonResponse(data, safe=False)


@api_view(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse({
            'id': category.id,
            'name': category.name
        })
    except Category.DoesNotExist:
        raise Http404("Category not found")


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all().values('id', 'title', 'description', 'price', 'category__name')
    return JsonResponse(list(products), safe=False)


@api_view(['GET'])
def product_detail(request, id):
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

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all().values('id', 'text', 'product__title')
    return JsonResponse(list(reviews), safe=False)


@api_view(['GET'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
        return JsonResponse({
            'id': review.id,
            'text': review.text,
            'product': review.product.title
        })
    except Review.DoesNotExist:
        raise Http404("Review not found")