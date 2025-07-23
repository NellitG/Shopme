from django.shortcuts import render
from rest_framework import viewsets
from order_item.models import Order_item
from order_item.serializers import Order_itemSerializer

# Create your views here.
class Order_itemViewSet(viewsets.ModelViewSet):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer