def extraer_subcadena(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Contrato: Extrae una subcadena de caracteres predeterminados de otra cadena.

    Precondiciones: La variable cadena debe ser un string. La variable posicion debe ser un entero mayor o
    igual a 0 y la variable cantidad debe ser un entero positivo.
    Postcondiciones: Devuelve la subcadena extraida en formato string.

    """
    final = posicion + cantidad
    # Con slices
    sub = cadena[posicion:final]

    # Sin slices
    sub2 = [cadena[x] for x in range(posicion, final)]
    # sub2 = "".join(sub2)

    return sub


print(extraer_subcadena("El número de teléfono es 4356-7890", 25, 9))
print(extraer_subcadena("A veces resuelvo todo como en intro a la algoritmia", 30, 21))
