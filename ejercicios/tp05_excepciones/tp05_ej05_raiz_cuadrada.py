from math import sqrt


class NumeroNegativo(Exception):
    pass


def raiz_cuadrada(num) -> float:
    """
    Contrato: Permite calcular la raiz cuadrada de un número.

    Precondiciones: La variable num debe ser mayor a 0 y su valor no puede ser negativo.
    Postcondiciones: Devuelve la raíz cuadrada del número ingresado.

    """
    return sqrt(num)


def main() -> None:
    """Función principal."""

    while True:
        try:
            num = float(input("\nIngrese un número para calcular la raíz cuadrada: "))
            if num < 0.0:
                raise NumeroNegativo

        except ValueError:
            print("\nError. Debe ingresar un número.")

        except NumeroNegativo:
            print(
                "\nError. No se puede calcular la raíz cuadrada de un número negativo. Ingrese un número positivo."
            )

        except Exception as error:
            print(error)

        else:
            print(raiz_cuadrada(num))
            break


if __name__ == "__main__":
    main()
