class Rectangulo:
    _base: float
    _altura: float

    def __init__(self, base: float, altura: float) -> None:
        if base <= 0 or altura <= 0:
            raise Exception("Las dimensiones del rectángulo deben ser mayores que 0")
        self._base = base
        self._altura = altura
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if base <= 0:
            raise Exception("La base del rectángulo debe ser mayor que 0")
        self._base = base

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise Exception("La altura del rectángulo debe ser mayor que 0")
        self._altura = altura

    def area(self) -> float:
        return self._base * self._altura
    
    def __str__(self):
        return f"Rectángulo de base {self._base} y altura {self.altura}"
    
    def es_cuadrado(self) -> bool:
        return self._base == self._altura
    
    def __eq__(self, otro) -> bool:
        return (self._base == otro._base and self._altura == otro._altura) or 
        (self._base == otro._altura and self._altura == otro._base) 
    
if __name__ == "__main__":
    r = Rectangulo(3, 4)
    print(r)
    print(r.area())
    print(r.es_cuadrado())
    r.base = 5
    print(r)
    r.altura = 5
    print(r)
    print(r.area())
    print(r.es_cuadrado())
    r.base = 0
