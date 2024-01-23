from enum import Enum

class Jugada(Enum):
    PIEDRA = 0
    PAPEL = 1
    TIJERAS = 2
    
    def __gt__(self, otro):
        return (otro.value + 1) % 3 == self.value
    
    def __lt__(self, otro):
        return (self.value + 1) % 3 == otro.value
    
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
    
    