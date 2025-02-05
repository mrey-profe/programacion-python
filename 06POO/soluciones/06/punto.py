class Punto:
    __x: int
    __y: int
    
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x: int):
        if x >= -100 and x <= 100:
            self.__x = x
        else:
            self.__x = 0
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y: int):
        if y >= -100 and y <= 100:
            self.__y = y
        else:
            self.__y = 0
            
    def moverHorizontal(self, positivo: bool, valor: int) -> None:
        if positivo:
            self.x = min(self.x + valor, 100)
        else: # negativo
            self.x = max(self.x - valor, -100)
    
    def moverVertical(self, positivo: bool, valor: int) -> None:
        if positivo:
            self.y = min(self.y + valor, 100)
        else: # negativo
            self.y = max(self.y - valor, -100)
    
    def __str__(self):
        return f"Punto en x={self.x} e y={self.y}"
            
if __name__ == "__main__":
    punto0 = Punto()
    print(punto0)
    punto1 = Punto(-150, 500)
    print(punto1)
    punto = Punto(90,60)
    print(punto)
    punto.moverHorizontal(True, 5)
    print(punto)
    punto.moverHorizontal(False, 5)
    print(punto)
    punto.moverHorizontal(True, 20)
    print(punto)
    punto.moverHorizontal(False, 2000)
    print(punto)
    
            