'''
SUMA Y VALUEERROR.
Un problema común al solicitar una entrada numérica ocurre cuando las personas 
ingresan texto en lugar de números. Cuando intentas convertir la entrada a un entero (int), 
obtendrás un ValueError. Escribe un programa que solicite dos números. Suma los números 
y muestra el resultado. Captura el ValueError si alguno de los valores de entrada no es 
un número e imprime un mensaje de error amigable. Prueba tu programa ingresando dos números 
y luego ingresando texto en lugar de un número. Envuelve tu código del en un bucle while para 
que el usuario pueda continuar ingresando números incluso si comete un error ingresando texto 
en lugar de un número.
'''


while True:
    '''Aqui se van a sumar dos numeros y se va a introducir un manejo de error.'''
    n1 = input("Introduce un numero;")#pido un numero
    if n1 == "s":#Compruebo si es "s", si lo es me salgo del programa
        print("Saliendo del programa.....")
        break
    n2 = input("Introduce otro numero;")
    if n2 == "s":#Compruebo si es "s", si lo es me salgo del programa
        print("Saliendo del programa.....")
        break

    try:#Aqui compruebo el codigo que puede fallar;
        n1 = int(n1)#n1 tiene que ser int, si no, falla
        n2 = int(n2)#n2 tiene que ser int, si no, falla
    except ValueError:
        print("Este programa solo suma, las letras no son compatibles.")

    else:#El else lo que hace es que solo si el try es exitoso se ejecuta.
        suma = n1 + n2
        print(f"La suma de {n1} y {n2} es: {suma}.")#Si todo eso pasa, printo
#Volver a hacer en modo funcion.