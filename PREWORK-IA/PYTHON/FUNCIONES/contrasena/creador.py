'''
Por otro lado puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria.
La función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)
'''

import random
import string


def generar_contrasena_segura(longitud,incluir_mayus=True,incluir_minusculas=True,incluir_numeros=True, incluir_caracteres_especiales=True):
    """Genera una contrasena segura dada una longitud"""
    #Longitud: numero de caracteres de la contrasena
    #Incluir_mayusculas: si true la contrasena incluira al menos una mayuscula
    #Incluir_minuscula: si true la contrasena incluira al menos una minuscula
    #Incluir_numeros: si true la contrasena incluira al menos un numero
    #Incluir_caracteres_especiales: si true la contrasena incluira al menos un caracter especial

    caracteres = ""
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    contrasena = "".join(random.choice(caracteres) for i in range(longitud))

    return contrasena




