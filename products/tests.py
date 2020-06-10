from django.test import TestCase
from .models import Product
# Create your tests here.

class ProductTests(TestCase):
    """
    Test for product models
    """

    def test_str(self):
        test_name = Product(name="Test Product")
        self.assertEqual(str(test_name), 'Test Product')
