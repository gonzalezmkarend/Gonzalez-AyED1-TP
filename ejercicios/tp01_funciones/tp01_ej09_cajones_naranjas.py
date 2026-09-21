"""Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo."""

# Mi interpretación de la consigna es que, si quedan naranjas sueltas (que no logran completar un cajón) 
# quedan como sobrantes. Si quedan también cajones sin enviar porque no se logró completar el peso mínimo del camión, 
# también son sobrantes para el próximo viaje pero son dos categorías distintas: naranjas sueltas y cajones.

import random

random.seed(0)


def genera_peso(naranja) -> int:
    """
    Contrato: Genera un peso aleatorio para asignarles a las naranjas.

    Pre: el dato debe ser entero y positivo.
    Post: Devuelve un entero positivo entre 150g y 350g.

    """

    peso = random.randint(150, 350)

    return peso


def separa_cosecha(naranjas=list) -> tuple:
    """
    Contrato: Verifica el peso de las naranjas y las clasifica en dos grupos: aptas y jugo.

    pre: los datos que recibe deben ser enteros positivos.
    post: devuelve una tupla con dos listas, una con las naranjas aptas y otra con las de jugo.

    """
    aptas = []
    jugo = []

    for naranja in naranjas:
        if naranja >= 200 and naranja <= 300:
            aptas.append(naranja)

        else:
            jugo.append(naranja)

    return (aptas, jugo)


def carga_cajones(aptas = list):
    """
    Contrato: Se encarga de cargar los cajones con naranjas aptas.

    pre: la lista que recibe no debe estar vacía.
    post:

    """
    cajones_jugo = 0


def carga_camiones():
    """
    Contrato: Se encarga de cargar los camiones con los cajones de naranjas.

    pre:
    post:

    """
    pass


def main() -> None:
    
    while True:
        cosecha_total = int(input("\nIngrese la cosecha total de naranjas: "))
        if cosecha_total > 0:
            break

    pesos = []
    for nar in range(cosecha_total):
        nar = genera_peso(nar)
        pesos.append(nar)

    aptas, jugo = separa_cosecha(cosecha_total)
    


if __name__ == "__main__":
    main()
