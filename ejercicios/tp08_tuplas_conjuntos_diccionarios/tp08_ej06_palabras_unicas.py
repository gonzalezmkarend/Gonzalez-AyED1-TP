def elimina_puntuacion(palabra: str) -> str:
    """
    Contrato: Recibe una palabra y elimina los signos de puntuación
    en caso de que los posea.

    Precondiciones: La palabra debe ser de formato cadena.
    Postcondiciones: Devuelve una cadena con la palabra sin
    signos de puntuación.

    """
    palabra = palabra.casefold()
    nueva = [letra for letra in palabra if letra.isalnum()]

    return "".join(nueva)


def elimina_repetidos(frase: str) -> set[str]:
    """
    Contrato: Recibe una cadena que corresponde a una frase y
    elimina las palabras repetidas, dejando un único ejemplar
    de cada una.

    Precondiciones: La variable frase debe ser una cadena.
    Poscondiciones: Devuelve un conjunto de cadenas.

    """
    frase = frase.split()
    frase_limpia = [elimina_puntuacion(palabra) for palabra in frase]

    return set(frase_limpia)


def largo_palabra(palabra: str) -> int:
    """
    Contrato: Cuenta la cantidad de caracteres de una palabra.

    Precondiciones: La variable palabra debe ser una cadena.
    Postcondiciones: Devuelve un entero que representa el largo de
    la palabra.

    """
    largo = [letra for letra in palabra]

    return len(largo)


def ordena_longitud(sin_repetidos: set[str]) -> tuple[int]:
    """
    Contrato: Ordena la frase según el largo de cada palabra en
    orden ascendente.

    Precondiciones: el conjunto que recibe no debe estar vacío y
    sus valores deben ser cadentas.
    Postcondiciones: Devuelve una tupla de cadenas ordenadas por
    el largo de cada palabra.

    """
    sin_repetidos = list(sin_repetidos)

    ordenada = sorted(sin_repetidos, key=largo_palabra)

    return tuple(ordenada)


def main() -> None:
    """Función principal del programa."""
    while True:
        frase = input("\nIngrese una frase: ")

        if frase:
            break

    sin_repetidos = elimina_repetidos(frase)

    print(ordena_longitud(sin_repetidos))


if __name__ == "__main__":
    main()
