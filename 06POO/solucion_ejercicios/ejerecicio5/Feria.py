class Feria:
    numero_entradas: dict[str, int]
    precio_entradas: dict[str, int]
    
    def __init__(self):
        self.numero_entradas = {}
        self.precio_entradas = {}
        
    def anhadir_entradas(self, tipo_entrada: str, numero_entradas: int, precio_entrada: int):
        if tipo_entrada in self.numero_entradas:
            self.numero_entradas[tipo_entrada] += numero_entradas
        else:
            self.numero_entradas[tipo_entrada] = numero_entradas
        self.precio_entradas[tipo_entrada] = precio_entrada
        
    def comprar_entrada(self, tipo_entrada: str, numero_entradas: int) -> float:
        # Se le indica el tipo de entrada y el numero de entradas que quiere comprar y se devuelve el precio # total
        if tipo_entrada in self.numero_entradas:
            if self.numero_entradas[tipo_entrada] >= numero_entradas:
                self.numero_entradas[tipo_entrada] -= numero_entradas
                return numero_entradas * self.precio_entradas[tipo_entrada]
            else:
                return 0
        else:
            return 0
        
    def __str__(self) -> str:
        cadena_devolver = "Tipo".ljust(20) + "\tNúmero\tPrecio\n"
        cadena_devolver += "------------------------------------------\n"
        for tipo_entrada in self.numero_entradas:
            cadena_devolver += f"{tipo_entrada.ljust(20)}\t{self.numero_entradas[tipo_entrada]}\t{self.precio_entradas[tipo_entrada]}\n"
        return cadena_devolver
        
if __name__ == "__main__":
    feria = Feria()
    feria.anhadir_entradas("sala-principal", 2000, 10)
    feria.anhadir_entradas("compra-venta", 300, 25)
    feria.anhadir_entradas("vip", 20, 100)
    print(feria)
    