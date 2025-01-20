class ContaBancaria:
    nome_titular: str
    numero_conta: str
    saldo: float
    
    def __init__(self, nome_titular: str, numero_conta: str, saldo: float=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo