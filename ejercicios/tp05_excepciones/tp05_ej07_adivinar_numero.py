import random
random.seed(0)  

def main() -> None:
    '''Función principal.'''

    numero_random = random.randint(1,500)
    intentos = 0

    print("-"*50)
    print("¡Juguemos a adivinar un número!")
    print("-"*50)

    while True:
        try:
            intento = int(input("Ingrese un número: "))
            
        except ValueError:
            print("\nUps. Debe ingresar un número entero")
            intentos += 1

        else:
            if intento > numero_random:
                print("\nEl número a adivinar es menor.")
                intentos += 1

            elif intento < numero_random:
                print("\nEl número a adivinar es mayor.")
                intentos += 1

            else:
                print("\n¡Felicidades!¡Adivinaste el número!")
                print(f"Cantidad de intentos: {intentos}")
                break
                

if __name__ == "__main__":
    main()