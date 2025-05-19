from geodePy.const import pi

class ang:
    
    @staticmethod
    def decDeg(gg:int, mm:int, ss:float, ori:str, lat:bool=True):
        """
        Convierte grados, minutos y segundos a grados decimales, con dirección geográfica.

        Args:
            gg (int): Grados (0 a 90 para latitudes, 0 a 360 para longitudes).
            mm (int): Minutos.
            ss (float): Segundos.
            ori (str): Dirección cardinal ('N', 'S' para latitudes; 'E', 'W' para longitudes).
            lat (bool, optional): Si es True, se interpreta como latitud; si es False, como longitud. Default es True.

        Returns:
            float: El ángulo en grados decimales, con signo según la orientación.

        Raises:
            ValueError: Si los valores están fuera de rango o `ori` es inválido.
        """
        ori = ori.upper()

        if lat:
            if not (0 <= gg <= 90):
                raise ValueError("Latitudes deben tener grados entre 0 y 90")
            if ori not in ("N", "S"):
                raise ValueError("Latitudes deben tener orientación 'N' o 'S'")
        else:
            if not (0 <= gg <= 360):
                raise ValueError("Longitudes deben tener grados entre 0 y 360")
            if ori not in ("E", "W"):
                raise ValueError("Longitudes deben tener orientación 'E' o 'W'")

        decimal = gg + mm / 60 + ss / 3600
        if (lat and ori == "S") or (not lat and ori == "W"):
            return -decimal
        return decimal
    
    @staticmethod
    def radians(dec:float) -> float:
        """
        Convierte un ángulo de grados a radianes.

        Args:
            deg (float): Ángulo en grados decimales.

        Returns:
            float: Ángulo convertido a radianes.
        """
        return (dec * pi) / 180
    
    @staticmethod
    def degrees(rad: float) -> float:
        """
        Convierte radianes a grados decimales.

        Args:
            rad (float): Radianes en grados decimales.

        Returns:
            float: Ángulo convertido a grados decimales
        """
        return (rad * 180) / pi
