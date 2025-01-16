class Libro:
    titulo: str
    autor: str
    num_ejemplares: int
    num_ejemplares_prestados: int

    def __init__(self, titulo:str, autor:str, num_ejemplares:int=1):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares
        self.num_ejemplares_prestados = 0
        pass

    def __str__(self) -> str:
        return (
            f"Libro:\n\t{self.titulo}\n\t{self.autor}\n\t"
            f"Prestados: {self.num_ejemplares_prestados}/{self.num_ejemplares}"
        )
        
    def prestar(self) -> bool:
        if self.num_ejemplares > self.num_ejemplares_prestados:
            self.num_ejemplares_prestados += 1
            return True
        else: # Non hai exemplares para prestar
            return False

if __name__ == "__main__": # Executado só se se lanza como un script, e non se se importa como un módulo
    l = Libro("Cien años de soledad", "Gabriel García Márquez", 3)
    l2 = Libro("El Quijote", "Miguel de Cervantes")
    l3 = Libro("Harry Potter", "J.K. Rowling", 5)
    print(l)
    l.prestar()
    print(l)
    print(l2)
    print(l3)
