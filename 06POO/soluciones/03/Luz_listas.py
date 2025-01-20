class Luz:
    cor: int
    CORES = ("vermello", "verde", "ambar", "rosa", "branco", "azul", "violeta")
    
    def __init__(self):
        self.cor = 0
        
    def cambia_cor(self) -> None:
        self.cor = (self.cor + 1) % len(self.CORES)
            
    def __str__(self):
        return f"Semáforo de cor {self.CORES[self.cor]}"

if __name__ == "__main__":
    s = Luz()
    print(s)
    s.cambia_cor()
    print(s)
    s.cambia_cor()
    print(s)