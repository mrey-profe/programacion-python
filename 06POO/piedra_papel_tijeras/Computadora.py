import random
from Jugada import Jugada

class Computadora:
    puntuacion: int
    rondas_ganadas: int
    
    def __init__(self):
        self.puntuacion = 0
        self.rondas_ganadas = 0
        
    def sumar_punto(self):
        self.puntuacion += 1
        
    def resetear_puntuacion(self):
        self.puntuacion = 0
        
    def __str__(self):
        return f"Computadora - {self.puntuacion} puntos"
    
    def jugada(self) -> Jugada:
        jugada = random.choice(Jugada._member_names_)
        return Jugada[jugada]
    
    def sumar_ronda_ganada(self):
        self.rondas_ganadas += 1