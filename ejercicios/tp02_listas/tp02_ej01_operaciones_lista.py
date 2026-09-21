
from random import randint

def carga_lista() -> list[int]:
    '''
    Contrato: genera una lista de valores aleatorios entre 1000 y 9999. La cantidad de valores también es aleatoria.
    
    pre: no recibe ningún parámetro.
    post: devuelve una lista de enteros positivos.
    
    '''
    cant = randint(10, 99)
    lista = [randint(1_000, 9_000) for x in range(cant)]

    return lista

def producto(lista = list[int]) -> int:
    '''
    Contrato: multiplica los valores de la lista.
    
    pre: la lista no debe estar vacía.
    post: devuleve un entero con el total de la multiplicación.
    
    '''
    producto = 1
    for num in lista:
        producto *= num

    return producto


def elimina(lista = list[int], valor = int) -> list[int]:
    '''
    Contrato: Elimina todas las apariciones del valor ingresado que se encuentren en la lista.
    
    pre: la lista no debe estar vacía el y el valor debe ser entero.
    post: devuelve la lista sin los valores que se sacaron.
    
    '''
    for num in lista:
        if num == valor:
            lista.pop(valor)

    return lista


def es_capicua(lista = list[int]) -> bool:
    '''
    contrato: determina si una lista es capicúa.
    
    pre: la lista no debe estar vacía
    post: devuelve verdadero o falso.
    
    '''

    return lista == lista[ : :-1]

def main() -> None:
    lista = carga_lista
    print(producto(lista))
    print(elimina(lista))
    print(es_capicua(lista))
