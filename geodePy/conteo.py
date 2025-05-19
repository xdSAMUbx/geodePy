class Conteo():

    @staticmethod
    def factorial (n:int) -> int:
        if n==0:
            return 1
        elif n<0:
            raise SyntaxError("No se puede calcular el factorial de un número negativo")
        
        fac:int = 1
        for i in range(1,n+1): fac *= i
        return fac

    @staticmethod
    def C(n:int, k:int) -> float:

        if k>n: 
            raise SyntaxError("En un coeficiente binomial k no puede ser mayor a n")
        else:
            num:int = n-k
            comb:float = Conteo.factorial(n)/(Conteo.factorial(num)*Conteo.factorial(k))
        return comb