'''Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.'''


def aplica_descuento(viajes = int) -> float:
    '''
    Aplica los descuentos correspondientes según los viajes realizados.
    precondiciones = el valor de viajes solo puede sere positivo y entero.
    postcondiciones = devuelve un float con los descuentos aplicados.

    '''
    tarifa = 1753.04
    gastos_mes = 0

    if viajes < 20:
        gastos_mes = tarifa * viajes
        return gastos_mes

    else:
        pass


def main():
    viajes = 0
    while viajes < 1:
        viajes = int(input("Ingrese la cantidad de viajes realizados: "))

    gasto = aplica_descuento(viajes)
    print(f"El gasto total de los viajes fue: {gasto}")


if __name__ == "__main__":
    main()
