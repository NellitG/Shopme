from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
import httpx

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class CombinedProductView(APIView):
    async def get(self, request):
        async with httpx.AsyncClient() as client:
            response = await client.get('https://api.example.com/products')
            products = response.json()

        external_products = [
            {
                'id': product['id'],
                'name': product['name'],
                'description': product['description'],
                'price': product['price']
            } for product in products
        ]

        local_products = Product.objects.all()
        local_serialized = ProductSerializer(local_products, many=True).data

        all_products = local_serialized + external_products

        paginator = PageNumberPagination()
        paginated = paginator.paginate_queryset(all_products, request)
        return paginator.get_paginated_response(paginated)