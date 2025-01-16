import math

class Circulo:
    radio: float
    centro: tuple[float, float]
    
    def __init__(self, radio: float, centro: tuple[float, float] = (0, 0)):
        self.radio = radio
        self.centro = centro
        pass

    def area(self):
        return math.pi * self.radio ** 2
    
    def __str__(self):
        return f"Círculo:\n radio {self.radio}\n centro {self.centro}"


if __name__ == "__main__": # Executado só se se lanza como un script, e non se se importa como un módulo
    c = Circulo(3, (0, 1))
    c1 = Circulo(5)
    cadea = "Ola " + str(c)
    print(c1)