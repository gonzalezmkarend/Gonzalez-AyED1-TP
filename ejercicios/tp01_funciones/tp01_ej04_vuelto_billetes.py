def calcula_vuelto(compra = int, paga = int) -> tuple:
    '''
    Calcula la cantidad de billetes que tiene que darle el cajero de vuelto.
    pre: ambos datos deben ser enteros
    post: devuelve una tupla con los datos.

    '''
    vuelto = paga - compra
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    cambio = [ ]

    if vuelto % 10 != 0:
        print("No es posible entregar la totalidad del vuelto porque no hay billetes menores a $10.")

    else:
        for billete in billetes:
            cantidad_billetes = vuelto // billete
            cambio.append(cantidad_billetes)
            vuelto -= cantidad_billetes * billete
                 
        return (billetes, cambio)


def main() -> None:
    compra = 0
    while compra < 10: #Establezco $10 como la compra mínima.
        compra = int(input("Ingrese el monto a cobrar: "))

    paga = 0
    while paga < 1:
        paga = int(input("Ingrese el dinero recibido: "))

    if paga < compra:
        print("ERROR: El monto ingresado no es suficiente.")

    elif paga == compra:
        print("Gracias por comprar!")

    else:
        billetes, cambio = calcula_vuelto(compra, paga)
        for i, x in zip(billetes, cambio):
            if x > 0:
                print(f"Se devuelve {x} billetes de ${i}.")

      

if __name__ == "__main__":
    main()
