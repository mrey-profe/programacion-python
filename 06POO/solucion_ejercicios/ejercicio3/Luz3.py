# Los semáforos pueden tener distintos colores de luces

class Luz:
    __color: str
    colores: list[str]

    def __init__(self, colores: list[str]):
        self.__color = colores[0]
        self.colores = colores

    def cambiar_color(self) -> None:
        indice = self.colores.index(self.__color)
        self.__color = self.colores[(indice + 1) % len(self.colores)]

    def __str__(self):
        return f"Semáforo en {self.__color}"
    
if __name__ == "__main__":
    semaforo = Luz(["rojo", "verde", "amarillo"])
    for i in range(10):
        semaforo.cambiar_color()
        print(semaforo)
    print()
    s2 = Luz(["rojo", "verde", "amarillo", "azul", "blanco"])
    for i in range(10):
        s2.cambiar_color()
        print(s2)