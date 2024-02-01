class Alumnx:
    nombre: str
    dni: str
    edad: int
    nombre_escuela: str

    def __init__(self, nombre: str, dni: str, edad: int, nombre_escuela: str):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.nombre_escuela = nombre_escuela

    def es_mayor_edad(self) -> bool:
        return self.edad >= 18
    
    def __ge__(self, otro) -> bool:
        return self.edad >= otro.edad
    
    def __gt__(self, otro) -> bool:
        return self.edad > otro.edad
    
    def __le__(self, otro) -> bool:
        return self.edad <= otro.edad
    
    def __lt__(self, otro) -> bool:
        return self.edad < otro.edad
    
    def __eq__(self, otro) -> bool:
        return self.dni == otro.dni
    
if __name__ == "__main__":
    a1 = Alumnx("Pepe", "12345678A", 17, "IES El Pilar")
    a2 = Alumnx("Ana", "12345678A", 17, "IES El Pilar")
    print(a1 == a2)