def aplica_descuento(viajes=int) -> float:
    """
    Contrato: Aplica los descuentos correspondientes según los viajes realizados.

    pre: el dato ingresado viajes debe ser entero y positivo.
    post: devuelve un float que representa el gasto mensual con los descuentos aplicados.

    """
    assert viajes > 0

    tarifa_total = 1753.04
    gastos_mes = 0
    descuentos = [
        0.60,
        0.70,
        0.80,
    ]  # Lo que se paga del boleto según el descuento aplicado.
    cantidades = [
        41,
        31,
        21,
    ]  # El rango mínimo de viaje para que se aplique el descuento.

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
    while True:
        viajes = int(input("Ingrese la cantidad de viajes realizados: "))
        if viajes > 0:
            break

    gasto = aplica_descuento(viajes)
    print(f"El gasto total de los viajes fue: {gasto}")


if __name__ == "__main__":
    main()
