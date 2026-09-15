'''Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.'''

def concatenar_num(num1 = int, num2 = int) -> int:
    '''
    Recibe dos enteros y los devuelve concatenados.
    pre: ambos números deben ser enteros positivos.
    post: los números son devueltos en una variable entera.

    '''
    assert num1 > 0 and num1 <= 99_999 #Establezco que ambos números deben ser positivos 
    assert num2 > 0 and num2 <= 99_999 #y con un límite en 99.999.

    num_entero = num2
    digitos = 0 #contador
    while num_entero > 0:
        #Obtengo la cantidad de dígitos de num2
        num_entero = num_entero // 10
        digitos += 1

    num_concat = num1 * (10**digitos) + num2

    return num_concat

def main() -> None:
    while True:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        break

    concatenado = concatenar_num(num1, num2)

    print(f"El resultado de la concatenación fue: {concatenado}")

    assert concatenar_num(123, 456) == 123456
    assert concatenar_num(9, 12) == 912


if __name__ == "__main__":
    main()