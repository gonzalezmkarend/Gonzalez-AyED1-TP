def ingresa_num() -> tuple:
    """
    Contrato: Ingresa los números a evaluar y los devuelve en una tupla.

    Precondiciones: no rececibe datos.
    Postcondiciones: devuelve una tupla con tres números enteros positivos.

    """
    while True:
        a = int(input("Ingrese un número A: "))
        b = int(input("Ingrese un número B: "))
        c = int(input("Ingrese un número C: "))

        if (a > 0) and (b > 0) and (c > 0):
            break

    return (a, b, c)


def mayor_unico(a: int, b: int, c: int) -> int:
    """
    Contrato: Compara todos los datoss y devuelve el mayor de los tres números ingresados.

    pre-condiciones: a, b y c deben ser enteros positivos.
    post-condiciones: devuelve un solo valor.

    """
    mayor = 0
    assert a > 0
    assert b > 0
    assert c > 0

    if a > b:
        if a > c:
            mayor = a

    if b > a:
        if b > c:
            mayor = b

    if c > a:
        if c > b:
            mayor = c

    if mayor > 0:
        return mayor

    else:
        return -1


def main() -> None:
    a, b, c = ingresa_num()
    num = mayor_unico(a, b, c)
    if num > 0:
        print(f"El único número mayor de los ingresados fue: {num}")

    else:
        print("No se ingresaron mayores únicos.")


if __name__ == "__main__":
    main()
