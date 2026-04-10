herramientas = []
existencias = []


while True:

    print("""
    MENÚ
1 - CARGA DE HERRAMIENTAS
2 - CARGA DE EXISTENCIAS
3 - VISUALIZAR INVENTARIO
5 - SALIR
""")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
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
                cant_existencias = int(input(f"¿Cuánto desea ingresar para {busqueda_herramienta}? "))
                #LE AGREGA LAS EXISTENCIAS A LA HERRAMIENTA INGRESADA ANTERIORMENTE
                existencias[indice] = cant_existencias
                print("Existencias actualizadas correctamente!")
            else:
                print("Esa herramienta no existe")
        else:
            print("Error! No podés agregar existencias si no ingresaste antes al menos una herramienta")
    
    if opcion == "3":
        print("--- Inventario actual ---")
        print(f"Herramientas: {herramientas}")
        print(f"Existencias: {existencias}")

    # 5 SALIR DEL SISTEMA
    if opcion == "5":
        break

print("Saliendo del sistema...")
print(herramientas)
print(existencias)

