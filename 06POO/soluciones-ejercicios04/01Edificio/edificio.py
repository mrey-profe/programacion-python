from piso import Piso

class Edificio:
    calle: str
    __cuota_base: float
    pisos: list[Piso]
    
    
    def __init__(self, calle, pisos, puertas, cuota_base=1000):
        self.calle = calle
        self.cuota_base = cuota_base
        self.pisos = []
        for i in range(pisos):
            for j in range(puertas):
                self.pisos.append(Piso(i+1, chr(65+j)))
        self.pisos[0].es_presidente = True

    @property
    def num_pisos(self):
        return len(self.pisos)

    @property
    def cuota_base(self):
        return self.__cuota_base

    @cuota_base.setter
    def cuota_base(self, valor):
        self.__cuota_base = max(1000, valor)

    def calcular_cuota_total(self):
        total_viviendas = self.num_pisos
        if total_viviendas < 10:
            return self.cuota_base * 1.10
        elif total_viviendas <= 20:
            return self.cuota_base * 1.20
        elif total_viviendas <= 30:
            return self.cuota_base * 1.30
        else:
            return self.cuota_base * 1.35

    def nombrar_nuevo_presidente(self):
        for i in range(len(self.pisos)):
            if self.pisos[i].es_presidente:
                self.pisos[i].es_presidente = False
                indice_nuevo_presidente = (i + 1) % len(self.pisos) # Compruebo que no sea el último piso
                self.pisos[indice_nuevo_presidente].es_presidente = True
                break

    def __str__(self):
        pisos_str = "\n".join(str(piso) for piso in self.pisos)
        return f"Edificio en {self.calle}, Cuota Base: {self.cuota_base}, Cuota Total: {self.calcular_cuota_total():.2f}\nPisos:\n{pisos_str}"