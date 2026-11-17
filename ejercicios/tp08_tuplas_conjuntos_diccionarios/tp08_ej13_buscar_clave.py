from typing import Any


def buscar_clave(diccionario: dict[Any, Any], dato: Any) -> tuple[Any]:
    """
    Contrato: Devuelve las claves que compartan el mismo valor. El
    valor a buscar es recibido como parámetro.


    Precondiciones: El primer parámetro debe ser un diccionario y la
    variable dato no debe estar vacía.
    Postcondiciones: Devuelve una tupla con las claves encontradas.
    En caso de no haber coincidencia devuelve la tupla vacía.

    """
    claves = []
    for clave, valor in diccionario.items():
        if valor == dato:
            claves.append(clave)

    return tuple(claves)


dicc1 = {"carpeta": 1500, "lapicera": 500, "cuaderno": 1500, "goma": 300, "regla": 500}
dicc2 = {10: "rojo", 20: "azul", 30: "verde", 40: "rojo", 50: "amarillo"}
dicc3 = {(1, 2): [10, 20], (3, 4): [30, 40], (5, 6): [50, 60], (7, 8): [10, 20]}

assert buscar_clave(dicc1, 1500) == ("carpeta", "cuaderno")
assert buscar_clave(dicc2, "azul") == (20,)
assert buscar_clave(dicc3, [100, 200]) == ()
