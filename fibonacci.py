import time

def sucesion_fibonacci(num_terminos: int) -> list[int]:
    lista = [0, 1]

    for i in range(num_terminos - 2):
        lista.append(lista[-1] + lista[-2])

    return lista

def termino_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    actual = 1
    anterior = 0

    for i in range(n - 1):
        actual, anterior = actual + anterior, actual
        # suma = actual + anterior
        # anterior = actual
        # actual = suma

    return actual
t1 = time.time()
sucesion_fibonacci(800)
t2 = time.time()
termino_fibonacci(799)
t3 = time.time()

print(t2-t1)
print(t3-t2)