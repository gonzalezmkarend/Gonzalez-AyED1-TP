
def numero_romano(num: int) -> str:
    '''
    Contrato: Convierte un número entero entre el 0 y el 3999 en número romano.
    
    Precondiciones: El número ingresado debe ser entero y positivo.
    Postcondiciones: Devuelve un string de .
    
    '''
    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    m = num // 1000
    c = (num % 1000) // 100
    d = (num // 10) % 10
    u = num % 10

    return millares[m]+centenas[c]+decenas[d]+unidades[u]


while True:
    numero = int(input("Ingrese un número: "))
    if numero >= 0 and numero <= 3999:
        break

print(numero_romano(numero))