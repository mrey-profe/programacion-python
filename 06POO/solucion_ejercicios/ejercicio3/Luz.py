class Luz:
    __color: str

    def __init__(self):
        self.__color = "rojo"

    def cambiar_color(self) -> None:
        if self.__color == "rojo":
            self.__color = "verde"
        elif self.__color == "verde":
            self.__color = "amarillo"
        else:
            self.__color = "rojo"

    def __str__(self):
        return f"Semáforo en {self.__color}"
    
if __name__ == "__main__":
    semaforo = Luz()
    for i in range(10):
        semaforo.cambiar_color()
        print(semaforo)

    