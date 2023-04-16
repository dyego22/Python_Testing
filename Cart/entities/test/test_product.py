import unittest
from entities.product import Product

class TestProduct(unittest.TestCase):
    
    def test_product_example(self):
        self.assertEqual(1,1)
    def setUp(self) -> None:
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name,self.price)    
    def test_produc_object(self):
        name = 'Manzana'
        price = 1.70
        product= Product(name,price)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price,1.7,'Lo Sentimos error en precio')
    def test_product_name(self):
        self.assertEqual(self.smartphone.name,self.name)
    def test_product_price(self):
        self.assertEqual(self.smartphone.price,self.price)