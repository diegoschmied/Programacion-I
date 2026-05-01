asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]
print(f"Lista original {asistencias}")

asistencias_sin_repetidos = set(asistencias)
print(f"Empleados que asistieron al menos una vez {asistencias_sin_repetidos}")

#Creo el diccionario
recuento_asistencias = dict()

for nombre in asistencias:
    if nombre in recuento_asistencias:
        recuento_asistencias[nombre] += 1
    else:
        recuento_asistencias[nombre] = 1

print("Cantidad de asistencias por empleado: ")
for nombre, veces in recuento_asistencias.items():
    print(f"{nombre}: {veces} veces")
