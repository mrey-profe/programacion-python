class Coche:
    # Atributos de Coche, no es necesario declararlos, pero lo hacemos por claridad
    marca: str
    modelo: str
    potencia: int
    num_marchas: int
    contador: int = 0 # Atributo de clase
    
    def __init__(self, marca, modelo, potencia, num_marchas = 5) -> None:
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.num_marchas = num_marchas
        self._marcha_actual = 1
        Coche.contador += 1 # Para acceder a un atributo de clase, hay que hacerlo a través de la clase
        
    def __str__(self) -> str:
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nPotencia: {self.potencia}\nNúmero de marchas: {self.num_marchas}"
    
    def cambiar_marcha(self, subir: bool) -> None:
        if subir:
            if self._marcha_actual < self.num_marchas:
                self._marcha_actual += 1
        else:
            if self._marcha_actual > 1:
                self._marcha_actual -= 1
                
    def marcha_atras(self) -> None:
        self._marcha_actual = -1
        
    def punto_muerto(self) -> None:
        self._marcha_actual = 0
        
if __name__ == "__main__":
    c1 = Coche("Audi", "A4", 150)
    print(c1)
    c1.cambiar_marcha(True)
    print(c1._marcha_actual)
    c1.cambiar_marcha(False)
    print(c1._marcha_actual)
    c1.punto_muerto()
    print(c1._marcha_actual)
    c2 = Coche("Seat", "Ibiza", 90, 6)
    print(c2)
    print(c1)
    print(Coche.contador)