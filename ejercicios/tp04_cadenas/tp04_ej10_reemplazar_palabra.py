def reemplaza_palabra(cadena: str, pal_elim: str, pal_nueva: str) -> tuple[str, int]:
    """
    Contrato: Se encarga de modificar una cadena reemplazando una palabra por otra 
    (en cada una de las apariciones de la palabra a reemplazar)

    Precondiciones: Los tres datos que recibe (cadena, pal_elim, pal_nueva) deben ser
    de formato string.
    Postcondiciones: Devuelve una tupla con una nueva cadena modificada y otra con la
    cantidad de veces que apareció la palabra a eliminar (entero).

    """
    cadena = cadena.split()
    veces = [pal for pal in cadena if pal.casefold() == pal_elim.casefold()]

    '''lista = []
    for palabra in cadena:
        if palabra.casefold() == pal_elim.casefold():
            lista.append(pal_nueva)

        else:
            lista.append(palabra)'''

    nueva = [pal_nueva if palabra.casefold() == pal_elim.casefold() else palabra for palabra in cadena]

    print(nueva)

    return (" ".join(nueva), len(veces))



assert reemplaza_palabra(
    "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them",
    "RING",
    "Rang",
) == (
    "One Rang to rule them all, One Rang to find them, One Rang to bring them all and in the darkness bind them",
    3,
)
assert reemplaza_palabra(
    "Pablito clavó un clavito ¿Qué clavito clavó Pablito?", "PABLITO", "Claudito"
) == ("Claudito clavó un clavito ¿Qué clavito clavó Claudito?")


