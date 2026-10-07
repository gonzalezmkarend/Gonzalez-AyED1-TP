
def es_capicua(cadena: str) -> bool:
    '''
    Contrato: Determina si una cadena de caracteres es capicúa.
    
    Pre: La variable cadena debe ser string.
    Post: Devuelve True en caso de que sí sea capicúa o False en caso contrario.
    
    '''
    # Con " reconocer" me tiraba index out of range porque le asignaba el len(cadena) a largo antes de sacarle el espacio.
    # Obviamente pasó media hora hasta que me di cuenta.

    cadena = cadena.lower().strip()
    largo = len(cadena)

    for x in range(largo // 2):
        if cadena[x] != cadena[largo - 1 - x]:
            return False

    return True

assert es_capicua("Neuquen") == True
assert es_capicua(" reconocer") == True 
assert es_capicua("capicua") == False