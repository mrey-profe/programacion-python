class Coche:
    def __init__(self, marca, modelo, potencia, num_marchas = 5) -> None:
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.num_marchas = num_marchas
        self._marcha_actual = 1
        
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
    coche = Coche("Audi", "A4", 150)
    print(coche)
    coche.cambiar_marcha(True)
    print(coche._marcha_actual)
    coche.cambiar_marcha(False)
    print(coche._marcha_actual)
    coche.punto_muerto()
    print(coche._marcha_actual)