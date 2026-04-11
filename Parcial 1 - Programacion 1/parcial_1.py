herramientas = []
existencias = []


while True:

    print("""
    --- MENÚ ---
1 - CARGA DE HERRAMIENTAS
2 - CARGA DE EXISTENCIAS
3 - VISUALIZAR INVENTARIO
4 - CONSULTA DE STOCK (EXISTENCIAS)
5 - REPORTE AGOTADOS
6 - ALTA DE NUEVO PRODUCTO
7 - ACTUALIZACIÓN DE STOCK (VENTA/INGRESO)
8 - SALIR
""")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 8:
        print("Error!")
        opcion = input("Ingrese una opción válida: ")

    # 1 CARGA INICIAL DE HERRAMIENTAS
    if opcion == "1":
        cant_herramientas = input("¿Cuántas herramientas va a ingresar? ")

        while not cant_herramientas.isdigit() or int(cant_herramientas) <= 0:
            print("Error! Ingrese un número entero y mayor a 0")
            cant_herramientas = input("Por favor, ingrese una cantidad válida: ")

        cant_herramientas = int(cant_herramientas)

        for cant in range(1, cant_herramientas + 1):
            herramienta = input(f"Ingrese la {cant} herramienta: ")
            while herramienta.upper() in herramientas or herramienta == "":
                print(f"Error! {herramienta} la herramienta ya está cargada o dejó el espacio vacio")
                herramienta = input(f"Por favor, ingrese una herramienta diferente: ")

            herramientas.append(herramienta.upper())
            #LE AGREGO UN 0 A EXISTENCIAS PARA ASI PODER HACER CARGAS SALTEADAS EN LA OPCION 2
            existencias.append(0)
    
    # 2 CARGA DE EXISTENCIAS
    if opcion == "2":
        if len(herramientas) > 0:
            busqueda_herramienta = input("Ingrese la herramienta: ").upper()

            if busqueda_herramienta in herramientas:
                indice = herramientas.index(busqueda_herramienta)
                cant_existencias = input(f"¿Cuánto desea ingresar para {busqueda_herramienta}? ")

                while not cant_existencias.isdigit() or int(cant_existencias) <= 0:
                    print("Error! Ingrese un número entero y mayor a 0")
                    cant_existencias = input(f"¿Cuánto desea ingresar para {busqueda_herramienta}? ")

                #LE AGREGA LAS EXISTENCIAS A LA HERRAMIENTA INGRESADA ANTERIORMENTE
                existencias[indice] = int(cant_existencias)
                print("Existencias actualizadas correctamente!")
            else:
                print("Esa herramienta no existe")
        else:
            print("Error! No podés agregar existencias si no ingresaste antes al menos una herramienta")
    
    # 3 - SE VE EL INVENTARIO ACTUAL
    if opcion == "3":
        print("--- Inventario actual ---")
        print(f"Herramientas: {herramientas}")
        print(f"Existencias: {existencias}")

    # 4 - CONSULTA STOCK (EXISTENCIAS)
    if opcion == "4":
        busqueda_herramienta = input("Ingrese la herramienta: ").upper()

        while not busqueda_herramienta.isalpha() or busqueda_herramienta == "":
            print("Error! escriba correctamente la herramienta a consultar")
            busqueda_herramienta = input("Ingrese la herramienta: ").upper()

        if busqueda_herramienta in herramientas:
            indice = herramientas.index(busqueda_herramienta)
            print(f"Herramienta: {busqueda_herramienta}")
            print(f"Existencias: {existencias[indice]}")
        else:
            print("La herramienta no se encuentra en el listado")

    # 5 - REPORTE DE AGOTADOS
    if opcion == "5":
        agotados = []
        for i in range(len(herramientas)):

            if existencias[i] == 0:
                agotados.append(herramientas[i])
        print(f"Lista de agotados {agotados}")

    # 6 - ALTA DE NUEVO PRODUCTO
    if opcion == "6":
        alta_producto = input("Ingrese la nueva herramienta: ").upper()

        if not alta_producto.isalpha or alta_producto == "" or alta_producto in herramientas:
            print("Error! verifique si la herramienta ya está ingresa o si la escribió correctamente")
        else:
            herramientas.append(alta_producto)
            existencias.append(0)
            print("Herramienta dada de alta exitosamente!")
        

    # 7 - ACTUALIZACIÓN DE STOCK (VENTA/INGRESO)
    if opcion == "7":
        print("1 - VENTA")
        print("2 - INGRESO")
        opcion_actualizacion = input("Seleccione una opción: ")

        while not opcion_actualizacion.isdigit() or int(opcion_actualizacion) < 0 or int(opcion_actualizacion) > 2:
            print("Error! Opción inválida")
            opcion_actualizacion = input("Seleccione una opción válida: ")

        # VENTA
        if opcion_actualizacion == "1":
            print("--- VENTA ---")
            producto_venta = input("Ingrese el producto: ")

            if not producto_venta.upper() in herramientas:
                print("El producto no se encuentra en la lista")
            else:
                indice = herramientas.index(producto_venta.upper())
                if existencias[indice] <= 0:
                    print("Este producto no tiene existencias")
                else:
                    cant_producto_venta = input("¿Cuánto desea vender? ")

                    while not cant_producto_venta.isdigit() or int(cant_producto_venta) <= 0:
                        print("Error!")
                        cant_producto_venta = input("Ingrese correctamente la cantidad ")
                    
                    cant_producto_venta = int(cant_producto_venta)

                    if cant_producto_venta <= existencias[indice]:
                        resta = existencias[indice] - cant_producto_venta
                        existencias[indice] = resta
                        print("Producto vendido con éxito!")
                    else:
                        print("La cantidad solicitada es mayor a la existente!")
        
        # INGRESO POR REPOSICIÓN
        if opcion_actualizacion == "2":
            print("--- INGRESO ---")
            producto_ingreso = input("Ingrese el producto: ")
            
            if not producto_ingreso.upper() in herramientas:
                print("El producto no se encuentra en la lista")
            else:
                indice = herramientas.index(producto_ingreso.upper())
                cant_ingreso = input(f"¿Cuántas unidades de {producto_ingreso.upper()} ingresaron? ")

                while not cant_ingreso.isdigit() or int(cant_ingreso) <= 0:
                    print("Error!")
                    cant_ingreso = input("Ingrese una cantidad válida: ")
                
                cant_ingreso = int(cant_ingreso)

                suma = existencias[indice] + cant_ingreso
                existencias[indice] = suma
                print(f"Stock actualizado exitosamente!")

    # 8 SALIR DEL SISTEMA
    if opcion == "8":
        break

print("Saliendo del sistema...")