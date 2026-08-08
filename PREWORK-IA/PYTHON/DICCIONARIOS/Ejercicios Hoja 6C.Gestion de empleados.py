
empleados = {}

continuar = True
while continuar:
    print("1.Agregar empleado")
    print("2.Actualizar salario de empleados")
    print("3.Mostrar lista de empleados")
    print("4.Calcular promedio salarial por departamento")
    print("5. Salir")
    opcion = input("Seleccione una opcion:")

    ###Agregar nuevos empleados
    if opcion == "1":
        nombre = input("Ingrese nombre del empleado: ")
        salario = float(input("Ingrese salario del empleado: "))
        departamento = input("Ingrese departamento del empleado: ")

        empleados[nombre] = {
            "salario": salario,
            "departamento": departamento
    }
        print("Empleado agregado exitosamente")
        print(empleados)




        
    ###Actualizar el salario de un empleado existente
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        #Comprobamos la existencia del empleado en la base de datos
        if nombre in empleados:
            #Pedimos nuevo salario del empleado
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            #Actualizamos salario del empleado
            empleados[nombre]["salario"] = nuevo_salario
            print("Salario actualizado exitosamente")
        #Si el empleado no existe en la base de datos lo indicamos
        else:
            print("Empleado no encontrado")
        
    ###Mostrar la lista completa de empleados
    elif opcion == "3":
        print("Lista de empleados: ")
        #Recorremos pares clave valor
        for nombre, datos_empleado in empleados.items():
            salario = datos_empleado["salario"] #Extraemos salario
            departamento = datos_empleado["departamento"] #Extraemos departamento
            print(f" Nombre: {nombre}, Salario: {salario}, Departamento: {departamento}")
    ###Calcular el promedio salarial por departamento.
    elif opcion == "4":
        departamento = input("Ingrese el departamento: ")
        #inicializamos variables
        total_salarios = 0
        contador = 0
        #recorremos datos de los empleados guardados en los valores del dict
        for datos_empleado in empleados.values():
            # si el departamento coincide sumamos el salario.
            if datos_empleado["departamento"] == departamento:
                total_salarios = total_salarios + datos_empleado["salario"]
                contador = contador + 1
        #Si hay empleados en el departamento calculamos el promedio
        if contador > 0:
            promedio_salario = total_salarios / contador
            print(f"Promedio salarial del departamento {departamento}: {promedio_salario}")
        # si no hay empleados en el departamento lo indicamos
        else:
            print(f"No hay empleados en el departamento {departamento}")
    elif opcion == "5":
        continuar = False
        print("A salido del programa. Hasta pronto guapo.")
    else:
        print("Opcion invalida, seleciona una opcion valida.")







