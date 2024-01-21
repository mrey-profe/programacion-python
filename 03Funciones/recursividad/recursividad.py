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
    return termino_fibonacci(n-1) + termino_fibonacci(n-2)

print(sucesion_fibonacci(10))
print(termino_fibonacci(10))