a = 10
b = input("Introduce un número: ")
result = a / b #Error: TypeError. "b" es un string y no se puede dividir un int por un string.
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[5]) #Error: IndexError. "numbers[5]" el indice que se desea imprimir está fuera de rango dentro del índice de la lista, la cual llega hasta 2.