# from django.shortcuts import render
# from rest_framework import generics, permissions
# from accounts.serializers import RegisterSerializer
# from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken

# # Create your views here.
# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer
#     queryset = User.objects.all()
#     permission_classes = [permissions.AllowAny]

# class LogoutView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         try:
#             refresh_token = request.data.get['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response({"message": "Successfully logged out"}, status=204)
#         except KeyError:
#             return Response({"error": "Refresh token is required"}, status=400)
#         except KeyError:
#             return Response({"error": "Invalid or expired token"}, status=400)