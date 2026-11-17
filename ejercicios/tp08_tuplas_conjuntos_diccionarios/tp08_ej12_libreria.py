class NumeroNegativo(Exception):
    pass


def crear_diccionario(productos: list[str]) -> dict[str, float]:
    """
    Contrato: Permite crear un diccionario con los nombres
    de producto como clave y su precio como valor. El precio
    del producto es ingresado por teclado.

    Precondiciones: La lista de productos debe estar vacía y
    sus elementos no deben estar repetidos.
    Postcondicones: Devuelve un diccionario.

    """
    diccionario = {}
    for producto in productos:
        print(f"\n{producto}")
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))

                if precio <= 0.0:
                    raise NumeroNegativo

            except (ValueError, NumeroNegativo):
                print("\nError. Debe ingresar un número positivo.")

            else:
                diccionario[producto] = precio

                break

    return diccionario


def main() -> None:
    """Función principal del programa"""

    productos = ["Lapicera", "Cuaderno", "Lápiz", "Carpeta", "Regla"]
    dicc = crear_diccionario(productos)

    if dicc:
        dicc["Cuaderno"] *= 1.15

    print("\n------Catálogo de productos y precios------")
    for producto, precio in dicc.items():
        print(f"\n{producto}: ${precio:.2f}")


if __name__ == "__main__":
    main()
