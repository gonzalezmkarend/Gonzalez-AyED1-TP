"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""

# Supongo que se refiere a formatos de mail inválidos.


def descompone_correo(correo: str) -> tuple[str]:
    """
    Contrato: Descompone una dirección de correo electrónico y los
    devuelve en una tupla. En caso de que el correo sea inválido
    devuelve una tupla vacía.
    Un correo electrónico válido será aquel que cumpla con los siguientes
    requisitos:
        - usuario (debe existir antes del @)
        - un único @ ()
        - dominio (debe existir después del @)
        - extensión (debe existir al final del dominio, separada por un punto)
        - no pueden haber puntos consecutivos.
        - no pueden haber puntos al inicio ni al final.

    Precondiciones: La variable correo debe tener el formato cadena.
    Postcondiciones: Si el correo es válido devuelve una tupla de cadenas,
    si el correo es inválido devuelve una tupla vacía.

    """
    num_arrobas = correo.count("@")
    if num_arrobas != 1:
        return ()

    else:
        correo = correo.split("@")
        dominio = correo[1].split(".")
        del correo[1]
        correo.extend(dominio)

        # Si hay algún elemento vacío quiere decir que había
        # un . consecutivo, al principio o al final del correo.
        vacio = any(elem == "" for elem in correo)

        if vacio:
            return ()

        if len(correo) < 3:
            return ()

    return tuple(correo)


def main() -> None:
    """Función principal del programa"""
    while True:
        correo = input("\nIngrese la dirección de correo electrónico: ")

        if correo:
            break

    descomp = descompone_correo(correo)
    if len(descomp) == 0:
        print("\nEl correo ingresado es inválido.")

    else:
        print(descomp)


if __name__ == "__main__":
    main()
