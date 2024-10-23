import math

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

print(round(area_circulo(10), 2))