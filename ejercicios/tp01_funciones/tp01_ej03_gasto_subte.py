'''Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.'''

def aplica_descuento(viajes = int) -> float:
    '''
    Aplica los descuentos correspondientes según los viajes realizados.
    precondiciones = el valor de viajes solo puede sere positivo y entero.
    postcondiciones = devuelve un float con los descuentos aplicados.

    '''
    tarifa_total = 1753.04
    gastos_mes = 0
    descuentos = [0.60, 0.70, 0.80] #Lo que se paga del boleto según el descuento aplicado.
    cantidades = [41, 31, 21] #El rango mínimo de viaje para que se aplique el descuento.

    if viajes < 21:
        gastos_mes = viajes * tarifa_total
        return gastos_mes

    else:
        for descuento, cantidad in zip(descuentos, cantidades):
            if cantidad <= viajes:
                resto = viajes - cantidad
                viajes -= resto
                gastos_mes += resto * (tarifa_total * descuento)

        gastos_mes += viajes * tarifa_total

        return gastos_mes
            

def main():
    viajes = 0
    while viajes < 1:
        viajes = int(input("Ingrese la cantidad de viajes realizados: "))

    gasto = aplica_descuento(viajes)
    print(f"El gasto total de los viajes fue: {gasto}")


if __name__ == "__main__":
    main()
