"""
LISTA DE TAREAS
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea, marcar una tarea como
completada y mostrar todas las tareas
"""

class listatareas:
  
    def __init__(self, listapendiente=[],tarea="",tareas_realizadas=[]):
        self.listapendiente = []
        self.tarea = ""
        self.tareas_realizadas = []
        

    def agregar_tarea(self):
        """Esta funcion agrega una tarea a la lista."""

        self.tarea = input("Introduce una tarea pendiente: ")
        self.listapendiente.append(self.tarea)
        return self.listapendiente


    def tarea_completada(self):
        "Esta funcion marca una tarea como completada"

        self.tarea_terminada = input("Introduce una tarea terminada: ")
        if self.tarea_terminada in self.listapendiente:
            self.listapendiente.remove(self.tarea_terminada)
            self.tareas_realizadas.append(self.tarea_terminada)
            print(f"---> Tarea {self.tarea_terminada} marcada como completada.")
        else:
            print(f"---> La tarea '{self.tarea_terminada}' no existe en pendientes.")
        return self.tareas_realizadas
        

    def mostrar_tareas(self):
        """Muestra las tareas completadas y pendientes."""
        print("\n--- ESTADO DE TAREAS ---")
        print(f"Pendientes: {self.listapendiente}")
        print(f"Completadas: {self.tareas_realizadas}")
        print("-------------------------------\n")




#----- FLUJO DE PRUEBA --------
mis_tareas = listatareas

# 1. Agregamos 2 tareas
mis_tareas.agregar_tarea()
mis_tareas.agregar_tarea()

# 2. Mostramos el estado inicial
mis_tareas.mostrar_tareas()

# 3. Completamos 1 tarea
mis_tareas.tarea_completada()

# 4. Mostramos el estado final
mis_tareas.mostrar_tareas()








