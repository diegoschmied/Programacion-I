try:
    numero = int(input("Ingrese un número: "))
    numero = float(numero)

except ValueError:
    print("Error!")
    print("Ingrese un número válido")

except Exception as e:
    print("Error!")
    print("Se detectó el siguiente error: ", type(e).__name__)

else:
    print(f"El valor ingresado es válido: {numero}")

finally:
    print("Finalizó el sistema")