def contar_vocales(palabra: str) -> dict[str, int]:
    """
    Contrato: Permite contar las vocales que se encuentren en una palabra.

    Precondiciones: La variable palabra debe ser una cadena.
    Postcondiciones: En caso de que la palabra haya tenido vocales devuelve
    el diccionario con los contadores actualizados, en caso contrario
    devuelve el diccionario sin cambios.

    """
    dicc = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letra in palabra.casefold():
        if letra in ("a", "e", "i", "o", "u"):
            dicc[letra] += 1

    return dicc


def vocales_frase(frase: str) -> None:
    """
    Contrato: Recibe una frase y permite contar las vocales de cada
    una de sus palabras.

    Precondiciones: La variable frase debe ser una cadena.
    Postcondiciones: No devuelve nada, hace prints en la pantalla.

    """
    frase = frase.split()

    for palabra in frase:
        print(f"La palabra {palabra} contiene:")

        vocales = contar_vocales(palabra)
        for vocal, cantidad in vocales.items():
            print(f"{vocal}: {cantidad}")


def main() -> None:
    """Función principal del programa"""

    frase = "Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales contiene, identificando la cantidad de cada una. Devolver un diccionario con los resultados. Luego desarrollar un programa para leer una frase e invocar a la función por cada palabra que contenga la misma. Imprimir las palabras y la cantidad de vocales hallada."

    vocales_frase(frase)


if __name__ == "__main__":
    main()
