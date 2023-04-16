import unittest
from entities.product import ProductDiscountError
from entities.product import Product
from entities.shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def is_available_to_skip():
        return True
    def is_connected():
        return False
    def setUp(self) -> None:
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name,self.price)
        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)



    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(),'lo sentimos no esta vacio')

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone,self.shopping_cart_2.products)
        product = Product('Nuevo Producto',10)
        self.shopping_cart_2.add_product(product)
        self.assertIn(product,self.shopping_cart_2.products)
    def test_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone,self.shopping_cart_2.products)

    def test_discount_errop(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Exmaple', price=10.0, discount= 15.0)
    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15))
        self.shopping_cart_1.add_product(Product(name='Camara',price=700,discount=70))

        self.assertGreater(self.shopping_cart_1.total,0)
        self.assertLess(self.shopping_cart_1.total,1000)

        self.assertEqual(self.shopping_cart_1.total,645)
    def test_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total,0)
    
    @unittest.skip('La prueba no cumple con los requisitos necesarios')
    def test_skip_example(self):
        self.assertEqual(1,1)
    @unittest.skipUnless(is_connected,'No Cuenta con los requisitos')
    def test_skip_example_two(self):
        pass

if __name__ == '__main__':
    unittest.main()