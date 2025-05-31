from datetime import datetime, timedelta
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import filters
from django_filters import rest_framework as djando_filters

from products.filters import FlashSaleFilters
from products.models import FlashSale, Product, ProductViewHistory


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()

    class FlashSaleSerializer(serializers.ModelSerializer):
        class Meta:
            model = FlashSale
            fields = ('id', 'product', 'discount_percentage', 'start_time', 'end_time')

    serializer_class = FlashSaleSerializer

    filter_backends = (djando_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = FlashSaleFilters
    search_fields = ['discount_percentage']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_time', openapi.IN_QUERY, description='Aksiya boshlanish vaqti', type=openapi.TYPE_STRING, format='date-time'),
            openapi.Parameter('end_time', openapi.IN_QUERY, description='Aksiya tugash vaqti', type=openapi.TYPE_STRING, format='date-time'),
            openapi.Parameter('search', openapi.IN_QUERY, description='Chegirma foyizi orqali qidirish', type=openapi.TYPE_STRING)
        ]
    )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET'])
def check_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    user_viewed = ProductViewHistory.objects.filter(user=request.user, product=product).exists()

    upcoming_flash_sale = FlashSale.objects.filter(
        product=product,
        start_time__lte=datetime.now() + timedelta(hours=24)
    ).first()

    if user_viewed and upcoming_flash_sale:
        discount = upcoming_flash_sale.discount_percentage
        start_time =upcoming_flash_sale.start_time
        end_time =upcoming_flash_sale.end_time
        return Response({
            'message': f"This product will be a {discount}% off flash sale!",
            'start_time': start_time,
            'end_time': end_time,
        })
    else:
        return Response({
            'message': "No upcoming flash sales for this product."
        })
