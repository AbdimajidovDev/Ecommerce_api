from django_filters import rest_framework as django_filters
from .models import Product, FlashSale


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']


class FlashSaleFilters(django_filters.FilterSet):

    class Meta:
        model = FlashSale
        fields = ['start_time', 'end_time']
