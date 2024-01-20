class Persona:
    nombre: str
    edad: int
    dni: str
    id: int
    num_personas: int = 0 # atributo de clase

    def __init__(self, nombre: str, edad: int, dni: str):
        if nombre == "":
            raise Exception("El nombre no puede estar vacío")
        self.nombre = nombre
        if edad < 0 or edad > 120:
            raise Exception("Valor de la edad incorrecto")
        self.edad = edad
        if not Persona.dni_correcto(dni):
            raise Exception("El DNI no es correcto")
        self.dni = dni
        self.id = Persona.num_personas
        Persona.num_personas += 1


    @staticmethod
    def dni_correcto(dni: str) -> bool:
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            return False
        if not dni[-1].isalpha():
            return False
        if not dni[:8].isdigit():
            return False
        resto = int(dni[:8]) % 23
        if dni[-1].upper() != letras[resto]:
            return False
        return True

if __name__ == "__main__":
    p1 = Persona("Juan Pérez López", 35, "123456789Z")
    p2 = Persona("María Pérez López", 30, "123454789Z")
    p3 = Persona("Elena Pérez López", 32, "123456789Z")
    print(Persona.dni_correcto("123456789Z"))