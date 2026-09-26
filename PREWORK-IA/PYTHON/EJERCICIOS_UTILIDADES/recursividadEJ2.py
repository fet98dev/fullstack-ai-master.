




def buscar_cantidad_producto(inventario, codigo_producto, inicio = 0, fin = None):
    if fin is None:
        fin = len(inventario) - 1
#Caso base: si el rango no es valido
    if inicio > fin:
        return 0


    medio = (inicio+fin)// 2

#Comparar el codigo del producto con el codigo de la posicion media
    if inventario[medio]['codigo']==codigo_producto:
        #Caso base
        return inventario[medio]['cantidad']
    