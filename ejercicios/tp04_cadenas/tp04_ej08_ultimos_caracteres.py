def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Contrato: Extrae de una cadena los últimos n caracteres.

    Precontrato: La variable cadena debe tener formato string y la variable n debe ser un entero positivo.
    Postcontrato: Devuelve un string correspondiente a los caracteres extraidos.

    """
    n = n * -1  # Lo paso a negativo para usarlo como índice negativo.

    return cadena[n:]


print(ultimos_caracteres("cantimplora", 3))
