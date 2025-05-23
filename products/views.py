from django.db import models
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Product, Review, Category
from products.serializers import ProductSerializer, ReviewSerializer, CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', None)
        if category:
            self.queryset = self.queryset.filter(category=category)  # faqat biz tanlagan p. categoriyasidagi p.lar chiqadi
        return super().list(request, *args, **kwargs)


    def retrieve(self, request, *args, **kwargs): # detail endpoints uchun
        instance = self.get_object() # biz chaqirgan mahsulot
        serializer = self.get_serializer(instance)
        related_products = Product.objects.filter(category=instance.category).exclude(id=instance.id)[:5] # shu p. categoryasiga tegishli boshqa p.larni ham chaqirish
        related_serializer = ProductSerializer(related_products, many=True) # datalarni serializerlash
        return Response({
            'product': serializer.data, # bizga kerak mahsulot
            'related_products': related_serializer.data # mahsulotimiz turdoshlari
        })

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_products = Product.objects.annotate(avg_rating=models.Avg('reviews__rating')).order_by('-avg_rating')[:3]
        serializer = ProductSerializer(top_products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        product = self.get_object()
        reviews = product.reviews.all()

        if reviews.count() == 0:
            return Response({"average_rating": "No reviews yet!"})
        avg_rating = sum([review.rating for review in reviews]) / reviews.count()
        return Response({"average_rating": avg_rating})
