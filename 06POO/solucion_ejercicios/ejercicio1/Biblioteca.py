from Libro import Libro

class Biblioteca:
    _nombre: str
    __libros: list[Libro]

    def __init__(self, nombre: str):
        if len(nombre) == 0:
            raise Exception("El nombre no puede estar vacío")
        self._nombre = nombre
        self.__libros = []

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) == 0:
            raise Exception("El nombre no puede estar vacío")
        self._nombre = nombre

    @property
    def numero_libros(self):
        return len(self.__libros)
    
    @property 
    def numero_ejemplares(self):
        ejemplares = 0
        for libro in self.__libros:
            ejemplares += libro.num_ejemplares
        return ejemplares


    def anhadir_libro(self, libro: Libro) -> None:
        self.__libros.append(libro)

    def eliminar_libro(self, titulo: str) -> bool:
        indice = self.buscar_libro(titulo)
        if indice != -1: # Existe el libro
            del self.__libros[indice]
            return True
        return False

    def buscar_libro(self, titulo: str) -> int: 
        # Devuelve el índice en el que se encuentra el libro en la lista
        for i in range(len(self.__libros)):
            if self.__libros[i].titulo == titulo:
                return i
        return -1 # No lo ha encontrado
    
    def prestar_libro(self, titulo: str) -> bool:
        indice = self.buscar_libro(titulo)
        if indice != -1: # Existe el libro
            # libro = self.__libros[indice]
            # return libro.prestar()
            return self.__libros[indice].prestar()
        return False
    
    def devolver_libro(self, titulo: str) -> bool:
        indice = self.buscar_libro(titulo)
        if indice != -1: # Existe el libro
            # libro = self.__libros[indice]
            # return libro.devolver()
            return self.__libros[indice].devolver()
        return False
    
if __name__ == "__main__":
    biblio = Biblioteca("IES de Teis")
    li = Libro("Quijote", "Cervantes", 3, 3)
    biblio.anhadir_libro(li)
    li = Libro("El hobbit", "Tolkien", 2, 0)
    biblio.anhadir_libro(li)
    li = Libro("El señor de los anillos", "Tolkien", 2, 0)
    biblio.anhadir_libro(li)
    print(biblio.eliminar_libro("El hobbit"))
    print(biblio.eliminar_libro("Harry Potter"))
    print(biblio.prestar_libro("Quijote"))
    print(biblio.numero_libros)
    print(biblio.numero_ejemplares)
biblio.nombre = "Otro"
pass
