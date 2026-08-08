

'''
REGISTRO DE VENTAS:
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. 
El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
producto)
'''
#Diccionario en el que se guardaran las ventas.
ventas = {}

#pedimos el nombre del producto por pantalla
while True:
    producto = input("Ingrese producto: ")
    if producto.lower() == "salir":
        break
    #Pedimos la cantidad vendida por pantalla y la convertimos a numero entero
    cantidad = int(input(f"¿Cuantas unidades de '{producto}' se vendieron?: "))

    #Guardamos o actualizamos en el diccionario vacio
    if producto in ventas:
        ventas[producto] += cantidad
    else:
        ventas[producto] = cantidad
print("RESUMEN FINAL DE VENTAS")
print(ventas)


#imprimir el registro de ventas y el total de ventas diarias.
