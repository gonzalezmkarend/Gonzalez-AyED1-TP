def elimina_num(conjunto: set[int], num: int) -> set[int] | None:
    """
    Contrato: Permite eliminar un número de un conjunto.

    Precondiciones: El conjunto no debe estar vacío y la variable
    num debe ser entera.
    Postcondiciones: Si el elemento no existe, no devuelve nada.
    Si el elemento se encuentra en el conjunto lo elimina y lo
    devuelve.

    """
    try:
        conjunto.remove(num)

    except KeyError, Exception:
        return None

    else:
        return conjunto


def main() -> None:
    """Función principal"""

    conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    while True:
        try:
            num = int(input("\nIngrese el número que desee eliminar: "))

        except ValueError, Exception:
            print("\nError. Debe ingresar un número entero.")

        else:
            conj = elimina_num(conjunto, num)

            if conj:
                print(conj)

            else:
                print("\nEl número ingresado no se encuentra en el conjunto.")

        if num == -1:
            break


if __name__ == "__main__":
    main()
