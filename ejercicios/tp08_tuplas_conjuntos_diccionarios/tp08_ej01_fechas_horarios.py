# ---------------BIBLIOTECA---------------

from datetime import datetime, timedelta

# ----------------------------------------


# ----------------------------------------
class NumeroNegativo(Exception):
    pass


class HoraIncorrecta(Exception):
    pass


class MinIncorrectos(Exception):
    pass


# ----------------------------------------

# ----------------FUNCIONES---------------


def verifica_fecha() -> tuple[int]:
    """
    Contrato: Permite que el usuario ingrese una fecha mediante el teclado
    y verifica que esta misma sea válida.

    Precondiciones: No recibe ningún dato
    Postcondiciones: Devuelve una tupla de enteros que representan una fecha
    válida según el calendario.

    """
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))

            datetime(anio, mes, dia)

        except ValueError:
            print("\nError debe ingresar una fecha válida.")

        else:
            print("\nLa fecha ingresada es válida.")
            break

    return dia, mes, anio


def sumar_dias(fecha: tuple[int]) -> tuple[int]:
    """
    Contrato: Permite ingresar por teclado una determinada cantidad
    de días y los suma a una fecha.

    Precondiciones: La variable fecha debe ser una tupla que no puede estar vacía
    y su datos deben ser enteros positivos.
    Postcondiciones: Devuelve una nueva fecha válida que corresponde a los
    días sumados.

    """
    # Desempaqueto las tuplas para poder usar datetime con el formato que acepta.
    dia, mes, anio = fecha

    while True:
        try:
            dias = int(
                input("\nIngrese la cantidad de días que desea sumar a la fecha: ")
            )
            if dias < 0:
                raise NumeroNegativo

        except (ValueError, NumeroNegativo):
            print("\nError. Debe ingresar un número válido.")

        else:
            nueva = datetime(anio, mes, dia)
            nueva = nueva + timedelta(dias)

            # Asigno los valores de nueva a variables individuales
            # con los métodos year, month y day para poder devolverlos
            # como una tupla.
            anio, mes, dia = (nueva.year, nueva.month, nueva.day)

            return dia, mes, anio


def ingresa_horario() -> tuple[int] | None:
    """
    Contrato: Permite ingresar un horario mediante teclado (horas y minutos)
    y verifica que sea válido.

    Precondiciones: No recibe ningún dato.
    Poscondiciones: Devulve una tupla con el tiempo transcurrido o None en
    caso de que hayan pasado más de 24 hs.

    """
    while True:
        try:
            hora = int(input("\nIngrese la hora: "))
            minutos = int(input("Ingrese los minutos: "))

            if hora < 0 or hora > 23:
                raise HoraIncorrecta

            if minutos < 0 or minutos > 59:
                raise MinIncorrectos

        except (ValueError, HoraIncorrecta, MinIncorrectos):
            print("\nError. Los datos ingresados son inválidos.")

        else:
            print("\nLa hora ingresada es válida.")

            return hora, minutos


def calcula_horario(horario1: tuple[int], horario2: tuple[int]) -> tuple[int]:
    """
    Contrato: Calcula el tiempo trascurrido en horas y minutos entre dos
    horarios distintos, siendo el máximo 24 hs (un día)

    Precondiciones: horario1 y horario2 deben ser tuplas cuyos valores sean
    enteros.
    Postcondiciones: Devuelve una tupla que

    """
    h1, m1 = horario1
    h2, m2 = horario2

    hor1 = datetime(2026, 11, 14, h1, m1)
    hor2 = datetime(2026, 11, 14, h2, m2)

    if (h1, m1) > (h2, m2):
        # hor1 pasa a ser el día anterior.
        hor1 - timedelta(1)
        diferencia = hor2 - hor1

    else:
        diferencia = hor2 - hor1

    horas = diferencia.seconds // 3600
    if horas > 24:
        return

    else:
        minutos = diferencia.seconds % 3600 // 60

        return horas, minutos


# -----------------MAIN-----------------


def main() -> None:
    """Función principal"""

    fecha = verifica_fecha()
    if fecha:
        dia, mes, anio = sumar_dias(fecha)
        print(f"\nLa fecha nueva es {dia}/{mes}/{anio}.")

    horario1 = ingresa_horario()
    horario2 = ingresa_horario()

    tiempo = calcula_horario(horario1, horario2)

    if not tiempo:
        print("\nEl sistema no puede calcular más allá de 24hs transcurridas.")

    elif tiempo == (0, 0):
        print("\nNo trasncurrió tiempo, es el mismo horario.")

    else:
        horas, minutos = tiempo
        print(
            f"\nEl tiempo que transcurrió entre ambos horarios fue: {horas}hs y {minutos}min."
        )


if __name__ == "__main__":
    main()
