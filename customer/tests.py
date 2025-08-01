from django.test import TestCase
from .models import Customer

# Create your tests here.
class CustomerTests(TestCase):
    def test_customer_creation(self):
        customer = Customer.objects.create(name="Test Customer", email="JhQ7S@example.com", phone_number="1234567890", password="password", address="123 Main St, Anytown, USA")
        self.assertEqual(customer.name, "Test Customer")
        self.assertEqual(customer.email, "JhQ7S@example.com")
        self.assertEqual(customer.phone_number, "1234567890")
        self.assertEqual(customer.password, "password")
        self.assertEqual(customer.address, "123 Main St, Anytown, USA")