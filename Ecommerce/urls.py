"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet
from cart.views import CartViewSet
from category.views import CategoryViewSet
from customer.views import CustomerViewset
from order.views import OrderViewSet
from order_item.views import Order_itemViewSet
from payment.views import PaymentViewSet
from shipment.views import ShipmentViewSet
from wishlist.views import WishlistViewSet
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from accounts.views import RegisterView
# from accounts.views import LogoutView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'customers', CustomerViewset)
router.register(r'orders', OrderViewSet)
router.register(r'order_items', Order_itemViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'wishlists', WishlistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/register/', RegisterView.as_view(), name='register'),
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/logout/', LogoutView.as_view(), name='logout'),
]
