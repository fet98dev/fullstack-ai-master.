"""
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). 
Implementa dos funciones, una para
agregar el producto vendido con su precio y 
otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])
"""


ventas = []

def agregar_producto(producto,precio):
    """Agregar los productos de las ventas"""

    productos = {"Producto": producto,
                 "Precio": precio}
    
    ventas.append(productos)
    
    print(f"Producto '{producto}' anadido correctamente.")



def mostrar_producto():
    """Mostrar todas las ventas registradas con sus precios."""
    if not ventas:
        print("No hay ventas registradas todavia.")
        return
    print("----RESUMEN DE VENTAS")
    for venta in ventas: #DONDE FALLABA ERA EN NO RECORRER LA LISTA, ES UNA LISTA NO LA PUEDES IMPRIMIR,HAY QUE RECORRERLA CON UN FOR
        print(f"----Producto: {venta['Producto']} | Precio: €{venta['Precio']}")

agregar_producto("Camiseta", 15.99)
agregar_producto("Pantalon", 19.99)
agregar_producto("tenis", 13.99)

mostrar_producto()





    

























