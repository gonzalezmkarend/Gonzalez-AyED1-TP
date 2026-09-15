'''Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.'''

def verifica_validez(dia = int, mes = int, anio = int) -> bool:
    '''
    Verifica la validez de la fecha en conjunto.
    precondiciones = los datos deben ser enteros positivos.
    postcondiciones = si la fecha es válida devuelve True, en caso contrario devuelve False.

    '''
    valido = True

    #si el mes es febrero, verifico primero si el año es bisiesto.
    bisiesto = False
    if mes == 2:
        if anio % 4 == 0 and anio % 100 != 0:
            bisiesto = True

        elif anio % 400 == 0:
            bisiesto = True

        if bisiesto == True and dia > 29:
            valido = False

        elif dia > 28:
            valido = False

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            valido = False

    return valido

def main() -> None:
    pass

if __name__ == "__main__":
    main()