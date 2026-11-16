from typing import Any


def eliminar_claves(
    diccionario: dict[Any, Any], lista: list[Any]
) -> tuple[dict[Any, Any], int]:
    """
    Contrato: Permite eliminar claves de un diccionario y contar cuántas
    de estas fueron borradas.

    Precondiciones: El diccionario no debe estar vacío. Los valores de la
    lista deben ser inmutables.
    Postcondiciones: Devuelve una tupla con el diccionario modificado y un
    entero que representa la cantidad de claves eliminadas.
    En caso de que no se hayan podido eliminar claves devuelve el diccionario
    sin modificaciones y el contador en cero.

    """
    contador = 0

    for clave in lista:
        try:
            diccionario.pop(clave)

        except KeyError:
            print(f"\nLa clave {clave} no existe dentro del diccionario.")

        else:
            contador += 1

    return diccionario, contador


# Todas las claves existen:
assert eliminar_claves({"a": 10, "b": 20, "c": 30}, ["a", "b"]) == ({"c": 30}, 2)

# Ninguna clave existe:
assert eliminar_claves(
    {1: "uno", 2: "dos", (3, 4): "tres y cuatro"}, ["x", "y", "z"]
) == ({1: "uno", 2: "dos", (3, 4): "tres y cuatro"}, 0)

# Alguna de las claves existen:
assert eliminar_claves(
    {(1, 2): "primera", (3, 4): "segunda", (5, 6): "tercera", (7, 8): "cuarta"},
    [(1, 2), (5, 6), (9, 10)],
) == ({(3, 4): "segunda", (7, 8): "cuarta"}, 2)
