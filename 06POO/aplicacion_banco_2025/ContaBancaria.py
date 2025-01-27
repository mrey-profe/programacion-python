from Persoa import Persoa # Do ficheiro Persoa.py importa a clase Persoa

class ContaBancaria:
    titular: Persoa
    numero_conta: str
    saldo: float
    
    def __init__(self, titular: Persoa, numero_conta: str, saldo: float=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        
    def __str__(self):
        return f"Titular: {self.titular.nome}. Número de conta: {self.numero_conta}. Saldo: {self.saldo}."
    
    def movemento(self, cantidade: float, e_ingreso: bool=True) -> bool:
        if e_ingreso:
            self.saldo += cantidade
        else:
            self.saldo -= cantidade
        # if self.saldo < 0:
        #     return False
        # else:
        #     return True
        return self.saldo >= 0
    
if __name__ == "__main__":
    conta1 = ContaBancaria(Persoa("Pepita Docampo", 25, "12345678Z"), "ES45 0987 0987 0987 0988", 100)
    print(conta1)
    p = Persoa("Mario Pérez", 34, "12123123E")
    conta2 = ContaBancaria(p, "ES45 0987 0987 0987 0999")
    print(conta2)
    print(conta1.movemento(150, False))
    print(conta1)
    print(conta1.movemento(60, True))
    print(conta1)
    print(conta1.movemento(30))
    print(conta1)