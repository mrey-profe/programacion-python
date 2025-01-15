from Vista import Vista
from Jugador import Jugador
from Jugada import Jugada
from Computadora import Computadora

class Juego:
    vista: Vista
    jugador: Jugador
    computadora: Computadora
    
    def __init__(self) -> None:
        self.vista = Vista()
        self.computadora = Computadora()
    
    def compara_jugadas(self, jugada_jugador: Jugada, jugada_computadora: Jugada):
        if jugada_jugador > jugada_computadora:
            self.vista.mostrar_ganador_jugada(self.jugador.nombre)
            self.jugador.sumar_punto()
        elif jugada_jugador < jugada_computadora:
            self.vista.mostrar_ganador_jugada("el ordenador")
            self.computadora.sumar_punto()
        else:
            self.vista.mostrar_empate_jugada()
    
    def ha_finalizado_ronda(self) -> bool:
        return self.jugador.puntuacion == 3 or self.computadora.puntuacion == 3
    
    def resetear_puntuaciones(self):
        self.jugador.resetear_puntuacion()
        self.computadora.resetear_puntuacion()
    
    def jugar_ronda(self):
        opcion = 0
        while opcion != self.vista.SALIR and not self.ha_finalizado_ronda():
            opcion = self.vista.mostrar_menu_opcion()
            self.vista.mostrar_opcion(opcion)
            jugada_computadora = self.computadora.jugada()
            self.vista.mostrar_opcion(jugada_computadora.value + 1, False)
            if opcion != self.vista.SALIR:
                jugada_jugador = Jugada(opcion - 1)
                self.compara_jugadas(jugada_jugador, jugada_computadora)
                self.vista.mostrar_puntuaciones(self.jugador.nombre, self.jugador.puntuacion, self.computadora.puntuacion)

    def determinar_mostrar_ganador_ronda(self):
        if self.jugador.puntuacion == 3:
            self.jugador.sumar_ronda_ganada()
            ganador = self.jugador.nombre
        else:    
            self.computadora.sumar_ronda_ganada()
            ganador = "el ordenador"
        self.vista.mostrar_ganador_partida(ganador)
        self.vista.mostrar_rondas_ganadas(self.jugador.nombre, self.jugador.rondas_ganadas, self.computadora.rondas_ganadas)
                
    def jugar(self):
        self.vista.bienvenida()
        nombre = self.vista.pedir_nombre_jugador()
        self.jugador = Jugador(nombre)
        jugar = True
        while jugar:
            self.jugar_ronda()
            if self.ha_finalizado_ronda():
                self.determinar_mostrar_ganador_ronda()
                jugar = self.vista.volver_a_jugar()
                if jugar:
                    self.resetear_puntuaciones()
            else:
                jugar = False # El usuario ha escogido la opción self.vista.SALIR, salir del juego
            
        
        
