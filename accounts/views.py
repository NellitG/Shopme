from django.shortcuts import render
from rest_framework import generics, permissions
from accounts.serializers import RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
