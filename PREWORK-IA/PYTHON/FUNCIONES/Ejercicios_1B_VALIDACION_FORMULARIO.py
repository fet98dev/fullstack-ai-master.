
"""
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”
"""
def validar_formulario(nombre,numero_telefono,email):
    """Valida el formulario segun los requisitos"""
    if len(nombre) < 3:
        return False
    if "@" not in email or "." not in email:
        return False
    if len(numero_telefono)!= 9 or not numero_telefono.isdigit():
        return False
    
    return True



nombre = input("Introduce un nombre: ")
numero_telefono = input("Introduce un numero de telefono: ")
email= input("Introduce un email: ")


valido = validar_formulario(nombre,numero_telefono,email)


if valido:
    print("El formulario esta bien escrito.")
else:
    print("El formulario esta mal rellenado.")