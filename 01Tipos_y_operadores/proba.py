def piramide(altura: int) -> None:
    for fila in range(1, altura + 1): # Filas
        print(" " * (altura - fila), end="")
        for columna in range(fila, 0, -1): #Columnas
            print(columna, end="")
        print()

piramide(5)