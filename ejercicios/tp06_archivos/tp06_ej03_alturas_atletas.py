# Sin terminar


def _ingresar_cadena(msg: str) -> str:
    """
    Contrato:
        - Permite ingresar datos por teclado.

    Precondiciones:
        - Recibe un string, mensaje de input.

    Postcondiciones:
        - str; devuelve el dato ingresado por teclado.
    """
    return input(msg)


def grabar_rango_alturas(deportes: set[str]) -> bool:
    """
    Contrato:
        - Graba en un archivo (si no existe, lo crea) las alturas de los distintos atletas de las distintas disciplinas.

    Precondiciones:
        - Un conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False

    try:
        with open("alturas_por_deporte.txt", "wt", encoding="utf-8") as arch:
            for deporte in deportes:
                arch.write(deporte + "\n")
                print(f"Deporte: {deporte}")

                while True:
                    altura = _ingresar_cadena(
                        "Ingrese la altura del atleta (-1 para salir): "
                    )

                    if altura == "-1":
                        break

                    arch.write(altura + "\n")

    except OSError:
        print("\nError. No se pudo acceder al archivo")
        return False

    else:
        return True


def grabar_promedio() -> bool:
    """
    Contrato:
        - Graba en un archivo (si no existe, lo crea) e promedio de las alturas de los atletas de las distintas disciplinas.

    Precondiciones:
        - No recibe datos

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    try:
        with open("alturas_por_deporte.txt", "rt", encoding="utf-8-sig") as arch:
            suma_alturas = 0.0
            contador = 0
            promedios = {}
            deporte = None

            for linea in arch:
                try:
                    linea = float(linea)

                except ValueError:
                    if not deporte:
                        deporte = linea.strip()

                    else:
                        if suma_alturas:
                            promedios[deporte] = suma_alturas / contador
                            suma_alturas = 0.0
                            contador = 0
                            deporte = linea.strip()

                else:
                    suma_alturas += linea
                    contador += 1

            # Guardo en el diccionario el deporte y el promedio que me quedaron
            # en las variables.
            if suma_alturas:
                promedios[deporte] = suma_alturas / contador

    except OSError:
        print("\nError. No se pudo acceder al archivo.")
        return False

    # Ahora guardo los promedios en otro archivo
    try:
        with open("promedios_por_deporte.txt", "wt", encoding="utf-8") as arch:
            for deporte, promedio in promedios.items():
                arch.write(deporte + "\n")
                arch.write(str(promedio) + "\n")

    except OSError:
        print("\nError. No se pudo acceder al archivo.")
        return False

    else:
        return True


def mostrar_mas_altos() -> float|None:
    """
    Contrato: Calcula el promedio general de todas las disciplinas.
    
    Precondiciones: No recibe nigún dato.
    Postcondiciones: Si no se pudo acceder al archivo no devuelve nada.
    Si se pudo realizar el promedio lo devuelve como una variable flotante.
    Si no hay promedios para calcular no devuelve nada.
    
    """
    try:
        with open("promedios_por_deporte.txt", "rt", encoding= "utf-8") as arch:
            promedio_gral = 0.0
            contador = 0

            for linea in arch:
                try:
                     linea = float(linea)

                except ValueError:
                    continue

                else:
                    promedio_gral += linea
                    contador += 1

            if contador:
                promedio_gral = promedio_gral / contador

                return promedio_gral

            else:
                return

    except OSError:
        print("\nError. No se pudo acceder al archivo.")
        return




def main() -> None:
    """Programa principal."""
    deportes = {
        "Fútbol",
        "Básquetbol",
        "Golf",
        "Waterpolo",
        "Judo",
        "Rugby",
        "BMX",
        "Críquet",
    }

    grabar_rango_alturas(deportes)
    grabar_promedio()
    promedio = mostrar_mas_altos()


if __name__ == "__main__":
    main()
