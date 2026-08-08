'''
CONTRASENA SEGURA
Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. 

Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). 

La función debe devolver un
valor booleano que indique si la contraseña es válida o no. 
'''

#Si tiene que devolver algo como falso o verdadero entonces tendre que empezar dando false o true a el valor.





def validar_contrasena(contrasena):
    if len(contrasena) < 9: #Si la contrasena tiene una longitus menor de 9 devuelve que es falso y no sigue.
        return False

    
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros = False
    tiene_caracter_especial = False


    #Comprobamos si las condiciones que nos han pedido.a
    for caracter in contrasena:#Recorro la contrasena letra por letra y compruebo si se cumple todo.
                                #Se recorre con for. tanto letra por letra como un lista.
        if caracter.isupper():#Comprobamos si tiene mayuscula
            tiene_mayusculas = True
        elif caracter.islower():#Comprobamos si tiene minuscula
            tiene_minusculas = True
        elif caracter.isdigit():#Comprobamos si tiene digitos
            tiene_numeros = True
        else:
            tiene_caracter_especial = True #Si no es ninguno de los anteriores entonces tiene que ser un caracter especial 
                                            # y tendra que ser igual a True.


    #Si todo se cumple devuelve que es verdadero.
    return tiene_mayusculas and tiene_minusculas and tiene_numeros and tiene_caracter_especial
    



















