from django.test import TestCase
from django.test.client import Client
from .models import Product, ProductCategory
from django.core.management import call_command


# Create your tests here.


class ModelTests(TestCase):
    def test_product_create_with_price(self):
        product = Product(price=0)
        self.assertIsNotNone(product.price)


class TestMainappSmoke(TestCase):
	def setUp(self):
		call_command('flush', '--noinput')
		call_command('loaddata', 'test_db.json')
		self.client = Client()

	def test_mainapp_urls(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

		response = self.client.get('/contact/')
		self.assertEqual(resoponse.status_code, 200)

		response = self.client.get('products/')
		self.assertEqual(response.status_code, 200)

		response = self.client.get('/products/category/0/')
		self.assertEqual(response.status_code, 200)

		for category in ProductCategory.objects.all():
			response = self.client.get(f'/products/category/{category.pk}/')
			self.assertEqual(response.status_code, 200)

		for product in Poduct.objects.all():
			response = self.client.get(f'/products/product/{product.pk}/')
			self.assertEqual(response.status_code, 200)


	def tearDown(self):
		call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')

