from punto import Punto

class Linea:
    __coordenadas: list[Punto]
    
    def __init__(self, p1: Punto, p2: Punto) -> None:
        self.__coordenadas = [p1, p2]
    
    def moverHorizontal(self, positivo: bool, valor: int) -> None:
        self.__coordenadas[0].moverHorizontal(positivo, valor)
        self.__coordenadas[1].moverHorizontal(positivo, valor)
        
    def moverVertical(self, positivo: bool, valor: int) -> None:
        self.__coordenadas[0].moverVertical(positivo, valor)
        self.__coordenadas[1].moverVertical(positivo, valor)
        
    def __str__(self):
        return f"Liña que pasa por: \n {self.__coordenadas[0]} \n {self.__coordenadas[1]}"
    
if __name__ == "__main__":
    p1 = Punto(2, 1)
    p2 = Punto(-3,-4)
    linea = Linea(p1, p2)
    print(linea)
    linea.moverHorizontal(True, 10)
    print(linea)