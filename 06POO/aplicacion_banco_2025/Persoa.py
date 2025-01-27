class Persoa:
    nome: str
    __idade: int
    __dni: str
    
    def __init__(self, nome: str, idade: int, dni: str):
        self.nome = nome
        self.idade = idade
        self.dni = dni

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade >= 0 and isinstance(idade, int):
            self.__idade = idade
        else:
            raise Exception("Idade incorrecta")

    @property
    def dni(self): # Getter, se le pone el mismo nombre que el atributo pero sin __
        return self.__dni
    
    @dni.setter
    def dni(self, dni): # Setter, se le pone el mismo nombre que el atributo pero sin __
        if (Persoa.comprobar_dni(dni)): # Solo lo modificamos si es correcto
            self.__dni = dni
        else:
            raise Exception("DNI incorrecto")
            
    def __str__(self):
        return f"Nome: {self.nome}. Idade: {self.idade}. DNI: {self.dni}."
    
    @staticmethod
    def comprobar_dni(dni: str) -> bool:
        letras = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
        dni_sen_letra = int(dni[:8])
        letra = dni[-1]
        return letras[dni_sen_letra % 23] == letra
    
if __name__ == "__main__":
    try:
        p = Persoa("Pepita Docampo", 25, "12345678Z")
        p.idade = -5
        print(p)
        p.dni = "12345678A"
        print(p)
        p1 = Persoa("Mario Pérez", 30, "87654321B")
        print(p1)
        print(Persoa.comprobar_dni("12345678Z"))
    except Exception as e:
        print(e)