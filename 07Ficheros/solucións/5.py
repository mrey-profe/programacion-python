import os

ficheiros = os.listdir(".")

with open("directory.txt", "w") as ficheiro_directorio:
    for ficheiro in ficheiros:
        ficheiro_directorio.write(ficheiro + "\n")