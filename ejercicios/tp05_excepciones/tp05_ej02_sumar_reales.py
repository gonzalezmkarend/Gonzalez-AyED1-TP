def suma_num(num1: str, num2: str) -> float:
    """
    Contrato: Recibe dos cadenas de caracteres que representan dos números reales. Los suma y devuelve su resultado como número flotante.
    En caso de que los datos que reciba no sean válidos, devuelve un -1

    Precondiciones: Las cadenas no deben estar vacías.
    Postcondiciones: En caso de que los números sean válidos devuelve el resultado de la suma, en caso contrario devuelve un -1

    """
    num = -1
    try:
        num1 = float(num1)

    except ValueError:
        return num

    else:
        try:
            num2 = float(num2)

        except ValueError:
            return num

        else:
            return num1 + num2


def main() -> None:
    while True:
        num1 = input("\nIngrese el primer número: ")
        if num1:
            break

    while True:
        num2 = input("\nIngrese el segundo número: ")
        if num2:
            break

    num = suma_num(num1, num2)
    if num == -1:
        print("\nError. Se ingresaron datos inválidos.")

    else:
        print(f"\nLa suma de los números fue: {num}")


if __name__ == "__main__":
    main()
