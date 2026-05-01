a = 10
b = int(input("Introduce un número: ")) #Se corrige la entrada del valor para la variable "b" para que este sea un entero
result = a / b #Ahora puede realizarce la división ya que ambos valores son enteros
print(f"Resultado: {result}")

numbers = [1, 2, 3, 9, 7, 0] #Se añaden elementos a la lista para que a la hora se imprimir por pantalla el elemento en el índice 5, este no arroje error
print(numbers[5]) #Ahora si imprime por pantalla el elemento del indice 5 el cual es 0