"""
SISTEMA DE RESERVAS DE VUELOS
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. 
Aquí tienes una posible estructura:

- Clase base: `Vuelo`
- Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
- Métodos: agregar pasajero, verificar disponibilidad de asientos

- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
- Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)

Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.
"""



#Dos funciones;
##Verificar_disponibiladad; Si la capacidad no supera 150 entonces es TRUE
##Si la capacidad supera los 150 entonces lanzo mensaje de que el avion esta lleno.


###agregar_pasajeros; Si la funcion verificar_disponibiladad es TRUE
###Entonces pido el pasajero y lo añado a la lista de pasajeros.

#####Ejemplo de uso
#####Primero verifico
#####Segundo


class Vuelo:
    def __init__(self,numero_vuelo, origen, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad#es capacidad de asientos disponibles
        self.pasajeros = []


    def verificar_disponibilidad(self):
        pass

    def agregar_pasajeros(self):
        pass

class VueloEspecial(Vuelo):
    def __init__(self,numero_vuelo, origen, destino, capacidad, motivo):
            super().__init__(numero_vuelo,origen,destino,capacidad)
            self.motivo = motivo
    






#EJEMPLO DE USO
mi_vuelo = Vuelo("UX198", "MAL","BCN",9)
mi_vuelo2 = VueloEspecial("UX198", "MAL","BCN",130, "Vacaciones")
mi_vuelo.verificar_disponibilidad()
mi_vuelo.agregar_pasajeros()


print("Numero de vuelo:",mi_vuelo.numero_vuelo)
print("Origen:",mi_vuelo.origen)
print("Destino:",mi_vuelo.destino)
print(mi_vuelo2.motivo)



            




    