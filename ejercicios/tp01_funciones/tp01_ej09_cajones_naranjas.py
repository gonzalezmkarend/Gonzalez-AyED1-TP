
from random import randint

def separa_cosecha(naranjas=list) -> tuple:
    """
    Contrato: Verifica el peso de las naranjas y las clasifica en dos grupos: aptas y jugo.

    pre: la lista que recibe no debe estar vacía.
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


def carga_cajones(aptas=list):
    """
    Contrato: Carga los cajones con 100 naranjas cada uno y calcula el peso de los mismos. Si hay sobrantes calcula su peso y número

    pre: la lista que recibe no debe estar vacía.
    post: devuelve una tupla con dos valores: una lista con los pesos de los cajones y otra tupla con la cantidad de sobrante 
    y su peso (en caso de que sobre).

    """
    cant_caj = len(aptas) // 100
    sueltas = len(aptas) % 100

    cajones = []

    for i in range(cant_caj):
        # Como ya se las cantidades que guardan los cajones y cuántos necesito, voy sacando de a 100 naranjas.
        inicio = i * 100
        peso = sum(aptas[inicio : inicio + 100])

        cajones.append(
            peso
        )  # Y guardo el peso total del cajón en una lista de cajones.

    sobrante = 0  # Si no hay sueltas vuelve en 0.
    if sueltas > 0:
        peso = sum(
            aptas[-sueltas:]
        )  # Si hay sueltas también suma su peso. Puede que sea medio YAGNI pero me pareció útil.
        sobrante = (sueltas, peso)

    return (cajones, sobrante)


def carga_camiones(cajones=list) -> tuple:
    """
    Contrato: Calcula cuántos camiones se van a necesitar para transportar los cajones de naranjas.

    pre: la lista de cajones no debe estar vacía.
    post: devuelve una tupla que contiene la cantidad de camiones que se necesitan y el peso sobrante si hubiese.

    """
    cargas = (400, 500)
    # 
    camiones = 0
    camion = 0
    sobrante = 0 # Si no sobran cajones vuelve vacío.   
    for cajon in cajones:
        if camion + cajon <= cargas[1]:
            camion += cajon

        else:
            if camion >= cargas[0]:
                camiones += 1
                camion = cajon

            elif camion < cargas[0]:
                sobrante = camion + cajon
                break

    if camion >= cargas[0]:
        camiones += 1
    else:
        sobrante = camion

    return (camiones, sobrante)

    
def main() -> None:

    while True:
        cosecha_total = int(input("\nIngrese la cosecha total de naranjas: "))
        if cosecha_total > 0:
            break

    pesos = [randint(150, 350) for x in range(cosecha_total)]
    aptas, jugo = separa_cosecha(pesos)

    print(f"\nHay un total de: {len(aptas)} naranjas aptas en la cosecha.")

    cajones, nar_sobr = carga_cajones(aptas)
    print(f"\nLa cantidad de cajones de 100 naranjas aptas son {len(cajones)}")
    if nar_sobr[0] > 0:
        print(f"\nLa cantidad de naranjas sueltas son: {nar_sobr[0]}, con un peso de {nar_sobr[1]/100} kg")

    else:
        print("\nNo quedaron naranjas sueltas.")

    camiones, sobrante = carga_camiones(cajones)
    print(f"Se necesitan {camiones} para repartir la cosecha de naranjas.")
    if sobrante > 0:
        print(f"Hubo un total de {sobrante} kg de naranja que quedará para el próximo reparto.")

    else:
        print(f"No hubo cajones sobrantes.")


if __name__ == "__main__":
    main()
