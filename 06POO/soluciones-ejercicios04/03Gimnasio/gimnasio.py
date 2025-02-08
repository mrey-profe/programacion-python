from cliente import Cliente
from clase import Clase

class Gimnasio:
    _nombre: str
    __clientes: list[Cliente]
    __clases: list[Clase]

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__clientes = []
        self.__clases = []

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if isinstance(valor, str) and len(valor) > 0:
            self._nombre = valor
        else:
            raise ValueError("El nombre debe ser un string")

    def registrar_cliente(self, cliente: Cliente):
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)

    def agregar_clase(self, clase: Clase):
        if clase not in self.__clases:
            self.__clases.append(clase)

    def reservar_clase(self, id_cliente: str, nombre_clase: str) -> bool:
        for cliente in self.__clientes:
            if cliente.id == id_cliente:
                cliente_reserva = cliente
                break
        for clase in self.__clases:
            if clase.nombre == nombre_clase:
                clase_reserva = clase
                break
        if cliente_reserva and clase_reserva:       
            return clase_reserva.inscribir_cliente(cliente_reserva)
        return False

    def cancelar_reserva(self, id_cliente: str, nombre_clase: str) -> bool:
        for clase in self.__clases:
            if clase.nombre == nombre_clase:
                clase_reserva = clase
                break
        if clase_reserva:
            return clase_reserva.cancelar_inscripcion(id_cliente)
        return False

    def clases_disponibles(self) -> list[Clase]:
        return [clase for clase in self.__clases if len(clase.inscritos) < clase.capacidad]

    def __str__(self) -> str:
        clientes_str = "\n".join(str(cliente) for cliente in self.__clientes)
        clases_str = "\n".join(str(clase) for clase in self.__clases)
        return f"Gimnasio: {self.nombre}\n\nClientes:\n{clientes_str}\n\nClases:\n{clases_str}"
