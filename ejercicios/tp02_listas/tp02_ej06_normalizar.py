
def normaliza_lista(lista: list[int]) -> list[float]:
    '''
    Contrato: Normaliza los enteros de la lista para que la suma de sus elementos de un total de: 1.0.

    Pre: La lista no debe estar vacía y sus elementos deben ser postitivos y enteros.
    Post: Devuelve una lista de flotantes.
    
    '''

    total = sum(lista)
    lista_normalizada = [num / total for num in lista]

    return lista_normalizada

assert normaliza_lista([1, 1, 2]) == [0.25, 0.25, 0.5]
assert normaliza_lista([8, 5, 7]) == [0.4, 0.25, 0.35]
assert normaliza_lista([6, 9, 10]) == [0.24, 0.36, 0.4]


