
datos = {}



#El programa debe permitir registrar y mantener un seguimiento de los puntajes de un juego.
##Ingresar los nombres y puntajes.
###El programa tiene que pedirte los nombres y los puntajes:
####Almacenarlos en un diccionario.
continuar = True
while continuar:
    nombre = input("Ingresa el nombre del jugador (o `salir´ para terminar):")
    if nombre.lower() == "salir":
        continuar = False
    else:
        puntaje = int(input("Ingresa los puntos del jugador:"))
        datos[nombre] = puntaje





###Proporcionar funcionalidades para mostrar el puntaje mas alto(max(puntaje)), el promedio de puntajes(media(puntajes))
#  y la cantidad total de jugadores.(len(nombre))


#para saber el maximo es :
jugador_mas_alto = max(datos, key=datos.get)
puntaje_mas_alto = datos[jugador_mas_alto]
print("Puntaje mas alto:")
print("Jugador:", jugador_mas_alto)
print("Puntaje:",puntaje_mas_alto)

#obtener el promedio de puntajes
total_puntajes = sum(datos.values())
cantidad_jugadores = len(datos)
promedio = total_puntajes/ cantidad_jugadores
print("Promedio:", promedio)

print("La cantidad de jugadores es: ", cantidad_jugadores)





































