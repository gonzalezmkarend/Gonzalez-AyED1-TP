from random import randint


def main() -> None:
    """
    Contrato: Función principal que organiza la ejecución del programa.

    Pre: No recibe ningún dato.
    Post: Muestra por pantalla el resultado de la ejecición.

    """

    lista = [randint(1, 100) for x in range(30)]
    a_eliminar = lista[::2]

    print(f"\nLa lista original: {lista}")

    for num in a_eliminar:
        if num in lista:
            lista.remove(num)

    print(f"\nLos valores a eliminar: {a_eliminar}")

    print(f"\nLa lista resultante: {lista}")


if __name__ == "__main__":
    main()
