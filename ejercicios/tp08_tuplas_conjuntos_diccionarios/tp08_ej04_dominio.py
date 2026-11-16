def compara_fichas(ficha1=tuple[int], ficha2=tuple[int]) -> bool:
    """
    Contrato: Compara si dos fichas encajan (encajan cuando tienen
    al menos un número en común) Si encajan devuelve True y en
    caso contrario false.

    Precondiciones: Ambas tuplas (ficha1 y ficha2) deben contener dos
    datos enteros.
    Postcondiciones: Devuelve un booleano.

    """

    encajan = set(ficha1) & set(ficha2)

    return bool(encajan)


assert compara_fichas((1, 2), (3, 4)) == False
assert compara_fichas((1, 3), (2, 3)) == True
assert compara_fichas((9, 12), (9, 13)) == True
