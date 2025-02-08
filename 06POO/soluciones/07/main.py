from usuario import Usuario
from tarea import Tarea

usuarios = []

# Crear un usuario
usuario1 = Usuario("Elena")
usuarios.append(usuario1)

# Agregar tareas al usuario
usuario1.agregar_tarea(Tarea("Comprar pan", "2025-02-10"))
usuario1.agregar_tarea(Tarea("Estudiar para el examen", "2025-02-15")) 

# Mostrar tareas del usuario
print(f"Tareas de {usuario1.nombre}:")
for tarea in usuario1.mostrar_tareas():
    print(tarea)

# Cambiar estado de una tarea
print(usuario1.cambiar_estado_tarea("Comprar pan", "completada"))

# Mostrar tareas actualizadas
print(f"Tareas de {usuario1.nombre} actualizadas:")
for tarea in usuario1.mostrar_tareas():
    print(tarea)