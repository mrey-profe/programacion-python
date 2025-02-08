from persona import Persona

class Piso:
    __numero: int
    __puerta: str
    __residentes: list[Persona]
    es_presidente: bool
    
    def __init__(self, numero, puerta):
        self.numero = numero
        self.puerta = puerta
        self.__residentes = []
        self.es_presidente = False

    @property
    def residentes(self):
        return self.__residentes

    def agregar_residente(self, persona):
        self.__residentes.append(persona)

    def eliminar_residente(self, persona):
        if persona in self.__residentes:
            self.__residentes.remove(persona)

    def __str__(self):
        residentes_str = ", ".join(str(residente) for residente in self.__residentes)
        return f"Piso {self.numero}, Puerta {self.puerta}, Presidente: {self.es_presidente}, Residentes: [{residentes_str}]"
    
if __name__ == "__main__":
    p = Piso(1, "A")
    p.agregar_residente(Persona("Juan", 30))
    p.agregar_residente(Persona("Ana", 25))
    print(p)