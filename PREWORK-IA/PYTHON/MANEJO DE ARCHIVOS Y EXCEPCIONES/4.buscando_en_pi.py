'''
BUSCANDO EN PI

Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi 
(y en que posición. Puedes usar find()). 
Puedes usar el archivo pi_10000.txt
'''
#Abrir el archivo
##leer el archivo
###encontrar el numero que le pida.
####una vez encontrado utilizar .index para ver la posicion de tal
with open('pi_10000.txt') as arch_pi:
    doc = arch_pi.read()
    fecha = input("Introduce la fecha que quieres buscar: ")
    n_posicion = doc.find(fecha)# Busca el dato introducido y 
                                #nos da la posicion donde esta
    n_veces = doc.count(fecha)
    print(f"El nuemro {fecha}, se encuentra en la posicion {n_posicion} y aparece {n_veces} veces.")
