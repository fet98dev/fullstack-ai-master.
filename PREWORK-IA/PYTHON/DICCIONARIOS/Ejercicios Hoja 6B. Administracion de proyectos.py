

#Programa para administrar tareas y responsabilidades.
tareas = {}

##Cada tarea tiene un nombre, una descripcion, un responsable

##Anadir una tarea nueva.
tareas["tarea1"] = {"descripcion": "limpiar el patio", "responsables":"pedro"}
tareas["tarea2"] = {"descripcion": "ayunar", "responsables":"unomismo"}
tareas["tarea3"] = {"descripcion":"estudiar como un cabron", "responsables":"yo"}
##Asignar responsables a las tareas existentes.
tareas["tarea1"]["responsables"] = "FETHE"
##Actualizar las descripciones de las tareas
tareas["tarea3"]["descripcion"] = "prepararse para el examen de aleman"

for tarea, infor in tareas.items():
    descripcion = infor["descripcion"]
    responsable = infor["responsables"]
    print("El responsable de la", tarea.title(),"es;",responsable)
    print("Su tarea es:", descripcion.title())
    print("")


