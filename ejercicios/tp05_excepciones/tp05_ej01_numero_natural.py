def main() -> None:
    """
    Función principal

    """
    while True:
        try:
            num = int(input("\nIngrese un número natural: "))
        except ValueError:
            print(f"\nError. Debe ingresar un número natural.")

        else:
            if num <= 0:
                # Esto cuenta????
                try:
                    raise ValueError("\nEl número ingresado debe ser mayor a 0.")
                except ValueError as mensj:
                    print(mensj)

            else:
                print(f"\nEl número ingresado fue: {num}")
                break


if __name__ == "__main__":
    main()
