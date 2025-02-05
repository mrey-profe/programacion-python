from ContaBancaria import ContaBancaria
from Persoa import Persoa

class Banco:
    nome: str
    enderezo: str
    telefono: str
    contas_bancarias: list[ContaBancaria]
    
    def __init__(self, nome: str, enderezo:str, telefono: str):
        self.nome = nome
        self. enderezo = enderezo
        self.telefono = telefono
        self.contas_bancarias = []
        
    def agregar_conta(self, conta: ContaBancaria) -> None:
        self.contas_bancarias.append(conta)
    
    def __str__(self):
        resultado = f"Banco: {self.nome}, {self.enderezo}, {self.telefono}, con contas:\n"
        for conta in self.contas_bancarias:
            resultado += str(conta) + "\n"
        return resultado
        
if __name__ == "__main__":
    b = Banco("Abanca", "Teis", "986789456")
    print(b)
    p = Persoa("Ana González", 30, "12345678Z")
    c = ContaBancaria(p, "789464643218")
    b.agregar_conta(c)
    print(b)