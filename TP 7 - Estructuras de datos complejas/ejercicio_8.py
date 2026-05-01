inventario = dict()

while True:
    print("""
    --- MENÚ ---
    1 - Consultar stock de un producto
    2 - Agregar unidades de un producto
    3 - Agregar nuevo producto
    4 - Salir
""")
    
    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
        print("Error!")
        opcion = input("Ingrese una opción valida: ")

    if opcion == "1":
        
        producto = input("Ingrese el producto a consultar: ").upper()

        while not producto.isalpha() or producto == "":
            print("Error!")
            print("Ingrese correctamente el producto (sin números o espacios vacios)")
            producto = input("Ingrese el producto a consultar: ").upper()

        if not producto in inventario:
            print("-" * 40)
            print("El producto no se encuentra en el inventario")
        else:
            unidades = inventario[producto]
            print(f"{producto} tiene {unidades} unidades")

    elif opcion == "2":

        producto = input("A qué producto desea agregar unidades: ").upper()

        while not producto.isalpha() or producto == "":
            print("Error!")
            print("Ingrese correctamente el producto (sin números o espacios vacios)")
            producto = input("Ingrese el producto a consultar: ").upper()

        if not producto in inventario:
            print("-" * 40)
            print("El producto no se encuentra en el inventario")
        else:
            cantidad = input("¿Cuántas unidades desea agregar? ")

            while not cantidad.isdigit() or int(opcion) < 0:
                print("Error!")
                cantidad = input("Ingrese una opción valida: ")

            inventario[producto] += int(cantidad)
            print("-" * 40)
            print("¡Unidades actualizadas correctamente!")

    elif opcion == "3":

        producto = input("¿Qué producto desea ingresar? ").upper()

        while not producto.isalpha() or producto == "":
            print("Error!")
            print("Ingrese correctamente el producto (sin números o espacios vacios)")
            producto = input("Ingrese el producto a consultar: ").upper()

        if not producto in inventario:
            inventario[producto] = 0
            print("-" * 40)
            print("¡Producto ingresado correctamente!")
        else:
            print("-" * 40)
            print("El producto ya se encuentra en el inventario")

    elif opcion == "4":
        break

print("-" * 40)
print("¡Saliendo del sistema!")