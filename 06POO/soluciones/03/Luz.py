class Luz:
    cor: str
    
    def __init__(self):
        self.cor = "vermello"
        
    def cambia_cor(self) -> None:
        if self.cor == "vermello":
            self.cor = "verde"
        elif self.cor == "ambar":
            self.cor = "vermello"
        elif self.cor == "verde":
            self.cor = "ambar"
            
    def __str__(self):
        return f"Semáforo de cor {self.cor}"

if __name__ == "__main__":
    s = Luz()
    print(s)
    s.cambia_cor()
    print(s)
    s.cambia_cor()
    print(s)