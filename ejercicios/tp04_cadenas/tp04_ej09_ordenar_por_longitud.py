def largo_palabra(palabra: str) -> int:
    """
    Contrato: Cuenta la cantidad de caracteres de una palabra ya sean números o letras.
    No incluye los signos de puntuación.

    Precondiciones: La variable palabra debe ser string.
    Postcondiciones: Devuelve un entero que representa los caracteres de la palabra.

    """
    largo = [letra for letra in palabra if letra.isalnum()]
    # Uso esta función para definir el largo sin tener en cuenta los signos de puntuación.

    return len(largo)


def ordena_longitud(cadena: str) -> str:
    """
    Contrato: Ordena una cadena de menor a mayor según la cantidad de caracteres de cada palabra,
    independientemente de si sea letra o número.

    Precondiciones: La varable cadena debe tener formato string.
    Postcondiciones: Devuelve un string ordenado de menor a mayor.

    """
    cadena = cadena.split()
    ordenadas = sorted(cadena, key=largo_palabra)

    return " ".join(ordenadas)


print(
    ordena_longitud(
        "Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk, agh burzum-ishi krimpatul"
    )
)
