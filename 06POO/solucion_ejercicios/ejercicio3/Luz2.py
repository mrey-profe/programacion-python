class Luz:
    __color: str
    COLORES: list[str] = ["rojo", "verde", "amarillo"]

    def __init__(self):
        self.__color = Luz.COLORES[0]

    def cambiar_color(self) -> None:
        indice = Luz.COLORES.index(self.__color)
        self.__color = Luz.COLORES[(indice + 1) % len(Luz.COLORES)]

    def __str__(self):
        return f"Semáforo en {self.__color}"
    
if __name__ == "__main__":
    semaforo = Luz()
    for i in range(10):
        semaforo.cambiar_color()
        print(semaforo)

    