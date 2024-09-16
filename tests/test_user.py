import unittest
from app.models.product import Product

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Example setup of a product
        self.product = Product(name="Test Product", price=100.00, quantity=10)

    def test_product_creation(self):
        # Test product creation
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100.00)
        self.assertEqual(self.product.quantity, 10)