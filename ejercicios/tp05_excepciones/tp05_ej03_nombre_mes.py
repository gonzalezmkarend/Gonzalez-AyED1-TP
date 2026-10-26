
def encuentra_mes(num: int) -> str:
    """
    Contrato: Dado un entero devuelve el mes correspondiente en formato cadena.

    Precondiciones: La variable num debe ser un entero mayor a 0 y no debe estar vacío.
    Postcondiciones: Devuelve el mes que corresponda al número, y en caso de ser inválido devuelve una lista vacía.

    """
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    try:
        return meses[num - 1]

    except IndexError:
        return []


def main() -> None:
    """Función principal"""

    while True:
        num = int(input("\nIngrese el mes en número: "))
        if num:
            break

    mes = encuentra_mes(num)
    if encuentra_mes == []:
        print("\nError. El mes ingresado es inválido.")

    else:
        print(mes)


if __name__ == "__main__":
    main()
