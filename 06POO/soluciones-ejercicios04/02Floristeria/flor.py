class Flor:
    nombre: str
    color: str
    __precio: float

    def __init__(self, nombre: str, color: str, precio: float):
        self.nombre = nombre
        self.color = color
        self.precio = precio

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        self.__precio = max(0, valor)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.color}): {self.precio:.2f}€"

    def __add__(self, other: 'Flor') -> float:
        if isinstance(other, Flor):
            return self.precio + other.precio
        else:
            raise TypeError("Solo se pueden sumar flores")
