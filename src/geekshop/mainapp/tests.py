from django.test import TestCase
from .models import Product

# Create your tests here.


class ModelTests(TestCase):
    def test_product_create_with_price(self):
        product = Product(price=0)
        self.assertIsNotNone(product.price)
