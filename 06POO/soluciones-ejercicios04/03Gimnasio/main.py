from gimnasio import Gimnasio
from cliente import Cliente
from clase import Clase

# Crear un gimnasio
gimnasio = Gimnasio("FiTeis")

# Registrar clientes
clientes = [
    Cliente("Ana García", "C001", 28, "básica"),
    Cliente("Carlos López", "C002", 35, "premium"),
    Cliente("María Rodríguez", "C003", 42, "básica")
]
for cliente in clientes:
    gimnasio.registrar_cliente(cliente)

# Agregar clases
clases = [
    Clase("Yoga", "Laura Martínez", "Lunes 18:00", 15),
    Clase("Spinning", "Pedro Sánchez", "Martes 19:00", 20),
    Clase("Pilates", "Elena Gómez", "Miércoles 17:00", 10)
]
for clase in clases:     
    gimnasio.agregar_clase(clase)

# Realizar reservas
gimnasio.reservar_clase("C001", "Yoga")
gimnasio.reservar_clase("C002", "Spinning")
gimnasio.reservar_clase("C003", "Pilates")
gimnasio.reservar_clase("C001", "Spinning")

# Mostrar estado del gimnasio
print(gimnasio)

# Mostrar clases disponibles
print("\nClases disponibles:")
for clase in gimnasio.clases_disponibles():
    print(clase)

# Cancelar una reserva
gimnasio.cancelar_reserva("C001", "Yoga")

# Mostrar estado actualizado
print("\nEstado actualizado después de cancelar una reserva:")
print(gimnasio)