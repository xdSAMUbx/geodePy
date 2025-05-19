class conteo:

    @staticmethod
    def factorial(n: int) -> int:
        """Calcula el factorial de un número no negativo."""
        if n < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def C(n: int, k: int) -> int:
        """Calcula la combinatoria: nCk"""
        if not (0 <= k <= n):
            raise ValueError("k debe estar entre 0 y n")
        return conteo.factorial(n) // (conteo.factorial(k) * conteo.factorial(n - k))

    @staticmethod
    def P(n: int, k: int) -> int:
        """Calcula la permutación: nPk"""
        if not (0 <= k <= n):
            raise ValueError("k debe estar entre 0 y n")
        return conteo.factorial(n) // conteo.factorial(n - k)

    @staticmethod
    def CR(n: int, k: int) -> int:
        """Combinatoria con repetición: C(n + k - 1, k)"""
        if n <= 0 or k < 0:
            raise ValueError("n debe ser positivo y k no negativo")
        return conteo.C(n + k - 1, k)

    @staticmethod
    def PR(n: int, repeticiones: list[int]) -> int:
        """Permutaciones con repetición: n! / (r1! * r2! * ... * rx!)"""
        if sum(repeticiones) != n:
            raise ValueError("La suma de las repeticiones debe ser igual a n")
        denominador = 1
        for r in repeticiones:
            denominador *= conteo.factorial(r)
        return conteo.factorial(n) // denominador

    @staticmethod
    def V(n: int, k: int) -> int:
        """Variaciones sin repetición: n! / (n - k)!"""
        if not (0 <= k <= n):
            raise ValueError("k debe estar entre 0 y n")
        return conteo.P(n, k)

    @staticmethod
    def VR(n: int, k: int) -> int:
        """Variaciones con repetición: n^k"""
        if n < 0 or k < 0:
            raise ValueError("n y k deben ser no negativos")
        return n ** k
