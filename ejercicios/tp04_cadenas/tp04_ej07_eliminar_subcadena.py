def eliminar_subcadena(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Contrato: Elimina una subcadena de una cadena.

    Precondiciones: La variable cadena debe ser un string. La variable cantidad deber ser un entero
    positivo. La variable
    Postcondiciones: Devuelve un string correspondiente a la cadena que resulta de la eliminación
    de la subcadena.

    """
    salto = posicion + cantidad

    # Con slices:
    parte1 = cadena[:posicion]
    parte2 = cadena[salto:]
    sub1 = parte1 + parte2

    # Sin slices:
    sub2 = [cadena[x] for x in range(len(cadena)) if x < posicion or x >= salto]
    # for x in range(len(cadena)):
    #   if x < posicion or x >= salto:
    #      sub2.append(cadena[x])

    sub2 = "".join(sub2)

    return sub1


print(eliminar_subcadena("A ver si funciona", 0, 9))

assert eliminar_subcadena("A ver si funciona", 0, 9) == "funciona"
assert eliminar_subcadena("123456789", 2, 5) == "1289"
