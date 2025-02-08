class Persona:
    __nombre: str
    __edad: int
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        if len(nombre) == 0:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if not isinstance(edad, int):
            raise ValueError("La edad debe ser un número entero")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.__edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"