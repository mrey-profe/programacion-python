from enum import Enum

class Jugada(Enum):
    PIEDRA = 0
    PAPEL = 1
    TIJERAS = 2
    LAGARTO = 3
    SPOCK = 4

    def __gt__(self, otro):
        prioridad = {
            "lagarto": {"piedra", "tijeras"},
            "piedra": {"papel", "spock"},
            "tijeras": {"piedra", "spock"},
            "spock": {"papel", "lagarto"},
            "papel": {"lagarto", "tijera"}
        }   
        return otro.name.lower() not in prioridad[self.name.lower()]
    
    def __lt__(self, otro):
        prioridad = {
            "lagarto": {"piedra", "tijeras"},
            "piedra": {"papel", "spock"},
            "tijeras": {"piedra", "spock"},
            "spock": {"papel", "lagarto"},
            "papel": {"lagarto", "tijera"}
        }   
        return otro.name.lower() in prioridad[self.name.lower()]
    
    def __eq__(self, otro):
        return self.value == otro.value
    
if __name__ == "__main__":
    import random
    jugada = random.choice(Jugada._member_names_)
    print(jugada)
    print(Jugada.PIEDRA > Jugada.TIJERAS)
    print(Jugada.TIJERAS > Jugada.PIEDRA)
    print(Jugada.PAPEL > Jugada.PIEDRA)
    print(Jugada.PIEDRA > Jugada.PAPEL)
    print(Jugada.TIJERAS > Jugada.PAPEL)
    print(Jugada.PAPEL > Jugada.TIJERAS)
    print(Jugada.PIEDRA > Jugada.PIEDRA)
    
    