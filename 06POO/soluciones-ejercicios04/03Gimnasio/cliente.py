class Cliente:
    nombre: str
    id: str
    __edad: int
    ___membresia: str
    TIPO_MEMBRESIA = ["básica", "premium"]

    def __init__(self, nombre: str, id: str, edad: int, membresia: str):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.membresia = membresia

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, valor: int):
        if valor > 0 and isinstance(valor, int):
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser un número entero positivo")

    @property
    def membresia(self) -> str:
        return self.__membresia

    @membresia.setter
    def membresia(self, valor: str):
        if valor in Cliente.TIPO_MEMBRESIA:
            self.__membresia = valor
        else:
            raise ValueError(f"La membresía debe ser {Cliente.TIPO_MEMBRESIA}")

    def __str__(self) -> str:
        return f"Cliente: {self.nombre}, ID: {self.id}, Edad: {self.edad}, Membresía: {self.membresia}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Cliente):
            return self.id == other.id
        return False
