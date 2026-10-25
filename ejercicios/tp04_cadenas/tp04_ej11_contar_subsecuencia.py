def encontrar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Contrato: Encuentra una secuencia de caracteres en orden (subcadena) en la totalidad de una frase (cadena)

    Precondiciones: los datos que recibe deben ser cadenas string y no deben estar vacías.
    Postcondiciones: devuelve un entero con la cantidad de veces que se encontró la subcadena en la frase.

    """

    indice = 0
    veces = 0
    cadena = cadena.casefold()
    subcadena = subcadena.casefold()

    for letra in cadena:
        if letra == subcadena[indice]:
            indice += 1

            if indice == len(subcadena):
                veces += 1
                indice = 0

    return veces


def main() -> None:
    """Función principal del programa."""

    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro"

    subcadena = "UADE"

    print(encontrar_subcadena(cadena, subcadena))


if __name__ == "__main__":
    main()
