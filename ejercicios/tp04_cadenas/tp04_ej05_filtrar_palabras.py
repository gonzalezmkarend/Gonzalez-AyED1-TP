def filtrar_palabras(frase: str, num: int) -> str:
    """
    Contrato: Guarda las palabras de una frase que tengan un número de caracteres mayor o igual a num.

    Precondiciones: La frase debe ser en formato string y el número debe ser entero
    y positivo.
    Postcondiciones: Devuelve un único string con las palabras filtradas.

    """
    frase = frase.split()

    # Con ciclos normales:
    palabras = []
    for palabra in frase:
        if len(palabra) >= num:
            palabras.append(palabra)

    # Con listas por comprensión:
    palabras = [pal for pal in frase if len(pal) >= num]

    # Con filter:
    palabras = list(filter(lambda pal: len(pal) >= num, frase))

    return " ".join(palabras)


palabras = filtrar_palabras(
    "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them",
    5,
)

print(palabras)
