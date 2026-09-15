'''
Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. 
Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.
'''

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre


class Tienda:
    def __init__(self):
        self.productosdispo = []

    def agregar_producto(self, producto):
        """Agrega un objeto Producto a la tienda."""
        self.productosdispo.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")

    def mostrar_inventario(self):
        """Muestra los productos disponibles en la tienda."""
        if not self.productosdispo:
            print("\nEl inventario está vacío.")
            return

        print("\n--- INVENTARIO DE LA TIENDA ---")
        for i, prod in enumerate(self.productosdispo, 1):
            # Accedemos directamente a prod.nombre
            print(f"{i}. {prod.nombre}")

    def realizar_compra(self):
        """Permite comprar (y retirar) un producto del inventario."""
        if not self.productosdispo:
            print("\nNo hay productos disponibles para comprar.")
            return

        self.mostrar_inventario()
        nombre_buscar = input("\nIntroduce el nombre del producto a comprar: ").strip()

        for prod in self.productosdispo:
            # Comparamos el nombre del objeto directamente
            if prod.nombre.lower() == nombre_buscar.lower():
                self.productosdispo.remove(prod)
                print(f"\n¡Has comprado '{prod.nombre}' con éxito! Se ha retirado del inventario.")
                return

        print(f"\nEl producto '{nombre_buscar}' no está disponible.")


# --- EJEMPLO DE USO ---

mi_tienda = Tienda()

# Creamos productos solo con su nombre
p1 = Producto("Cocacola")
p2 = Producto("Almendras")
p3 = Producto("Huevos")
p4 = Producto("Miel")

# Agregamos los productos a la tienda
mi_tienda.agregar_producto(p1)
mi_tienda.agregar_producto(p2)
mi_tienda.agregar_producto(p3)
mi_tienda.agregar_producto(p4)

# Mostramos el inventario inicial
mi_tienda.mostrar_inventario()

# Compramos un producto
mi_tienda.realizar_compra()

# Mostramos el inventario actualizado
mi_tienda.mostrar_inventario()



