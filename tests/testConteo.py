import unittest
from geodePy.conteo import conteo

class Testconteo(unittest.TestCase):

    # === FACTORIAL ===
    def test_factorial_cero(self):
        self.assertEqual(conteo.factorial(0), 1)

    def test_factorial_positivo(self):
        self.assertEqual(conteo.factorial(5), 120)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            conteo.factorial(-4)

    # === COMBINATORIA ===
    def test_combinatoria_correcta(self):
        self.assertEqual(conteo.C(5, 2), 10)

    def test_combinatoria_n_igual_k(self):
        self.assertEqual(conteo.C(4, 4), 1)

    def test_combinatoria_k_mayor_n(self):
        with self.assertRaises(ValueError):
            conteo.C(3, 5)

    # === PERMUTACIONES (P) ===
    def test_permutacion_correcta(self):
        self.assertEqual(conteo.P(5, 2), 20)

    def test_permutacion_n_igual_k(self):
        self.assertEqual(conteo.P(4, 4), 24)

    def test_permutacion_k_mayor_n(self):
        with self.assertRaises(ValueError):
            conteo.P(2, 3)

    # === PERMUTACIONES CON REPETICIÓN (PR) ===
    def test_permutacion_con_repeticion_correcta(self):
        self.assertEqual(conteo.PR(6, [2, 2, 2]), 90)  # 6! / (2!*2!*2!) = 720 / 8 = 90

    def test_permutacion_con_repeticion_suma_distinta(self):
        with self.assertRaises(ValueError):
            conteo.PR(6, [2, 2])  # 2+2 ≠ 6

    # === VARIACIONES (V) ===
    def test_variacion_correcta(self):
        self.assertEqual(conteo.V(5, 2), 20)  # 5*4 = 20

    def test_variacion_k_mayor_n(self):
        with self.assertRaises(ValueError):
            conteo.V(3, 5)

    # === VARIACIONES CON REPETICIÓN (VR) ===
    def test_variacion_con_repeticion_correcta(self):
        self.assertEqual(conteo.VR(3, 2), 9)  # 3^2

    def test_variacion_con_repeticion_negativos(self):
        with self.assertRaises(ValueError):
            conteo.VR(-1, 2)

        with self.assertRaises(ValueError):
            conteo.VR(2, -2)

if __name__ == '__main__':
    unittest.main()
