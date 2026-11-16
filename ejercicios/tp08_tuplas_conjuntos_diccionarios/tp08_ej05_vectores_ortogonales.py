def es_ortogonal(vector1: tuple[int], vector2: tuple[int]) -> bool:
    """
    Contrato: Recibe dos vectores y calcula si son ortogonales, devolviendo
    True si lo son o False en caso contrario.

    Precondiciones: Ambas tuplas deben contener números enteros.
    Postcondiciones: Devuelve un booleano.

    """
    a, b = vector1
    c, d = vector2

    resultado = a * c + b * d

    return resultado == 0


assert es_ortogonal((2, 3), (-3, 2)) == True
assert es_ortogonal((4, 2), (1, -2)) == True
assert es_ortogonal((15, 9), (1, 4)) == False
