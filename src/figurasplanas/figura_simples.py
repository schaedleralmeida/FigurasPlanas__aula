from math import pi
from .figuraplana import FiguraPlana

"""
Esse módulo implementa figuras simples criadas a partir de 
dimensões características.
As figuras implementadas são
-Retangulo

"""

class Retangulo(FiguraPlana):
    """
    Representa um retângulo de base b altura h.
    Iniciado com canto superior direito nas coordenadas (b/2, h/2).    
    """

    def __init__(self, b:float, h:float) -> None:

        self.b = b
        self.h = h
        A = b * h
        Ix = (b * h**3) / 12
        Iy = (h * b**3) / 12
        xc = 0.0
        yc = 0.0
        Ixy = 0.0
        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"Retangulo(b={self.b}, h={self.h})"

    def __str__(self) -> str:
        txt = f"Retângulo: b= {self.b}, h= {self.h} \n"
        txt += super().__str__()
        return txt


class Circulo(FiguraPlana):
    """
    Representa um retângulo de base b altura h.
    Iniciado com canto superior direito nas coordenadas (b/2, h/2).    
    """

    def __init__(self, r:float) -> None:
        A = pi * r**2
        pass

class SemiCirculo(FiguraPlana):
    """
    Representa um semicírculo de raio r.
    Iniciado com origem no centro do semicírculo e ângulo de 0 a pi.
    """

    def __init__(self, r:float) -> None:

        self.r = r
        A = (pi * r**2) / 2
        Ix = (pi * r**4) / 8
        Iy = (pi * r**4) / 8
        xc = 0.0
        yc = 4 * r / (3 * pi)
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy) 

    def __repr__(self) -> str:
        return f"SemiCirculo(r={self.r})"

    def __str__(self) -> str:
        txt = f"Semicírculo: r= {self.r} \n"
        txt += super().__str__()
        return txt