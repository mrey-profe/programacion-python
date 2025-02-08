from tarea import Tarea

class Usuario:
    nombre: str
    tareas: list[Tarea]
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        return [str(tarea) for tarea in self.tareas]

    def cambiar_estado_tarea(self, descripcion, nuevo_estado):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                tarea.estado = nuevo_estado
                return f"Estado de la tarea '{descripcion}' cambiado a '{nuevo_estado}'"
        return f"Tarea '{descripcion}' no encontrada"