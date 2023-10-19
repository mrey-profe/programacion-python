list = ["1",2,"a","b"]
resultado = []
for i in list:
    if not isinstance(i,str):
        resultado.append(i)

print(list)