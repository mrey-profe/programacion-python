from typing import Dict
from ramo import Ramo
from flor import Flor

class Floristeria:
    __nombre: str
    __pedidos: Dict[str, Ramo]

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__pedidos = {}

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        if len(nombre) == 0:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nombre

    def crear_pedido(self, nombre_cliente: str):
        if nombre_cliente not in self.__pedidos:
            self.__pedidos[nombre_cliente] = Ramo()

    def agregar_flor_a_pedido(self, nombre_cliente: str, flor: Flor):
        if nombre_cliente in self.__pedidos:
            self.__pedidos[nombre_cliente].agregar_flor(flor)
        else:
            raise KeyError(f"No existe un pedido para el cliente {nombre_cliente}")

    def calcular_total_pedidos(self) -> float:
        total = 0
        for ramo in self.__pedidos.values():
            total += ramo.precio_total
        return total

    def __str__(self) -> str:
        pedidos_str = "\n".join(f"{cliente}: {ramo}" for cliente, ramo in self.__pedidos.items())
        return f"Floristería {self.nombre}\nPedidos:\n{pedidos_str}"
