#Está fea mi resolución la verdad...

def diadelasemana(dia = int, mes = int, anio = int) -> int:
    '''
    Contrato: Permite averiguar el día de la semana para una fecha determinada.

    pre: los tres datos deben ser enteros y positivos.
    post: devuelve un entero (del 0 al 6) que representa el día de la semana.

    '''

    if mes < 3:
        mes = mes + 10
        año = año - 1

    else:
        mes = mes - 2

    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26 * mes - 2)// 10) + dia + anio2 + (anio2//4) + (siglo//4) - (2 * siglo)) % 7

    if diasem < 0:
        diasem = diasem + 7

    return diasem


def imprime_calendario(mes = int, anio = int, diasem = int) -> None:
    '''
    Contrato: Imprime un calendario que muestra el inicio de semana y todos sus días
    según los datos ingresados.

    pre: los datos deben ser enteros y positivos.
    post: no devuelve nada, solo imprime.

    '''
    total_dias = 0 #Primero calculo cuantos dias va a tener el calendario. 
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            total_dias = 29

        else:
            total_dias = 28

    elif mes in (4, 6, 9, 11):
        total_dias = 30

    else:
        total_dias = 31

    posicion = diasem #Arranca desde el diasem y cuando llega a 7 hace un salto de línea.

    print("\nDom. Lun. Mar. Mie. Jue. Vie. Sab.")
    print("    " * diasem, end = "")

    for i in range(total_dias):
        print(f"{i+1}", end = "")
        print(" ", end = "")
        posicion += 1

        if posicion == 7:
            print("")
            posicion = 0


def main() -> None:
    while True:
        mes = int(input("\nIngrese el mes: "))
        anio = int(input("Ingrese el año: "))

        if (mes > 1 and mes <= 12) and (anio > 0 and anio < 9999):
            break

    diasem = diadelasemana(1, mes, anio)

    imprime_calendario(mes, anio, diasem)


if __name__ == "__main__":
    main()