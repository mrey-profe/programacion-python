class Persona:
    nombre: str
    _dni: str
    _edad: int
    _altura: float
    _peso: float
    
    def __init__(self, nombre: str, dni: str, edad: int, altura: float, peso: float) -> None:
        self.nombre = nombre
        if (self.dni_correcto(dni)):
            self._dni = dni
        else:
            self._dni = ""
        self._edad = edad
        self._altura = altura
        self._peso = peso
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nDNI: {self._dni}\nEdad: {self._edad}\nAltura: {self._altura}"
    
    @property
    def dni(self) -> str:
        return self._dni
    
    @dni.setter
    def dni(self, dni: str) -> None:
        if (Persona.dni_correcto(dni)):
            self._dni = dni
    
    @property #getter
    def edad(self) -> int:
        return self._edad
    
    @edad.setter # Para poder usar el setter, hay que definir primero el getter
    def edad(self, edad: int) -> None:
        if edad >= 0 and edad <= 120:
            self._edad = edad
    
    @property
    def imc(self) -> float:
        return self._peso / (self._altura ** 2)
    
    @staticmethod
    def dni_correcto(dni: str) -> bool:
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            return False
        if dni[8].upper() != letras[int(dni[:8]) % 23]:
            return False
        return True
    
if __name__ == "__main__":
    p1 = Persona("Juan", "12345678A", 22, 1.75, 70)
    print(p1)
    print(p1.dni)
    p1.dni = "12345678A"
    print(p1.dni)
    p1.dni = "41013889J"
    print(p1.dni)
    p1.dni = "12345678"
    print(p1.dni)
    print(p1.imc)