try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except ValueError:
    print("Debe ingresar un número válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e: 
    print("Se detectó el siguiente error:", type(e).__name__)

try:
    numbers = [1, 2, 3]
    print("-")
    print(numbers[5])
except IndexError:
    print("-")
    print("Error! índice fuera de rango")