
def intercala_lista(lista1: list, lista2: list) -> list:
    """
    Contrato: Intercala los elementos de una lista.
    
    Pre: Las listas que recibe no deben estar vacías.
    Post: Devuelve a lista1 con los elementos intercalados de la lista2
    
    """
    for elem in range(len(lista2)):
        # Utilizo la variable posición para indicar dónde quiero que inserte los elementos
        # de la lista2.
        posicion = elem * 2 + 1
        
        # Como lista[i] es un único elemento int, no me permite asignarlo (debe ser únicamente
        # con iterables)
        lista1[posicion:posicion] = [lista2[elem]] # Lo hago lista.
        
        
    return lista1


print(intercala_lista([8, 1, 3], [5, 9, 7]))
print(intercala_lista([50, 6, 5, 4],[1, 6]))
print(intercala_lista([9, 12, 18], [7, 1, 3, 8, 4]))