
from random import randint

def genera_lista(n: 30) -> list[int]:
    '''
    Contrato: Genera una lista de números aleatorios del 1 al 100 inlcusive, la cantidad de números es determinada por n.
    
    pre: el dato n debe ser entero y positivo.
    post: devuelve una lista de números enteros y positivos.
    
    '''

    lista = [randint(1, 100) for x in range(n)]

    return lista


def lista_repetida(lista: list[int]) -> bool:
    '''
    Contrato: Recibe una lista y la recorre verificando si tiene números repetidos
    
    pre: La lista que recibe no debe estar vacía y sus elementos deben ser enteros.
    post: Devuelve un booleano. True si tiene elementos repetidos, False en caso contrario.
    
    '''

    return len(lista) == len(set(lista))


def nueva_lista(lista: list[int]) -> list[int]:
    '''
    Contrato: Genera una nueva lista con los elementos únicos de la lista original.
    
    pre: La lista que recibe no debe estar vacía.
    post: Devuelve una lista de enteros.
    
    '''
    lista_nueva = set(lista)

    return lista_nueva


def main() -> None:
    while True:
        n = int(input("Ingrese un número: "))
        if n > 0:
            break

    lista = genera_lista(n)
    print(lista)
    
    if lista_repetida(lista):
        print("La lista no contiene valores repetidos.")

    else:
        print("La lista contiene valores repetidos")

    lista_nueva = nueva_lista(lista)
    print(lista_nueva)
    

if __name__ == "__main__":
    main()