class Vista:
    def bienvenida(self):
        print("Bienvenido al juego Piedra, Papel o Tijeras")
        print("===========================================")

    def mostrar_menu_opcion(self) -> int:
        opcion = 0
        while opcion < 1 or opcion > 4:
            print("1. Piedra")
            print("2. Papel")
            print("3. Tijeras")
            print("4. Salir")
            opcion = int(input("Escoge una opción: "))
            if opcion < 1 or opcion > 4:
                print("Opción incorrecta")
        return opcion

    def mostrar_opcion(self, opcion, jugador : bool = True):
        verbo = "Has elegido" if jugador else "El ordenador elige"
        if opcion == 1:
            print(f"{verbo} Piedra")
        elif opcion == 2:
            print(f"{verbo} Papel")
        elif opcion == 3:
            print(f"{verbo} Tijeras")
        elif opcion == 4:
            print("Gracias por jugar")
            
    def pedir_nombre_jugador(self) -> str:
        return input("Introduce tu nombre: ")
    
    def mostrar_ganador_jugada(self, ganador):
        print(f"Gana {ganador} la jugada")
        
    def mostrar_empate_jugada(self):
        print("Empate en la jugada")
        
    def mostrar_puntuaciones(self, nombre_jugador, puntuacion_jugador, computadora):
        print(f"{nombre_jugador}: {puntuacion_jugador} - Computadora: {computadora}")
        
    def mostrar_ganador_partida(self, ganador):
        print(f"Gana {ganador} la partida")
        
    def volver_a_jugar(self) -> bool:
        respuesta = input("¿Quieres volver a jugar? (s/n): ")
        return respuesta == "s" or respuesta == "S"
    
    def mostrar_rondas_ganadas(self, nombre_jugador, rondas_jugador, rondas_computadora):
        print("===========================================")
        print("Rondas ganadas")
        print(f"{nombre_jugador}: {rondas_jugador} - Computadora: {rondas_computadora}")
        print("===========================================")
