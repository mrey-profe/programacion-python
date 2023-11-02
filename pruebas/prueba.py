incidencias = [[3, 2, 1, 4, 5], [1, 5, 10, 2, 8], [4, 3, 1, 0, 1]]

suma = 0
for f in range(len(incidencias)):
    suma += incidencias[f][0]

print("La suma de las incidencias de los lunes es ", suma)

sumas_incidencias_dia = [0, 0, 0, 0, 0]

# Suma incidencias por día
for dia in range(5):
    for f in range(len(incidencias)):
        sumas_incidencias_dia[dia] += incidencias[f][dia]

print(sumas_incidencias_dia)

# Suma incidencias por semana
sumas_incidencias_semana = []

for f in range(len(incidencias)):
    suma = 0
    for c in range(len(incidencias[f])):
        suma += incidencias[f][c]
    sumas_incidencias_semana.append(suma)

print(sumas_incidencias_semana)