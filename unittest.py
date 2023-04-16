import unittest

class TestExample(unittest.TestCase):
    def test_suma_numeros(self):
        numero1 = 10
        numero2 = 20
        resultado = numero1 + numero2

        self.assertEqual(resultado,40)
    def test_resta_numeros(self):
        self.assertEqual(31 -20,10)
if __name__ == '__main__':
    unittest.main()