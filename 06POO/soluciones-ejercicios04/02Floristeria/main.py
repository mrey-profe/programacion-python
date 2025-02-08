from floristeria import Floristeria
from flor import Flor

# Crear una floristería
floristeria = Floristeria("Flores Teis")

# Crear pedidos para clientes
floristeria.crear_pedido("Ana")
floristeria.crear_pedido("Carlos")

# Crear flores
rosa = Flor("Rosa", "Roja", 5.0)
tulipan = Flor("Tulipán", "Amarillo", 3.5)
girasol = Flor("Girasol", "Amarillo", 4.0)
lirio = Flor("Lirio", "Blanco", 4.5)

# Agregar flores a los pedidos
floristeria.agregar_flor_a_pedido("Ana", rosa)
floristeria.agregar_flor_a_pedido("Ana", tulipan)
floristeria.agregar_flor_a_pedido("Carlos", girasol)

# Mostrar pedidos
print(floristeria)

# Calcular y mostrar el total de todos los pedidos
print(f"\nTotal de todos los pedidos: {floristeria.calcular_total_pedidos():.2f}€")

# Agregar una flor más a un pedido existente
floristeria.agregar_flor_a_pedido("Ana", lirio)

# Mostrar pedidos actualizados
print("\nPedidos actualizados:")
print(floristeria)

# Calcular y mostrar el nuevo total de todos los pedidos
print(f"\nNuevo total de todos los pedidos: {floristeria.calcular_total_pedidos():.2f}€")

