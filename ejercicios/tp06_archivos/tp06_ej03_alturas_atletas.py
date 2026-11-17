

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
        - Una conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False

    with open("alturas_por_deporte.txt", "wt", encoding="utf-8") as arch:
        
        for deporte in deportes:
            arch.write(deporte + "\n")
            print(f"Deporte: {deporte}")

            while True:
                altura = _ingresar_cadena("Ingrese la altura del atleta (-1 para salir): ")

                if altura == "-1":
                    break
                
                arch.write(altura + "\n")


def grabar_promedio(deportes: set[str]) -> bool:
    """
    Contrato:
        - Graba en un archivo (si no existe, lo crea) e promedio de las alturas de los atletas de las distintas disciplinas.

    Precondiciones:
        - Una conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False
    
    with open("alturas_por_deporte.txt", "rt", encoding="utf-8-sig") as arch:
        pass      



def main() -> None:
    """Programa principal."""
    deportes = {"Fútbol", "Básquetbol", "Golf", "Waterpolo", "Judo", "Rugby", "BMX", "Críquet"}

    grabar_rango_alturas(deportes)


if __name__ == "__main__":
    main()