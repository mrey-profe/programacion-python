from edificio import Edificio
from persona import Persona

edificio = Edificio("Calle Mayor", 3, 2, 1200)

edificio.pisos[0].agregar_residente(Persona("Juan", 30))
edificio.pisos[0].agregar_residente(Persona("Ana", 25))
edificio.pisos[1].agregar_residente(Persona("Luis", 40))
edificio.pisos[2].agregar_residente(Persona("Maria", 35))

print(edificio)

print("\nNombrando nuevo presidente...")
edificio.nombrar_nuevo_presidente()

print(edificio)

print(f"\nCuota total del edificio: {edificio.calcular_cuota_total():.2f}")