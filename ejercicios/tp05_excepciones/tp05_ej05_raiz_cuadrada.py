from math import sqrt

while True:
    try:
        num = int(input("\nIngrese un número para calcular la raíz cuadrada: "))
    except ValueError:
        print("\nError. Debe ingresar un número entero.")

    else:
        if num:
            try:
                resultado = sqrt(num)
            except ValueError:
                print(
                    "\nError. No se puede calcular la raíz cuadrada de un número negativo. Ingrese un número positivo."
                )

            else:
                print(resultado)
                break
