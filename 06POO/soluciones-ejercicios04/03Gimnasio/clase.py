from cliente import Cliente

class Clase:
    __nombre: str
    __instructor: str
    horario: str
    __capacidad: int
    __inscritos: list[Cliente]

    def __init__(self, nombre: str, instructor: str, horario: str, capacidad: int = 20):
        self.nombre = nombre
        self.instructor = instructor
        self.horario = horario
        self.capacidad = capacidad
        self.__inscritos = []

    @property
    def capacidad(self) -> int:
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor: int):
        if valor >= 5 and valor <= 20 and isinstance(valor, int):
            self.__capacidad = valor
        else:
            self.__capacidad = 20
            
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if isinstance(valor, str) and len(valor) > 0:
            self.__nombre = valor
        else:
            raise ValueError("El nombre debe ser un string")
        
    @property
    def instructor(self) -> str:
        return self.__instructor
    
    @instructor.setter
    def instructor(self, valor: str):
        if isinstance(valor, str) and len(valor) > 0:
            self.__instructor = valor
        else:
            raise ValueError("El instructor debe ser un string")

    @property
    def inscritos(self) -> list[Cliente]:
        return self.__inscritos

    def inscribir_cliente(self, cliente: Cliente) -> bool:
        if len(self.__inscritos) < self.capacidad:
            self.__inscritos.append(cliente)
            return True
        return False

    def cancelar_inscripcion(self, id: str) -> bool:
        for cliente in self.__inscritos:
            if cliente.id == id:
                self.__inscritos.remove(cliente)
                return True
        return False

    def __str__(self) -> str:
        return f"Clase: {self.nombre}, Instructor: {self.instructor}, Horario: {self.horario}, Capacidad: {self.capacidad}, Inscritos: {len(self.__inscritos)}"
