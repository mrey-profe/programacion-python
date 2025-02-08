from flor import Flor

class Ramo:
    __flores: list[Flor]
    __precio_total: float

    def __init__(self):
        self.__flores = []

    def agregar_flor(self, flor: Flor):
        self.__flores.append(flor)

    @property
    def precio_total(self) -> float:
        return sum(flor.precio for flor in self.__flores)

    def __str__(self) -> str:
        flores_str = ", ".join(str(flor) for flor in self.__flores)
        return f"Ramo: [{flores_str}], Total: {self.precio_total:.2f}€"

    def __add__(self, other: 'Ramo') -> 'Ramo':
        if isinstance(other, Ramo):
            nuevo_ramo = Ramo()
            nuevo_ramo.__flores = self.__flores + other.__flores
            return nuevo_ramo
        else:
            raise TypeError("Solo se pueden sumar objetos Ramo")
