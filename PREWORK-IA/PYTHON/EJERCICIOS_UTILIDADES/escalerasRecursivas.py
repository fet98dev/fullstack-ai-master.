#Recursividad => Es una funcion que se llama a si misma, es decir, 
#una funcion que se llama a si misma para resolver un problema.
#Recursividad => Definicion de la funcion, se encuentra una llamada a si misma.
#Caso base => Retorno de la llamada, detenemos la llamada infinita. Caso de cumplimiento.
#Caso/llamada recursiva => Llamada interna a la funcion misma.

#1. Nos encontramos en el escalon N
#2. Solo podemos movernos 1 paso / 1 salto (saltar 2 escalones)
#Camino: hace referencia a la secuencia que sigo para llegar del punto inicial al punto final.

#Significado de N: Cuantos escalones me faltan para llegar al piso

#Formula: caminos(N) = caminos(N-1) + caminos(N-2)


def caminos(n):
    if n == 0:
        return 1 #Posibilidades que tengo encontrandome en el piso - 1 (no moverme)


    #Caso base. me pasé del piso (camino incorrecto)
    if n < 0:
        return 0

    #Caso recursivo:
    # desde N puedo bajar 1 (N-1) o saltar 2(N-2)    
    return caminos(n-1) + caminos(n-2)

print("Version Recursiva")
posibles_caminos = caminos(3)
print(posibles_caminos)



