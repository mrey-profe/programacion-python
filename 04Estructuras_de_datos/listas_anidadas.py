# Frutería que tiene pedidos para preparar de un conjunto de clientes y quiere saber 
# cuántas unidades de cada tiene que pedir
frutas = ["manzanas", "peras", "aguacates", "plátanos", "kiwis"]

pedidos = [[3, 5, 4, 8], [2, 0, 1, 9], [1, 2, 3, 1], [0, 5, 4, 3], [1, 2, 4, 5]]

frutas_totales = []

# for i in range(len(pedidos)):
#     total = 0
#     for cantidad in pedidos[i]:
#         total += cantidad
#     media = total / len(pedidos[i])
#     print("El total de", frutas[i], "es", total)

for i in range(len(pedidos)):
    total = 0
    for cantidad in pedidos[i]:
        total += cantidad
    frutas_totales.append(total)

for i in range(len(frutas_totales)):
    print("La cantidad de", frutas[i], "es", frutas_totales[i])

# Cuántas frutas en total se han pedido (suponemos que no hemos hecho nada anteriormente)
total_absoluto = 0

for cantidades_fruta in pedidos:
    for cantidad_cliente in cantidades_fruta:
        total_absoluto += cantidad_cliente

print(total_absoluto)

total_absoluto = 0
for f in range(len(pedidos)):
    for c in range(len(pedidos[f])):
        total_absoluto += pedidos[f][c]







