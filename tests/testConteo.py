import unittest
from geodePy.conteo import Conteo  # Asegúrate que este sea el path correcto

class TestConteoFactorial(unittest.TestCase):

    def test_factorial_positivo(self):
        self.assertEqual(Conteo.factorial(5), 120)  # 5! = 120

    def test_factorial_cero(self):
        self.assertEqual(Conteo.factorial(0), 1)  # 0! = 1

    def test_factorial_negativo(self):
        with self.assertRaises(SyntaxError):
            Conteo.factorial(-3)

    def test_combinantoria(self):
        self.assertEqual(Conteo.C(10,2), 45.0)  # 5! = 120

    def test_combinatoria_(self):
        self.assertEqual(Conteo.(0), 1)  # 0! = 1

    def test_factorial_negativo(self):
        with self.assertRaises(SyntaxError):
            Conteo.factorial(-3)

if __name__ == '__main__':
    unittest.main()