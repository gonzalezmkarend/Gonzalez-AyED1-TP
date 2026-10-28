def carga_datos() -> list[int]:
    """
    Contrato: Permite cargar datos ingresados por teclado a una lista vacía uno por uno.

    Precondiciones: No recibe ningún dato.
    Postcondiciones: Devuelve una lista de enteros.

    """
    lista = []

    while True:
        try:
            num = int(input("\nIngrese un número entero: "))

        except ValueError:
            print("\nError. Debe ingresar números enteros")

        else:
            if num == -1:
                break
            else:
                lista.append(num)

    return lista


def busca_valor(lista: list[int], valor: int) -> int:
    """
    Contrato: Busca la posición de un valor ingresado por el usuario.

    Precondiciones: La lista no debe estar vacía y la variable valor debe ser entera.
    Postcondiciones: En caso de encontrar el valor solicitado en la lista, devuelve su índice positivo, en caso contrario devuelve -1.

    """
    try:
        indice = lista.index(valor)

    except ValueError:
        return -1

    else:
        return indice


def main() -> None:
    """Función principal."""

    lista = carga_datos()
    contador_errores = 0

    while True:
        try:
            num = int(input("\nIngrese el valor que desea buscar: "))
            buscador = busca_valor(lista, num)

        except ValueError:
            print("\nError. Debe ingresar un número entero.")

        else:
            if buscador == -1:
                contador_errores += 1
                print("\nEl valor solicitado no se encuentra en la lista.")

            else:
                print(f"\nLa posición del valor solicitado es: {buscador}")

            if contador_errores == 3:
                print("\nSe alcanzó el límite máximo de intentos en el plan gratuito...")
                break


if __name__ == "__main__":
    main()
