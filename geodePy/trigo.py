from geodePy.conteo import conteo
from geodePy.const import pi

class trigo:
    @staticmethod
    def sen(ang: float, cont: int = 80, rad: bool = True) -> float:
        """
        Calcula una aproximación al seno de un ángulo usando la serie de Taylor.

        Args:
            ang (float): Ángulo a evaluar.
            cont (int, optional): Número de términos de la serie. Mayor = más precisión.
            rad (bool, optional): Si True, el ángulo está en radianes. Si False, se asume en grados.

        Returns:
            float: Aproximación al seno del ángulo.
        """
        if not rad:
            ang = ang * pi / 180  # convertir a radianes

        suma = 0.0
        for n in range(cont):
            num = (-1)**n * (ang**(2*n + 1))
            denom = conteo.factorial(2*n + 1)
            suma += num / denom

        return suma