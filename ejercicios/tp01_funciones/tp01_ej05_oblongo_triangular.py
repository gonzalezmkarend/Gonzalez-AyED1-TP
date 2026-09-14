''' Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas.'''

#---Lambda de oblongo:
oblongo = lambda num: ((4 * num + 1) ** (1/2)) % 1 == 0 

#---Lambda triangular:
triangular = lambda num: ((1 + 8 * num) ** (1/2)) % 1 == 0

while num < 1:
    num = int(input("Ingrese un número: "))
    assert num > 0 #El número ingresado debe ser positivo

    es_oblongo = oblongo(num)

    if es_oblongo == True:
        print(f"El número {num} es oblongo.")

    else:
        print(f"El número {num} no es un oblongo.")

    es_triangular = triangular(num)
    if es_triangular == True:
        print(f"El número {num} es triangular.")

    else:
        print(f"El número {num} no es triangular")

assert oblongo(12) == True
assert oblongo(10) == False
assert triangular(15) == True
assert triangular(11) == False
