"""Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. """

a = int(input("Ingrese un número A: "))
b = int(input("Ingrese un número B: "))

lista = [num for num in range(a, b+1) if num % 7 == 0 and num % 5 != 0]
print(lista)