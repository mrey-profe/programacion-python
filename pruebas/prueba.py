grupos = [
    ["Ana", "Luis", "Marta"],
    ["Juan"],
    ["Elena", "Jorge"]
]

for f in range(len(grupos)):
    for c in range(len(grupos[f])):
        print(integrante[f][c], end=", ")
    print()