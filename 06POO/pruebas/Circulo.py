import math

class Circulo:
    radio: float
    centro: tuple[float, float]
    
    def __init__(self, radio: float, centro: tuple[float, float] = (0,0)) -> None:
        self.radio = radio
        self.centro = centro

    @property
    def area(self) -> float:
        return math.pi * self.radio ** 2
    
    def redimensionar(self, proporcion: float) -> None:
        self.radio *= proporcion

    def mover(self, mover_x: float, mover_y: float) -> None:
        nuevo_x = self.centro[0] + mover_x
        nuevo_y = self.centro[1] + mover_y
        self.centro = (nuevo_x, nuevo_y)

    def __str__(self):
        return f"Círculo de radio {self.radio} situado en x = {self.centro[0]} e y = {self.centro[1]}"

if __name__ == "__main__":
    c1 = Circulo(5, (0,1))
    print(c1)
    c2 = Circulo(6, (2,3))
    print(c2)
    c3 = Circulo(2)
    print(c3)
    print(c3.radio)
    c3.radio = 10
    print(c3.radio)
    print(c3.area)
    c3.redimensionar(1.5)
    c3.mover(2, 4)
    pass