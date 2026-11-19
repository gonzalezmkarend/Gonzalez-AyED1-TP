# Sin finalizar.


class MayorQueBillon(Exception):
    pass


def descompone_centena(num: int) -> tuple[int]:
    """
    Contrato: Recibe un entero de dos o tres dígitos mayores a 20 y los
    descompone en tres variables que representan su centena, decena, y unidad.
    Estas variables pueden volver con un entero de un dígito o un entero de
    dos dígitos si es un número considerado especial (por ej: 15).

    Precondiciones: La variable num debe ser entera y no debe ser mayor a 999.
    Postcondiciones: Devuelve una tupla cuyos valores son enteros.

    """

    centena = num // 100
    decena = num % 100
    if decena >= 10 and decena <= 20:
        return (centena, decena, 0)

    else:
        decena = num // 10 % 10
        unidad = num % 10

        return (centena, decena, unidad)


def descompone_mil_mill(num: int) -> tuple[int, bool]:
    """
    Contrato: Recibe un número entero entre 1.000 y 999.999.999 y los separa
    en dos o tres valores dependiendo de si es mayor o menor a un millón.
    Devuelve una tupla que contiene cuatro valores:
    La primera centena, la centena de los miles y la centena de los millones y
    si el número es apócope devuelve una variable booleana del mismo nombre.

    Precondiciones: La variable num debe ser entera.
    Postcondiciones:

    """
    apocope = False

    if num >= 1_000_000:
        millon = num // 1_000_000
        mil = num % 1_000_000 // 1_000
        cent = num % 1_000

        if str(mil).endswith("1"):
            apocope = True

        return (millon, mil, cent, apocope)

    else:
        mil = num % 1_000_000 // 1_000
        cent = num % 1_000

        if str(mil).endswith("1"):
            apocope = True

        return (mil, cent, apocope)


def centenas_a_cadena(num: int, cadenas: dict) -> str:
    """
    Contrato: Expresa en letras cualquier número ingresado desde el 0 hasta el
    999 inclusive.

    Precondiciones: la variable num debe ser entera.
                    la varible centena debe ser un diccionario y no debe
                    estar vacío.
    Postcondiciones: devuelve una cadena de letras.

    """
    if num <= 20:
        return cadenas["ESPECIALES"][num]

    elif num <= 999:
        cent, dec, uni = descompone_centena(num)

        if cent == 0 and dec >= 2 and dec <= 9 and uni == 0:
            return cadenas["DECENAS_COMB"][dec - 3]

        if cent == 0 and dec >= 2 and dec <= 9 and uni >= 1:
            return cadenas["DECENAS_COMB"][dec - 3] + " y " + cadenas["ESPECIALES"][uni]

        if cent == 1 and dec == 0 and uni == 0:
            return cadenas["UNICOS"][0]

        if cent >= 1 and dec == 0 and uni >= 1:
            return (
                cadenas["CENTENAS_COMBINABLES"][cent - 1]
                + " "
                + cadenas["ESPECIALES"][uni]
            )

        if cent in (1, 2, 3, 4, 5, 6, 7, 8, 9) and dec >= 10 and dec <= 20 and uni == 0:
            return (
                cadenas["CENTENAS_COMBINABLES"][cent - 1]
                + " "
                + cadenas["ESPECIALES"][dec]
            )

        if cent in (1, 2, 3, 4, 5, 6, 7, 8, 9) and dec >= 3 and uni == 0:
            return (
                cadenas["CENTENAS_COMBINABLES"][cent - 1]
                + " "
                + cadenas["DECENAS_COMB"][dec - 2]
            )

        if cent in (1, 2, 3, 4, 5, 6, 7, 8, 9) and dec >= 3 and uni >= 1:
            return (
                cadenas["CENTENAS_COMBINABLES"][cent - 1]
                + " "
                + cadenas["DECENAS_COMB"][dec - 2]
                + " y "
                + cadenas["ESPECIALES"][uni]
            )


def miles_a_cadena(mil: int, centena: int, apocope: bool, cadenas: dict) -> str:
    """
    Contrato:

    Precondiciones:
    Postcondiciones:

    """
    centenas = centenas_a_cadena(centena)
    cent, dec, uni = descompone_centena

    return centenas


def main() -> None:
    """Función principal del programa."""

    cadenas = {
        "ESPECIALES": (
            "cero",
            "uno",
            "dos",
            "tres",
            "cuatro",
            "cinco",
            "seis",
            "siete",
            "ocho",
            "nueve",
            "diez",
            "once",
            "doce",
            "trece",
            "catorce",
            "quince",
            "dieciséis",
            "diecisiete",
            "dieciocho",
            "diecinueve",
            "veinte",
        ),
        "DECENAS_COMB": (
            "veinti",
            "treinta",
            "cuarenta",
            "cincuenta",
            "sesenta",
            "setenta",
            "ochenta",
            "noventa",
        ),
        "UNICOS": ("cien", "un", "ún", "mil", "millón", "millones"),
        "CENTENAS_COMBINABLES": (
            "ciento",
            "doscientos",
            "trescientos",
            "cuatrocientos",
            "quinientos",
            "seiscientos",
            "setecientos",
            "ochocientos",
            "novecientos",
        ),
    }
    while True:
        try:
            num = int(input("\nIngrese un número: "))

            if num >= 1_000_000_000_000:
                raise MayorQueBillon

        except (ValueError, MayorQueBillon):
            print("\nError. Debe ingresar un número entero menor que 1 billón.")

        else:
            break

    if num <= 999:
        print(centenas_a_cadena(num, cadenas))

    elif num <= 999_999:
        if num == 1_000:
            print(cadenas["UNICOS"][3])

        else:
            mil, cent, apocope = descompone_mil_mill(num)
            print(miles_a_cadena(mil, cent, apocope, cadenas))

    else:
        if num == 1_000_000:
            print(cadenas["UNICOS"][1] + " " + cadenas["UNICOS"][4])

        else:
            mill, mil, cent, apocope = descompone_mil_mill(num)


if __name__ == "__main__":
    main()
