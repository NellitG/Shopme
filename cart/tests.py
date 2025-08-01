from django.test import TestCase
from django.conf import settings
from .models import Cart
from .serializers import CartSerializer

# Create your tests here.
class CartTests(TestCase):
    def test_cart_creation(self):
        cart = Cart.objects.create(quantity=5)
        self.assertEqual(cart.quantity, 5)
        self.assertEqual(str(cart), f"Cart {cart.cart_id} with quantity {cart.quantity}")

class CartSerializerTests(TestCase):
    def test_cart_serializer(self):
        cart = Cart.objects.create(quantity=5)
        serializer = CartSerializer(cart)
        self.assertEqual(serializer.data, {
            'cart_id': cart.cart_id,
            'quantity': 5
        })