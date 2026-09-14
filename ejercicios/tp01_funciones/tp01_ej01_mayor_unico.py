def ingresa_num() -> tuple:
    '''
    Ingresa los números a evaluar y los devuelve en una tupla.
    Precondiciones:
    Postcondiciones: devuelve una tupla con tres números enteros positivos.
    '''
    a = 0
    while a < 1:
        a = int(input("Ingrese un número A: "))
               
    b = 0
    while b < 1:
        b = int(input("Ingrese un número B: "))
        
    c = 0
    while c < 1:
        c = int(input("Ingrese un número C: "))
        
    return (a, b, c)

def mayor_unico(a: int, b: int, c: int) -> int:
    '''
    Busca y devuelve el mayor de los tres números ingresados.
    pre-condiciones: a, b y c deben ser enteros positivos.
    post-condiciones: devuelve un solo valor.
        
    '''
    mayor = 0
    
    if a > b:        
        if a > c:
            mayor = a
            
    if b > a:        
        if b > c:
            mayor = b
            
    if c > a:        
        if c > b:
            mayor = c
    
    if mayor > 0:
        return mayor

    else:
        return -1
    
    
def main() -> None:
    a, b, c = ingresa_num()
    num = mayor_unico(a, b, c)
    if num > 0:
        print(f"El único número mayor de los ingresados fue: {num}")
                            
    else:
        print("No se ingresaron mayores únicos.")


if __name__ == "__main__":
    main()     