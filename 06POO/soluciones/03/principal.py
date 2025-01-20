from Luz_listas import Luz # from nome_ficheiro import clase
import time

if __name__ == "__main__":
    semaforo = Luz()
    print(semaforo)
    for i in range(10):
        time.sleep(1)
        semaforo.cambia_cor()
        print(semaforo)