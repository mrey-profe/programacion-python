class Libro:
    titulo: str
    autor: str
    num_ejemplares: int
    num_ejemplares_prestados: int

    def __init__(self, titulo: str, autor: str, num_ejemplares: int = 1, num_ejemplares_prestados: int = 0):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares
        self.num_ejemplares_prestados = num_ejemplares_prestados
        
    def prestar(self) -> bool:
        if self.num_ejemplares_prestados < self.num_ejemplares: # Puedo prestar
            self.num_ejemplares_prestados += 1
            return True
        else: # No hay suficientes ejemplares para prestar
            return False

    def devolver(self) -> bool:
        if self.num_ejemplares_prestados > 0: # Hay ejemplares prestados, se puede devolver
            self.num_ejemplares_prestados -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"Título: {self.titulo}\n Autor: {self.autor}\n Ejemplares: {self.num_ejemplares}\n Prestados: {self.num_ejemplares_prestados}"

if __name__ == "__main__":
    libro1 = Libro("Quijote", "Cervantes", 3, 0)
    print(libro1)
    for i in range(4):
        if libro1.prestar():
            print("Libro prestado correctamente")
        else:
            print("No quedan ejemplares")
        print(libro1.num_ejemplares_prestados)
    
    for i in range(4):
        if libro1.devolver():
            print("Libro devuelto correctamente")
        else:
            print("No había ejemplares prestados")
        print(libro1.num_ejemplares_prestados)