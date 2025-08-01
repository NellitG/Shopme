from django.test import TestCase
from .models import Category

# Create your tests here.
class CategoryTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(category_name="Test Category")
        self.assertEqual(category.category_name, "Test Category")
        self.assertEqual(str(category), "Test Category")