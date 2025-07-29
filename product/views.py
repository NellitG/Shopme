from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework import filters

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']