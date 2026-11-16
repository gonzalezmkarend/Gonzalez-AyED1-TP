def multiplica_num(num: int) -> dict[int]:
    """
    Contrato: Permite generar un diccionario con las multiplicaciones
    del 1 al 12 de un número entero que recibe como parámetro.

    Precondiciones: La variable número debe ser entera.
    Postcondiciones: Devuelve un diccionario de enteros.

    """
    diccionario = {clave: clave * num for clave in range(1, 13)}

    return diccionario


def main() -> None:
    """Función principal"""

    while True:
        try:
            num = int(input("\nIngrese un número: "))

        except ValueError:
            print("\nError. El número debe ser entero.")

        else:
            tabla = multiplica_num(num)

        if num:
            break

    print(f"\nLa tabla de multiplicar del número {num} es:")
    print(tabla)


if __name__ == "__main__":
    main()
