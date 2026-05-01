try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except:
    print("Error en la operación!")


try:
    numbers = [1, 2, 3]
    print("-")
    print(numbers[5])
except:
    print("-")
    print("Error!")