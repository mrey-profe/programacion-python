class Tarea:
    descripcion: str
    fecha_vencimiento: str
    __estado: str
    
    def __init__(self, descripcion, fecha_vencimiento):
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = "pendiente"

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado in ["pendiente", "completada"]:
            self.__estado = nuevo_estado
        else:
            raise ValueError("El estado debe ser 'pendiente' o 'completada'")

    def marcar_como_completada(self):
        self.estado = "completada"

    def __str__(self):
        return f"Tarea: {self.descripcion}, Vence: {self.fecha_vencimiento}, Estado: {self.estado}"