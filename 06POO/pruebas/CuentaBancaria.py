class Cuenta:
    numero_cuenta: str
    titular: str
    saldo: float
    
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0) -> None:
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        
    @staticmethod
    def comprobar_cuenta(numero_cuenta: str) -> bool:
        if len(numero_cuenta) != 20:
            return False
        if numero_cuenta[:2] != "ES":
            return False
        if not numero_cuenta[2:].isnumeric():
            return False
        if not Cuenta.comprobar_iban(numero_cuenta):
            return False
        return True
    
    @staticmethod
    def comprobar_iban(numero_cuenta: str) -> bool:
        coeficientes1 = [4, 8, 5, 10, 9, 7, 3, 6]
        suma = 0
        for i in range(8):
            suma += coeficientes1[i] * int(numero_cuenta[i])
        digito1 = 11 - (suma % 11)
        if digito1 == 10:
            digito1 = 1
        elif digito1 == 11:
            digito1 = 0
        print(digito1)
        
        coeficientes2 = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        segunda_parte = numero_cuenta[10:]
        suma2 = 0
        for i in range(10):
            suma2 += coeficientes2[i] * int(segunda_parte[i])
        digito2 = 11 - (suma2 % 11)
        if digito2 == 10:
            digito2 = 1
        elif digito2 == 11:
            digito2 = 0
        print(digito2)
        
        return digito1 == int(numero_cuenta[8]) and digito2 == int(numero_cuenta[9])        
    
print(Cuenta.comprobar_iban("20800806353040221707"))