'''Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
'''

def verifica_fechas() -> tuple:
    '''
    Verifica que el dia, mes y anio sean enteoros y válidos individualmente según el calendario.
    precondiciones: no recibe ningún dato.
    postcondiciones: devuelve tres datos enteros positivos en una tupla.
    '''
    dia = 0
    while dia < 1 or dia > 31:
        dia = int(input("Ingrese el día: "))

    mes = 0
    while mes < 1 or mes > 12:
        mes = int(input("Ingrese el mes: "))

    anio = 0
    while anio < 1 or anio > 9999:
        anio = int(input("Ingrese el año: "))

    return (dia, mes, anio)

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
    dia, mes, anio = verifica_fechas()
    es_valido = verifica_validez(dia, mes, anio)
    if es_valido == True:
        print(f"La fecha {dia}/{mes}/{anio} es válida.")

    else:
        print(f"La fecha {dia}/{mes}/{anio} es inválida.")


if __name__ == "__main__":
    main()

assert verifica_validez(15, 8, 2026) == True
assert verifica_validez(22, 2, 2025) == True
assert verifica_validez(29, 2, 1900) == False
assert verifica_validez(31, 4, 2000) == False