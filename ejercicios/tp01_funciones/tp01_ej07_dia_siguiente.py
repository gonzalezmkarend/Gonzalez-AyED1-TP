# Reciclé las funciones de fecha real :)
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
        if (
            (dia >= 1 and dia <= 31)
            and (mes >= 1 and mes <= 12)
            and (anio >= 1 and anio <= 9999)
        ):
            break

    return (dia, mes, anio)


def verifica_validez(dia=int, mes=int, anio=int) -> bool:
    """
    Contrato:  Verifica la validez de la fecha en conjunto.

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


def dia_siguiente(dia: int, mes: int, anio: int) -> tuple:
    """
    Contrato: Recibe tres enteros positivos que representan una fecha en formato dd/mm/aaaa y devuelve otra fecha
    correspondiente al dia siguiente, actualizando mes y año en caso de ser necesario.

    pre: los datos dia, mes y anio deben ser enteros positivos.
    post: la fecha del día siguiente se devuelve en conjunto dentro de una tupla.

    """

    dia += 1
    valido = verifica_validez(dia, mes, anio)

    if valido == False:
        dia = 1
        mes += 1

        if mes == 13:
            anio += 1
            mes = 1

        valido = verifica_validez(dia, mes, anio)
        if valido == True:
            return (dia, mes, anio)

    else:
        return (dia, mes, anio)


def suma_dias(d=int, m=int, a=int, dias=int) -> tuple:
    """
    Contrato: Suma una cantidad determinada de días a una fecha y los devuelve en una tupla.

    pre: todos los datos deben ser positivos y enteros.
    post: devuelve una tupla con los días modificados.

    """
    for dias in range(dias):
        d, m, a = dia_siguiente(d, m, a)

    return (d, m, a)


def dias_entre(dia1=int, mes1=int, anio1=int, dia2=int, mes2=int, anio2=int) -> int:
    """
    Contrato: Calcula la cantidad de días transcurridos entre dos fechas distintas.

    pre: todos los datos ingresados deben ser enteros y positivos.
    Los datos correspondientes a la segunda fecha no pueden ser menores a los de la primera.
    post: devuelve un entero igual o mayor a 0 que representan los días.

    """
    assert (dia1, mes1, anio1) <= (dia1, mes2, anio2)
    cont = 0

    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        dia1, mes1, anio1 = dia_siguiente(dia1, mes1, anio1)
        cont += 1

    return cont


def menu() -> None:
    print("-" * 50)
    print("MENU")
    print("-" * 50)
    print("\nOpción 1: Calcular día siguiente.")
    print("Opción 2: Sumar días.")
    print("Opción 3: Calcular días entre dos fechas.")
    print("Opción 4: Salir")
    print("")


def main() -> None:
    menu()
    while True:
        op = input("Ingrese una opción: ")

        if op == "4":
            print("\nSaliendo...")
            break

        elif op == "1":
            dia, mes, anio = verifica_fechas()

            es_valido = verifica_validez(dia, mes, anio)
            if es_valido == False:
                print("\nLa fecha ingresada es inválida.")

            else:
                d, m, a = dia_siguiente(dia, mes, anio)
                print(f"\nEl dia siguiente al ingresado es: {d}/{m}/{a}.")

        elif op == "2":
            while True:
                sumar_dias = int(
                    input("\nIngrese la cantidad de días que desea sumar: ")
                )
                if sumar_dias > 0:  # Se debe sumar al menos un día.
                    break

            day, month, year = suma_dias(dia, mes, anio, sumar_dias)
            print(
                f"\nA la fecha {dia}/ {mes}/ {anio} se le sumaron {sumar_dias} días. La nueva fecha es: {day}/{month} {year}"
            )

        elif op == "3":
            dia1, mes1, anio1 = verifica_fechas()
            dia2, mes2, anio2 = verifica_fechas()

            if (dia1, mes1, anio1) > (dia2, mes2, anio2):
                print("La segunda fecha no puede ser menor que la primera.")

            else:
                cont = dias_entre(dia1, mes1, anio1, dia2, mes2, anio2)
                if cont > 0:
                    print(
                        f"La cantidad de días transcurridos entre ambas fechas fue: {cont}."
                    )

                else:
                    print("Ambas fechas son iguales.")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
