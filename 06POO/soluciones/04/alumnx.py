class Alumnx:
    nome: str
    __dni: str
    __idade: int
    nome_escola: str
    
    def __init__(self, nome: str, dni: str, idade: int, nome_escola: str):
        self.nome = nome
        self.dni = dni
        self.idade = idade
        self.nome_escola = nome_escola
            
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni: str):
        if Alumnx.dni_correcto(dni):
            self.__dni = dni
        else:
            raise Exception("DNI incorrecto")
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            raise Exception("A idade non pode ser negativa")        
        
    @staticmethod
    def dni_correcto(dni: str) -> bool:
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            return False
        if not dni[-1].isalpha():
            return False
        if not dni[:8].isdigit():
            return False
        resto = int(dni[:8]) % 23
        if dni[-1].upper() != letras[resto]:
            return False
        return True
    
    def __str__(self) -> str:
        return f"{self.nome} ({self.dni}) de {self.idade} anos, estudante de {self.nome_escola}"
    
    def e_maior_idade(self) -> bool:
        return self.idade >= 18
    
    def __ge__(self, other):
        return self.idade >= other.idade
    
    def __gt__(self, other):
        return self.idade > other.idade
    
    def __le__(self, other):
        return self.idade <= other.idade
    
    def __lt__(self, other):
        return self.idade < other.idade
    
    def __eq__(self, other):
        return self.dni == other.dni
    
    
if __name__ == "__main__":
    try:
        a = Alumnx("Ana", "12345678Z", 18, "IES de Sar")
        print(a.e_maior_idade())
        a.idade = 15
        print(a.e_maior_idade())
        print(a)
        a2 = Alumnx("Juan", "12345678Z", 25, "IES de Teis")
        if a > a2:
            print("Ana é maior que Juan")
        else:
            print("Ana non é maior que Juan")
    except Exception as e:
        print(e)
    
    
    
    