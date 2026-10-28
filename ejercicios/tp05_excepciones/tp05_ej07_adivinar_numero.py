import random

def main() -> None:
    """Función principal."""

    numero_random = random.randint(1, 500)
    intentos = 0

    print("-" * 50)
    print("¡Juguemos a adivinar un número!")
    print("-" * 50)

    while True:
        try:
            intento = int(input("Ingrese un número: "))
            intentos += 1

        except ValueError:
            print("\nUps. Debe ingresar un número entero")

        else:
            if intento > numero_random:
                print("\nEl número a adivinar es menor.")

            elif intento < numero_random:
                print("\nEl número a adivinar es mayor.")

            else:
                print("\n¡Felicidades!¡Adivinaste el número!")
                print(f"Cantidad de intentos: {intentos}")
                break


if __name__ == "__main__":
    main()
