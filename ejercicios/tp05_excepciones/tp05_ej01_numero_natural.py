class NumeroNegativo(Exception):
    pass


def main() -> None:
    """
    Función principal

    """
    while True:
        try:
            num = int(input("\nIngrese un número natural: "))
            if num <= 0:
                raise NumeroNegativo

        except (ValueError, NumeroNegativo):
            print(f"\nError. Debe ingresar un número natural.")
        except NumeroNegativo:
            print("\n#El número ingresado debe ser mayor a 0.")

        except Exception as error:
            print(error)

        else:
            # if num <= 0:
            # Esto cuenta????
            #   try:
            #     raise ValueError("\nEl número ingresado debe ser mayor a 0.")
            #  except ValueError as mensj:
            #  print(mensj)

            # else:
            print(f"\nEl número ingresado fue: {num}")
            break


if __name__ == "__main__":
    main()
