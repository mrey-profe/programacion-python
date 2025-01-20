class Rectangulo:
    base: float
    altura: float
    
    def __init__(self, base: float=0, altura: float=0):
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return self.base * self.altura
    
    def __str__(self):
        return (
            f"Rectángulo de base {self.base}cm e altura {self.altura}cm.\n"
            f"A súa área é {self.area()}cm\u00B2"
        )
        
    def e_cadrado(self) -> bool:
        return self.base == self.altura

if __name__ == "__main__":
    r = Rectangulo(4.5, 4.5)
    print(r)
    if r.e_cadrado():
        print("É un cadrado")
    else:
        print("Non é un cadrado")