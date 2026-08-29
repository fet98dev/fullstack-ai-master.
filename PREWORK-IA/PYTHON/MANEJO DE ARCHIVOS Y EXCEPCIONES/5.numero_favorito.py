'''
NUMERO FAVORITO
Escribe un programa que solicite al usuario su número favorito. 
Utiliza json.dump() para almacenar este número en un archivo. 

Escribe unprograma separado que lea este valor e imprima el mensaje: 
"Sé cuál es tu número favorito… Es ____.” 
Combina ambos programas en un solo archivo
(puedes crear tantas funciones como necesites).
Si el número ya está almacenado, muestra el número favorito al usuario.
Si no lo está, solicita al usuario su número favorito y guárdalo en un archivo. 
Ejecuta el programa al menos dos veces para asegurarte de que funciona correctamente.
'''

#Escribir programa que solicite al usuario su numero favorito.  y usamos json.dump()
#para guardar el numero en un archivo. 
# Importamos el módulo 'json' integrado en Python para trabajar con formato JSON
import json


# Definimos la función encargada de pedir y guardar el número favorito
# Le asignamos un valor por defecto ("num_fav.json") a 'nombre_archivo' por si se llama sin argumentos
def guardar_numero_favorito(nombre_archivo="num_fav.json"):
    """Pide el número al usuario y lo guarda en el archivo JSON."""
    
    # Solicitamos por consola el número al usuario y guardamos la respuesta en la variable 'numero'
    numero = input("Introduce tu número favorito: ")
    
    # Abrimos el archivo en modo escritura ("w" = write)
    # Si el archivo no existe, Python lo crea automáticamente; si existe, lo sobrescribe
    # 'with' asegura que el archivo se cierre automáticamente al terminar el bloque
    with open(nombre_archivo, "w") as archivo:
        
        # 'json.dump()' toma la variable 'numero' y la escribe dentro del objeto de archivo 'archivo'
        json.dump(numero, archivo)
    
    # Confirmamos al usuario por consola que el número se ha guardado con éxito
    print("¡Gracias! He guardado tu número favorito.")


# Definimos la función encargada de leer el número guardado e imprimirlo
def leer_numero_favorito(nombre_archivo="num_fav.json"):
    """Lee el número del archivo JSON e imprime el mensaje."""
    
    # Abrimos el archivo en modo lectura ("r" = read)
    with open(nombre_archivo, "r") as archivo:
        
        # 'json.load()' extrae el contenido del archivo JSON y lo guarda en la variable 'numero'
        numero = json.load(archivo)
        
        # Imprimimos en pantalla el mensaje requerido usando una f-string para insertar la variable
        print(f"Sé cuál es tu número favorito… Es {numero}.")


# Definimos la función principal que controlará la lógica global del programa
def gestionar_numero_favorito():
    """Función principal que decide si leer o pedir el número."""
    
    # Guardamos en una variable el nombre del archivo JSON con el que vamos a trabajar
    archivo = "num_fav.json"
    
    # Iniciamos un bloque de prueba 'try' para intentar ejecutar la lectura primero
    try:
        # Intentamos ejecutar la función que lee el archivo
        leer_numero_favorito(archivo)
        
    # Si al intentar leer ocurre un error porque el archivo NO existe (FileNotFoundError)
    # O porque el archivo existe pero está vacío/corrupto (JSONDecodeError), atrapamos el error aquí:
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        
        # Como ocurrió un error arriba, ejecutamos esta función para pedir el número y crear el archivo
        guardar_numero_favorito(archivo)


# Llamamos a la función principal para iniciar la ejecución de todo el script
gestionar_numero_favorito()