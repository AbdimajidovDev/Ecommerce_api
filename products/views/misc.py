from rest_framework import viewsets
from django_filters import rest_framework as django_filters
from rest_framework import filters

from products.models import Order
from products.models import Review, Category
from products.serializers import ReviewSerializer, CategorySerializer
from products.permissions import IsOwnerOrReadOnly
from products.serializers import OrderSerializer



class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['name']
