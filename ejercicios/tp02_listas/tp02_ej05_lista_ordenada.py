
def esta_ordenada(lista: list) -> bool:
    '''
    Contrato: Verifica si la lista que recibe está ordenada de forma ascendente.
    
    Pre: La lista que recibe no debe estar vacía.
    Post: Devuelve un booleano. True en caso de que esté ordenada correctamente, False en caso contrario.
    
    '''

    lista_sortiada = sorted(lista) # Quizá sea una resolución nacida de la pereza...

    return lista == lista_sortiada


assert esta_ordenada([1, 2, 3, 4]) == True
assert esta_ordenada([5, 7, 90, 100]) == True
assert esta_ordenada([8, 6, 7, 1]) == False
assert esta_ordenada(["a", "b", "c"]) == False
