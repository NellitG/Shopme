from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import filters

# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']