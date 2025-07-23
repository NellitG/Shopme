from django.shortcuts import render
from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer

# Create your views here.
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer