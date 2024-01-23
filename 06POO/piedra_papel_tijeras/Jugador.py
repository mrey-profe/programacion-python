class Jugador:
    nombre: str
    puntuacion: int
    rondas_ganadas: int
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0
        self.rondas_ganadas = 0

    def __str__(self):
        return f"{self.nombre} - {self.puntuacion} puntos"

    def sumar_punto(self):
        self.puntuacion += 1

    def resetear_puntuacion(self):
        self.puntuacion = 0
        
    def sumar_ronda_ganada(self):
        self.rondas_ganadas += 1