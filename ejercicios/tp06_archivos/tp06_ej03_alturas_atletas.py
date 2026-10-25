"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los próximos juegos panamericanos.
Para eso encargó la realización de un programa que incluya las siguientes funciones:

grabar_rango_alturas(): Graba en un archivo las alturas de los atletas de distintas disciplinas,
los que se ingresan desde el teclado. Cada dato se debe grabar en una linea distinta.

grabar_promedio(): Graba en un archivo los promedios de las alturas de los atletas,
leyendo los datos del archivo generado en el paso anterior. La disciplina y el promedio debe grabarse en lineas diferentes.

mostrar_mas_altos(): Muestra por pantalla las disciplinas deportivas cuyos atletas superan la estatura promedio general.
Obtener los datos del segundo archivo.
"""

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

    with open("alturas_por_deporte.txt", "at", encoding="utf-8") as arch:
        
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

        for linea in arch:
            pass
        
    



def main() -> None:
    """ "Programa principal."""
    deportes = {"Fútbol", "Básquetbol", "Golf", "Waterpolo", "Judo", "Rugby", "BMX", "Críquet"}

    grabar_rango_alturas(deportes)


if __name__ == "__main__":
    main()