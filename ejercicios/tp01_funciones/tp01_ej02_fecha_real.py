def verifica_fechas() -> tuple:
    """
    Contrato: Permite ingresar tres fechas correspondientes a un día, un mes y un año. Verificando que
    sean coherentes individualmente.

    precondiciones: no recibe ningún dato.
    postcondiciones: devuelve tres datos enteros positivos dd/mm/aaa en una tupla.

    """
    while True:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))
        if (dia < 1 or dia > 31) and (mes < 1 or mes > 12) and anio < 1 or anio > 9999:
            break

    return (dia, mes, anio)


def verifica_validez(dia=int, mes=int, anio=int) -> bool:
    """
    Contrato: Verifica la validez de la fecha que recibe en conjunto.

    pre: los datos deben ser enteros positivos.
    post: si la fecha es válida devuelve True, en caso contrario devuelve False.

    """
    valido = True

    # si el mes es febrero, verifico primero si el año es bisiesto.
    bisiesto = False
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            bisiesto = True

        if bisiesto == True and dia > 29:
            valido = False

        elif dia > 28:
            valido = False

        elif mes in (4, 6, 9, 11):
            if dia > 30:
                valido = False

        elif mes in (1, 3, 5, 7, 8, 10, 12):
            if dia > 31:
                valido = False

        return valido


def main() -> None:
    dia, mes, anio = verifica_fechas()
    es_valido = verifica_validez(dia, mes, anio)
    if es_valido == True:
        print(f"La fecha {dia}/{mes}/{anio} es válida.")

    else:
        print(f"La fecha {dia}/{mes}/{anio} es inválida.")


if __name__ == "__main__":
    main()

assert verifica_validez(15, 8, 2026) == True
assert verifica_validez(22, 2, 2025) == True
assert verifica_validez(29, 2, 1900) == False
assert verifica_validez(31, 4, 2000) == False
