agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de inglés",
    ("Miercoles", "12:00"): "Entrega TP",
    ("Jueves", "20:00"): "Fútbol",
    ("Viernes", "15:00"): "Veterinario"
}

#El usuario ingresa el dia y la hora a consultar
dia_buscado = input("Ingrese el dia a consultar: ").capitalize()
hora_buscada = input("Ingrese la hora (ej: 15:00): ")

#Creo la tupla para poder comparar
datos = (dia_buscado, hora_buscada)

#Verifico si los datos existen en la agenda
if datos in agenda:
    actividad = agenda[datos]
    print(f"El dia {dia_buscado} a las {hora_buscada} tengo: {actividad}")
else:
    print(f"No hay actividades ni tareas para el dia {dia_buscado} a las {hora_buscada}")